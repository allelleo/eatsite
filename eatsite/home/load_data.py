from slugify import slugify
import random
import sqlite3
import openpyxl


def normalize_time(t):
    if 'мин' in t:
        return int(t.split(" ")[0])
    else:
        if "ч" in t:
            t = t.split(" ")[0]
            if "." in t:
                h = t.split(".")[0]
                m = t.split(".")[1]
                return int(h) * 60 + int(m)
            else:
                return int(t) * 60
        else:
            if "д" in t:
                t = t.split(" ")[0]
                return int(t) * 24 * 60


def LoadKitchenTypes(model):
    Ktypes = ['Русская', 'Татарская', 'Казахская', 'Итальянская', 'Восточноевропейская',
              'Кавказская',
              'Немецкая', 'Американская', 'Восточно-европейская', 'Грузинская', 'Азиатская', 'Венгерская',
              'Французская',
              'Среднеазиатская', 'Европейская', 'Армянская', 'Узбекская', 'Восточная']

    for k in Ktypes:
        newKT = model(title=k)
        newKT.save()


def LoadRecipes():
    conn = sqlite3.connect(r"C:\Users\allelleo\Desktop\eat\eatsite\db.sqlite3")
    cur = conn.cursor()
    sheet = openpyxl.load_workbook('data.xlsx').active
    titles = []
    kitchenTypes = {
        "Мировая": 1,
        "Украинская": 2,
        "Русская": 3,
        "Татарская": 4,
        "Казахская": 5,
        "Итальянская": 6,
        "Восточноевропейская": 7,
        "Кавказская": 8,
        "Немецкая": 9,
        "Американская": 10,
        "Восточно-европейская": 11,
        "Восточно - европейская": 11,
        "Грузинская": 12,
        "Азиатская": 13,
        "Венгерская": 14,
        "Французская": 15,
        "Среднеазиатская": 16,
        "Европейская": 17,
        "Армянская": 18,
        "Узбекская": 19,
        "Восточная": 20,

    }
    cats = {
        "Праздничный стол": 1,
        "Безалкогольные напитки": 2,
        "Вторые блюда": 3,
        "Кабачки": 4,
        "Выпечка": 5,
        "Специи и пряности": 6,
        "Грибы": 7,
        "Заготовки": 8,
        "Рецепты на мангале": 9,
        "Салаты": 10,
        'Десерты, сладости': 11,
        "Закуски": 12,
        "Супы": 13,
    }
    for i in range(2, 1715):
        title = sheet[f"B{i}"].value

        if title not in titles:
            titles.append(title)
            kitchenType = sheet[f"C{i}"].value
            cookingTime = sheet[f"D{i}"].value
            PortionCounter = sheet[f"E{i}"].value
            CaloricContent = sheet[f"F{i}"].value
            Squirrels = sheet[f"G{i}"].value
            Fats = sheet[f"H{i}"].value
            Carbohydrates = sheet[f"I{i}"].value
            Water = sheet[f"J{i}"].value
            ingredients = sheet[f"K{i}"].value
            steps = sheet[f"L{i}"].value
            category = sheet[f"M{i}"].value
            photo_link = sheet[f"N{i}"].value
            quote = sheet[f"O{i}"].value
            origin = sheet[f"P{i}"].value

            sql = f"""
            INSERT INTO home_recipe( title, quote, slug,
            published_date, steps, ingredients, preview,
            views, tags, author_name, author_link, CookingTime,
            PortionCounter, CaloricContent, Squirrels, Fats,
            Carbohydrates, Water, CookingLevel_id, KitchenType_id, category_id) 
            VALUES(
    "{title}", "{quote}", "{slugify(title) + str(i)}", "2022-12-17 16:16:39.858568",
    "{steps}", "{ingredients}", "preview_photo/{slugify(title) + str(i)}.jpg",
    0, "0", "SiteName", "SiteNameLink", {normalize_time(cookingTime)}, "{PortionCounter}",
    "{CaloricContent}", "{Squirrels}", "{Fats}", "{Carbohydrates}", "{Water}",
    {random.randint(1, 3)}, "{kitchenTypes[kitchenType]}", "{cats[category]}"
    );
            """
            print(sql)
            print(i)
            cur.execute(sql)
            conn.commit()


def LoadCategories(model):
    cats = ['Праздничный стол', 'Безалкогольные напитки', 'Вторые блюда', 'Кабачки', 'Выпечка', 'Специи и пряности',
            'Грибы', 'Заготовки', 'Рецепты на мангале', 'Салаты', 'Десерты, сладости', 'Закуски', 'Супы']

    for cat in cats:
        newKT = model(title=cat)
        newKT.save()


LoadRecipes()
