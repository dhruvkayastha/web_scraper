from PyPDF2 import PdfFileReader
import os
os.environ['no_proxy'] = '*' 
 
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        file = open("raw.txt",'a')
        # file = open("corpus/pdf_text_raw.txt", 'a')
        # file = open("test.txt",'w')
        for i in range(40,891):
            page = pdf.getPage(i)
            text = page.extractText()
            file.write(text) 
            file.write("\n")

        file.close()
 
file_path = 'art.pdf'
if __name__ == '__main__':
    # text_extractor(file_path)
    pass
from tika import parser

# Parse data from file
file_data = parser.from_file(file_path)
# Get files text content
text = file_data['content']
# file = open("raw.txt",'a')
file = open("corpus/pdf_text_raw.txt", 'a')
file.write(text)
file.close()
# # print(text)