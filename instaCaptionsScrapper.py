

import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('instaCaptions.xlsx')
worksheet = workbook.add_worksheet()


my_file = open("Links.txt", "r")
content = my_file.read()
content_list = content.splitlines()
my_file.close()
row=0

for i in content_list:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    temp = soup.find_all("title")[0].get_text().partition(':')[2] 
    print(temp)
    worksheet.write(row, 0, temp)     # Writes in file instaCaptions
    row=row+1

workbook.close()
