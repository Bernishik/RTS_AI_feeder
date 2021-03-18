import io
import requests
from PyPDF2 import PdfFileReader
import docx2txt


# DOCX TO TXT CONVERTER
def docx_to_txt(link):
    for idx, item in enumerate(link):
        response = requests.get(item)
        file = io.BytesIO(response.content)
        text = docx2txt.process(file)

        with open('converted_text/docx_to_txt/file-{idx}.txt'.format(idx=idx), 'w') as file:
            file.write(text)
    return 'complete'


# PDF TO TXT CONVERTER
def pdf_to_txt(link):
    for idx, item in enumerate(link):
        response = requests.get(item)
        file = io.BytesIO(response.content)

        reader = PdfFileReader(file, strict=False)

        with open('converted_text/pdf_to_txt/file-{idx}.txt'.format(idx=idx), 'w') as file:
            for i in range(reader.getNumPages()):
                contents = str(reader.getPage(i).extractText())
                file.write(contents)
    return 'complete'

# docx_to_txt('https://pasteur.epa.gov/uploads/10.23719/1500001/LDPE_nanoclay_Highlights_.docx')
# pdf_to_txt('https://www.nature.com/articles/453028a.pdf')
