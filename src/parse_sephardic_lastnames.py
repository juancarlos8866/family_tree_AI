import re
import pandas as pd
import PyPDF2

class SephardicLastNameParser:
    @staticmethod
    def extract_text_from_pdf(pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    @staticmethod
    def extract_data(text):
        pattern = r'(.*?)\s*((?:\([^)]+\))+)'
        matches = re.findall(pattern, text)
        
        data = []
        for lastname, refs in matches:
            lastname = lastname.strip()
            if lastname:  # Only add non-empty lastnames
                references = re.findall(r'\(([^)]+)\)', refs)
                data.append([lastname] + references)
        
        return data

    @staticmethod
    def create_dataframe_lastname(data):
        max_refs = max(len(row) - 1 for row in data)
        columns = ['Lastname'] + [f'Reference_{i+1}' for i in range(max_refs)]
        
        df = pd.DataFrame(data, columns=columns)
        return df