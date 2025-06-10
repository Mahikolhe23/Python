import pdfplumber
import pandas as pd


pdf_path = '/Users/mahendrakolhe/Downloads/3-06-26 Tenterfield REPORT NM.pdf'

pdf = pdfplumber.open(pdf_path)
lines = []
for page in pdf.pages:    
    text = page.extract_tables()
    str_arr = text[0]

    # if text is not None:
    #     liness= text.split('\n')
    #     lines += liness

# for l in lines:
#     print(l)
    for arr in str_arr:
        print(arr)

# for arr in str_arr:
#     print(arr)
#     for word in arr:
#         if word is not None and 'Client' in word:
#             print(arr)


