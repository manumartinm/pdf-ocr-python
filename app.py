import pandas as pd
from os import listdir
from utils import convert_pdf_to_txt
from os.path import isfile, join

files = [f for f in listdir('pdf') if isfile(join('pdf', f))]
content = []

for pdf in files:
    text = convert_pdf_to_txt(join('pdf', pdf))
    content.append({
        "Pdf": pdf,
        "Text": text
    })

pdf_df = pd.DataFrame.from_dict(content)
pdf_df.to_csv('pdf-ocr-text.csv', index=False)
