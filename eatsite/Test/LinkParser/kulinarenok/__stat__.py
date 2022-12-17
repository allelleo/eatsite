import openpyxl


sheet = openpyxl.load_workbook('data.xlsx').active
'''kitchenType = []
for i in range(1, 1715):
    kitchenType.append(str(sheet[f"C{i}"].value))

print(list(set(kitchenType)))'''

cats = []
for i in range(1, 1715):
    cats.append(str(sheet[f"M{i}"].value))

print(list(set(cats)))
