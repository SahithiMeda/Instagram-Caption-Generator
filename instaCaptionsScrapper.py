

import requests
from bs4 import BeautifulSoup
import xlsxwriter
import googletrans
from googletrans import Translator



workbook = xlsxwriter.Workbook('instaCaptions.xlsx')
worksheet = workbook.add_worksheet()


my_file = open("Links.txt", "r")
content = my_file.read()
content_list = content.splitlines()
my_file.close()
row=0

translator = Translator()

for i in content_list:
    try:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find_all("title")[0].get_text().partition(':')[2] 
        print(result)
        result = translator.translate(result)
        print(result.text)
        worksheet.write(row, 0, result.text)     # Writes in file instaCaptions
        row=row+1
    except:
        print("error in:"+ str(row))
        worksheet.write(row, 0, "CAPTION NOT LOADED")     # Writes in file instaCaptions
        row=row+1
workbook.close()
