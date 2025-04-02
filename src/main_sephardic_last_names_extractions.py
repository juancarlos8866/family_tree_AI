import pandas as pd
import os
from parse_sephardic_lastnames import SephardicLastNameParser
from sephardic_references import SephardicReferenceParser

################################################################################
## Step 1: Load and parse Sephardic last names from PDF
################################################################################
print("Step 1: Load and parse Sephardic last names from PDF")
# Path to your PDF file
pdf_path = '../data/raw/Sephardim.com_Namelist.pdf'

# Create parser instances
lastname_parser = SephardicLastNameParser()
reference_parser = SephardicReferenceParser()

# Extract text from PDF
pdf_text = lastname_parser.extract_text_from_pdf(pdf_path)

# Extract data from the PDF text
extracted_data = lastname_parser.extract_data(pdf_text)

# Create pandas DataFrame
df = lastname_parser.create_dataframe_lastname(extracted_data)

# Save the DataFrame to a CSV file
output_file = '../data/processed/extracted_data.csv'
df.to_csv(output_file, index=False)

print("Data has been extracted and saved to CSV file.")

###############################################################################
# Step 2: create sephardic lastname list file with references
################################################################################
print("Step 2: Create Sephardic last name list file with references")
# Get sephardic list text 
text = reference_parser.get_list_text()
# Extract references
references = reference_parser.extract_references(text)

# Create DataFrame
df_source = reference_parser.create_dataframe(references)

# Save the DataFrame to a CSV file
df_source.to_csv('../data/processed/reference_sources.csv', index=False)
print("\nData has been extracted and saved to 'reference_sources.csv'")

# Create a dictionary with the reference_number as key and the reference_source as value
reference_dict = df_source.set_index('Reference_Number')['Reference_Source'].to_dict()
print('Dictionary for reference sources created')

# Build dataframe with Lastname, Reference_Number and Reference_Source
data = []
for _, row in df.iterrows():
    lastname = row['Lastname']
    ref_numbers = []
    ref_sources = []
    
    for ref in row[1:]:  # Skip the 'Lastname' column
        if pd.notna(ref) and ref != 'None' and str(ref) in reference_dict:
            ref_numbers.append(str(ref))
            ref_sources.append(reference_dict[str(ref)])
    
    if ref_numbers:  # Only add a row if there are references
        data.append([
            lastname,
            '; '.join(ref_numbers),
            '; '.join(ref_sources)
        ])

df_references = pd.DataFrame(data, columns=['Lastname', 'Reference_Number', 'Reference_Source'])

# Save the DataFrame to a CSV file
print("Data has been extracted and saved to '../data/processed/jewishgen_sephardic_surnames.csv'")
df_references.to_csv('../data/processed/jewishgen_sephardic_surnames.csv', index=False)