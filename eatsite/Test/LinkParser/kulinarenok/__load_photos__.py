import requests
import openpyxl
from slugify import slugify

sheet = openpyxl.load_workbook('data.xlsx').active
titles = []
for i in range(2, 1716):
    title = sheet[f"B{i}"].value
    if title not in titles:
        _id = sheet[f"A{i}"].value
        url = sheet[f"N{i}"].value
        name = f"{slugify(title) + str(i)}.jpg"
        p = requests.get(url)
        out = open("C:\\Users\\allelleo\\Desktop\\eat\\eatsite\\media\\preview_photo\\" + name, "wb")
        out.write(p.content)
        out.close()
        titles.append(title)