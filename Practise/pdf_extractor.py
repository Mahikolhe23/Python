import pdfplumber
import pandas as pd


pdf_path = '/Users/mahendrakolhe/Downloads/3-06-26 Tenterfield REPORT NM.pdf'

pdf = pdfplumber.open(pdf_path)
for page in pdf.pages:    
    text = page.extract_tables()
    lines_array = text[0]
    final_list = []
    current_line = 0
    for num in range(current_line, len(lines_array)):
        current_client = current_site = current_location = ''
        line = lines_array[num]
        pattern = 'Location'
        matches = [string for string in line if string is not None and  string.find(pattern) != -1]
        if matches: 
            print(matches)
        # print(line)
        for word in line:
            if word is not None and 'Client' in word:
                current_client = line[0]
                # current_line += 1
            if word is not None and 'Site' in word:
                current_site = line[1]
                # print(current_site)
                # current_line += 1
            if word is not None and 'Location' in word:
                current_location = line[2]
                # print(current_location)
                # current_line += 1
        # print(line)
        # print(f'{current_client} {current_site} {current_location}')

