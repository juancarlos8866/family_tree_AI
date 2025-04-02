import re
import pandas as pd

class SephardicReferenceParser:
    @staticmethod
    def extract_references(text):
        # Pattern to match reference numbers and their descriptions
        pattern = r'\((\d+[a-z]?)\)\s*(.*?)(?=\(\d+[a-z]?\)|\Z)'
        matches = re.findall(pattern, text, re.DOTALL)
        
        references = {}
        for number, description in matches:
            references[number] = description.strip()
        
        return references

    @staticmethod
    def create_dataframe(references):
        df_source = pd.DataFrame(list(references.items()), columns=['Reference_Number', 'Reference_Source'])
        return df_source

    @staticmethod
    def get_list_text():
        # Text from 
        # https://jewishgen.org/databases/sephardic/SephardimComNames.html
        text = """
        (0) Self identified
        (1) From the civil records of Amsterdam, The Netherlands.(~)
        (2) From the records of Bevis Marks, The Spanish and Portuguese Congregation of London.(~)
        (3) From the burial register of Bethahaim Velho Cemetery, Published by the Jewish Historical Society of England.(~)
        (4) From the book, "History of the Jews in Venice", by Cecil Roth.(~)
        (5) Sephardic names extracted from the book, "Finding Our Fathers", by Dan Rottenberg. Each name is followed by a short biography and references for
        additional information. This book is a fine reference for those interested in learning Jewish genealogy research. The publication explains how and where to
        conduct research and can be purchased on this site through Amazon.com
        (6) From the book, " The Inquisitors and the Jews in the New World", by Seymour B. Liebman.(~)
        (6a) Reports the names of people who appeared before the inquisition in the New Spain.(~)
        (6b) Reports the names of people who appeared before the inquisition in New Granada.(~)
        (6c) Reports the names of people who appeared before the inquisition in El Peru.(~)
        (6d) Reports the names of people who appeared before the inquisition in Rio de La Plata.(~)
        (7) From the book, "A History of the Marranos", by Cecil Roth.(~)
        (8) From the book, "Jews in Colonial Brazil", by Arnold Wizhitzer.(~)
        (9) From the book, "Precious Stones of the Jews of Curacao Jewry 1657-1957.(~)
        (10) From the book, "The Jews of Rhodes", by Marc D. Angel.(~)
        (11) List of (mostly) Sephardic brides from the publication, "List of 7300 Names of Jewish Brides and Grooms who married in Izmir Between the Years 1883-
        1901 & 1918-1933.(~)
        (12) List of (mostly) Sephardic grooms from the publication listed above.(Izmir lists provided by Dov Cohen, Nof Ayalon Israel). Email
        address dkcohen@neto.net.il(~)
        13) From the book, "The Jews of New Spain", by Seymour B. Liebman.(~)
        (14) From the publication, "Los Sefardes", by Jose M. Estrugo. Published by Editorial Lex La Habana, 1958. (Apellidos corrientes entre los Sephardies)(~)
        (15) From the book, "The Jews of the Balkans, The Judeo-Spanish Community , 15th to 20th Centuries", by Esther Benbassa and Aron Rodrigue.(~)
        (16) From the book, "The Sephardic Jews of Bordeaux", by Frances Malino.(~)
        (17) From the book, "Hebrews of the Portuguese Nation", by Miriam Bodian.(~)
        (18) From the book, "The Sephardim of England", by Albert M. Hyamson.(~)
        (19) From Vol. 1, "A History of the Jews in Christian Spain", by Yitzhak Baer. (19a) Volume II.(~)
        (20) From the book, "A Life of Menasseh Ben Israel", by Cecil Roth. This book contains names from the Sephardic community of greater Amsterdam.
        Amsterdam was a major haven and transfer point for Sephardim and Morranos leaving Iberia.(~)
        (21) From the book, "Crisis and Creativity in the Sephardic World: 1391-1648", by Gampel. This book lists Sephardic movers and shakers during the period.(~)
        (22) From the book, "History of the Jews in Aragon", by Regne. Essentially a series of royal decrees by the House of Aragon. It contains Sephardic names
        recorded during the period 1213-1327. By this time family names were well developed. Be prepared for a challenge as you attempt to derive the modern
        equivalents for these 800 year old names. Prefixes such as Aben, Ibn, Aven, Avin, Ben and etc. are attached to the stemsof many names.If your people came
        from Aragon, and you cannot find the name in this list, I recommend to attach a prefix and look for it in that way. In addition, the spelling of many of the stems
        have changed with time. Some names (Adret, Cavalleria) exist to this date unchanged. This reference will introduce many new names and/or many new
        spellings to known names. (22c) indicates those names that are identified as converso names in the records. Suerte!(~)
        (23) From the book, "Secrecy and Deceit: The Religion of theCrypto-Jews", by David Gitlitz. The names of the Sephardim (and their residences) mentioned
        were, sometimes, involved with the inquisition. There were other names which are not listed here because the author did not identify those names as
        Sephardic.(~)
        (24) From the Ph.D. Dissertation of Michelle M. Terrill, "The Historical Archaeology of the 17th and 18th-Century Jewish Community of Nevis, British West
        Indies", Boston Univesity, 2000.(~)
        (25) From the book, "The Jews of Jamaica", by Richard D. Barnett and Philip Wright. This book contains tombstone inscriptions and dates of death from 1663-
        1880. Only names that appeared Sephardic are included here.(~)
        (26) From the book, "Die Sefarden in Hamburg" (The Sephardim in Hamburg [Germany]) by Michael Studemund-Halevy. German names are due to inter
        marriage(~)
        (27) From the book, "Historia de la Comunidad Isralelita de Chile", by Moshe Nes-El.(~)
        (28) From the book, "Judios Conversos" (Jewish Converts) by Mario Javier Saban. Los antepasados Judios de las familias Argentinas. This work contains many
        Sephardic names and family trees within its 3 volumes. Many of the individuals listed appeared before the inquistion and were secret Jews. Some later
        converted and intermarried. The description "Jew "and "Portuguese" appear to be used interchangeably. Only those names that were identified as Sephardic
        Jews or descendant from Sephardic Jews or in some cases, new Christians that married into Sephardic families are listed here. It is possible that some
        Sephardic names not well identified are not listed. If you have Sephardic/Portuguese family roots in early Argentina, research these volumes. Many of the
        names listed here represent the famous names of Jewish/Sephardic Argentina. Wonderful family trees, well detailed, are provided in the three volumes.(~)
        (28a) List of Portuguese Jews expelled from Buenos Aries, 1603. The list also contains the name of the vessel and date of arrival in Argentina. Los
        "Portugueses" Judaizantes expulsados de Buenas Aires.(~)
        (28b) "Portuguese" of Santiago del Estro. The list provides the year of arrival and entry point into Argentina. Apellidos de los Portugueses de Santiago del
        Estero.(~)
        (28c) "Portuguese" of Cordoba. Apellidos de los Portugueses de Cordoba. The list provides the entry point and the year of arrival.(~)
        (28d) "Portuguese" of San Miguel de Tucuman. The book provides the entry and the year of arrival in Argentina.(~)
        (28e) "Portuguese" of Talavera (1607). The list provides entry point and the year of arrival.(~)
        (28f) "Portuguese" of La Rioja. The list provides entry point and the year of arrival.(~)
        (28g) "Portuguese" of Salta. The book provides the entry point and the year of arrival.(~)
        (28h) "Portuguese" of Villa de Madrid de las Juntas. The book provides entry point and the year of arrival.(~)
        (28i) "Portuguese" of Jujuy. The book provides the entry point and the year of arrival.
        (28j) "Portuguese" registered in Santa Fe in 1643. The book provides entry point and the year of arrival.(~)
        (28k) List of names of those Sephardim expelled from Santa Fe. The book provides the place of birth and the year of arrival.(~)
        (28l) Jewish Portuguese families of Rio de la Plata.(~)
        (28m) Sephardic names in the records of the Auto de Fe of Lima in 1639.(~)
        (28n) The Oliver-Cavia family, descendants of the Jewish house of Ha-Levi Benveniste originally from Spain.(~)
        (28o) List of the "Portuguese" of Corrientes in the year 1643. Book provides age and place of birth.(~)
        (29) "Sangre Judia" ("Jewish Blood") by Pere Bonnin. A list of 3,500 names used by Jews, or assigned to Jews by the Holy Office (la Santo Oficio) of Spain. The
        list is a result of a census of Jewish communities of Spain by the Catholic Church and as found in inquisition records. Los Apellidos estan sacados de las listas
        de penitenciados por el Santo Oficio, de los censos de las juderias y de otras fuentes que indican claramente que la persona portadora del apellido es judia o
        judeoconversa. Tiene Vd. sangre judia? (~)
        (30) "Raizes Judaicas No Brasil" by Flavio Mendes Carvalho. This book contains names of Sephardim involved in the inquisition in Brazil. Many times date of
        birth, occupation, name of parents, age, and location of domicile are also included. Included in this list are the names of the relatives of the victims. Many of the
        victims were tortured to death or exiled so their lines might end here.(~)
        (31) Sephardic names from the magazine "ETSI". Most of the names are from (but not limited to) France and North Africa. Published by Laurence Abensur-
        Hazan and Philip Abensur. Subscriptions are available. If your family comes from the area served by ETSI, this magazine is worth while.
        <http://www.geocities.com/EnchantedForest/1321> (31/volume number/issue number) For example (31/3/8) = Esti volume 3, issue8. (~)
        (32) Sephardic surnames from the classic book "Genealogia Hebraica: Portugal e Gibraltar", by Jose Maria Abecassis. This book contains a list of names of
        Sephardim families that returned to Portugal and Gibralter after hundreds of years of expulsion. Family trees are included for many of the families. (~)
        (33) Sephardic names from the Jewish Historical Society of England. List of names provided by David Ferdinando dferdinando@gmail.com. (~)
        (33a) "The First English Jew", by Lucien Wolf. (~)
        (33b) "Crypo-Jews under the Commonweath", by Lucien Wolf. (~)
        (33c) "The Jewery of the Restoration", by Lucien Wolf.(~)
        (33d) "The Cemetery of the Resettlement", by Master A.S. Diamond. (~)
        (33e) "Foreign Trade of London Jews in the 17th Century", by Maurice Woolf.
        (33f) "The Community of the Resettlement 1656-84 - A Social Survey:, by A.S. Diamond. (~)
        (33g) "Maria Fernandez de Carvajal" by Lucien Wolf. (~)
        (33h) "Carvajal and Pepys", by Wilfred Samuel. (~)
        (33i) Extracts from "Jews of the Canary Islands", ed. Lucien Wolf. (~)
        (33j) "Process of Antao Rodigues Lindo, Native of Badajoz, Kingdom of Castile". (~)
        (34) From the book, "In Sure Dwellings: A Journey From Expulsion to Assimilation", by Margot F. Salom. The names are extracted from the research of an
        Austalian, Ms. Salom, into the her family. The names have been provided by the author. The book may be purchased form Seaview Press. FP 2000, Adelaide,
        5th Australia. The author's email address is Abshl@powerup.com.au. (~)
        (35) From the book "Histoire des Juifs de Rhodes, Chio, Cos, etc, by Abraham Galante. The names were extracted and provided by Daniel
        Kazez danielkazez@gmail.com.(~)
        (36) Sephardic names extracted from the book, "Noble Families Among The Sephardic Jews" by Isaac Da Costa, Bertram Brewster, and Cecil Roth. This book
        provides genealogy information about many of the more famous Sephardic families of Iberia, England and Amsterdam. For those tracing Sephardim from
        Spain to England or to Amsterdam, this book can be most valuable. Many name changes and aliases are provided. This reference documents the assimilation,
        name changes and coversion of many Sephardic families in Spain, England and The Netherlands. There is also a large section dealing the the genealogy of the
        members of Capadose family that converted to Christianity. (~)
        (37) Sephardic names from the book, "A Origem Judaica dos Brasileiros", by Jose Geraldo Rodrigues de Alckmin Filho, who personally provided the text. This
        publication contains a list of 517 Sephardic families punished by the inquisition in Portugal and Brazil. As familias punidas pela Inquidicao em Portugal e no
        Brasil.. (~)
        (38)Names from the book, "El Libro Verde de Aragon" (The Greenbook of Aragon) by Isidoro de las Cagigas.(~)
        (38a) Sephardic names to Converso (New Christian) names. Sephardic=Converso.|(~)
        (38b) Converso names from Sephardi names. Converso=Sephardic.(~)
        (38c) Sephardic names of Aragon.(~)
        (39) From ETSI, Volume 4, No.12 dated March 2001, "Aliases in Amsterdam", by Viberke Sealtiel-Olsen, a list of alias names used by Sephardim in
        Amsterdam. A wonderful research tool for Sephardic research in Amsterdam.(~)
        (39a) True Sephardic Name=Alias Name (~)
        (39b) Alias Name=True Sephardic Name.(~)
        (40) The Circumcision Register of Isaac and Abraham De Paiba (1715-1775) from the Achives of the Spanish and Portuguese Jews' Congregation of Bevis
        Marks (London. England). Family names include those circumcised, God fathers, and God mothers. There are also short sections of additional circumcisions
        1679-99 (40a), Marriages 1679-89 (40b), and births of daughters 1679-99(40c) (~)
        (41) "Conversos on Trial" by Haim Bienart. A well written story of the converso community of Ciudad Real, to include the converso inquisition trials in the
        mid 15th century. This book contains a list of names, some times providing the names of relatives, house locations, and professions. A fine resource for those
        with ties to Ciudad Real. (~)
        (42) Jewish names contained in Medieval documents from the Kingdom of Murcia. Apellidos judios en documentos medievales del Reino de Murcia. Most of
        these names, if not all, appear to be original Sephardic names not changed by conversion. (~)
        (43) Sephardic names from the site TARAZONA JUDIA. 43 (C) indentifies converso anmes .The site is presented as a memorial to the Jews of
        TARAZONA. (~) http://idd00bmy.eresmas.net/etarazonajudiaapellidos.html
        (44) From the site, "Los Apellidios Biblicos De Mallorica" (Biblical Names of Mallorca) by Miquel Ferra I Martorell. This site can be found
        at http://www.iciba.org.il/archivo/mallorca.html (44C) New Christians or Conversos from Mallorca..
        (45) Apellidos de Judios Sefardies (Surnames of the Sephardic Jews) from the site Comunidad Israelita Pincipado de Austurias. This site can be found
        at http://www.sefarad.as/apell/apea.htm
        (46) "Diciionario Sefaradi De Sobrenomes" ("Dictionary of Sephardic Surnames"): This reference provides thousand of Sephardic names of immigrants to
        Brazil. The authors have attempted to provide the ports of departure of these immigrants. The source of this information is also available.
        """
        # Include the full text from your original file here
        return text

