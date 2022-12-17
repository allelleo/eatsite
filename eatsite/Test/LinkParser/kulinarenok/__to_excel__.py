'''from openpyxl import Workbook

data = "data.xlsx"
wb = Workbook()
ws = wb.active
ws['A4'].value'''

import os


for address, dirs, files in os.walk(r'C:\Users\allelleo\Desktop\eat\eatsite\Test\LinkParser\kulinarenok\recipes'):
    for name in files:
        path = os.path.join(address, name)
        file = open(path, 'r')
        data = file.read()
        title = data.split("\n")[0]
        kitchenType = data.split("\n")[1]
        cookingTime = data.split("\n")[2]
        PortionCounter = data.split("\n")[3]
        CaloricContent = data.split("\n")[4]
        Squirrels = data.split("\n")[5]
        Fats = data.split("\n")[6]
        Carbohydrates = data.split("\n")[7]
        Water = data.split("\n")[8]
        ingredients = data.split("ING--#@")[1]
        steps = data.split("STEPS--&%")[1]
        category = data.split("CAT--&%")[1]
        photo_link = data.split("PH--&%")[1]
        quote = data.split("QUOE--&%")[1]
        origin = data.split("\n")[-1]
        break
    break
