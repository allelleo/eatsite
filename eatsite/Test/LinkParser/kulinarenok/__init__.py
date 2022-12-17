from bs4 import BeautifulSoup
import requests
from lxml import etree

links = open(r'C:\Users\allelleo\Desktop\eat\eatsite\Test\LinkParser\Links.txt','r').readlines()
urls = []
for link in links:
    if link:
        if link.strip():
            urls.append(link.replace("\n", "").replace(" ",""))

for url in urls:
    page = requests.get(url)
    if not page.status_code == 200:
        continue
    try:
        soup = BeautifulSoup(page.text, "html.parser")
        dom = etree.HTML(str(soup))
        title = soup.findAll('h1', class_='card-wrap__title fn')[0]
        print(title.text)
        KitchenType = soup.findAll('span', itemprop='recipeCuisine')[0]
        print(KitchenType.text)
        CookingTime = dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/span[2]')[0].text
        print(CookingTime)
        PortionCounter = dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[4]/span[2]')[0].text
        print(PortionCounter)

        CaloricContent = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[5]/span[2]')[0].text
        print(CaloricContent)
        Squirrels = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[6]/div/span[2]')[0].text
        print(Squirrels)
        Fats = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[7]/div/span[2]')[0].text
        print(Fats)
        Carbohydrates = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[8]/div/span[2]')[0].text
        print(Carbohydrates)
        Water = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[9]/div/span[2]')[0].text
        print(Water)
        DietaryFiber = \
        dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[10]/div/span[2]')[0].text
        print(DietaryFiber)
        quote = soup.findAll('div', itemprop='description')[0]
        print(quote.text)

        ingredients = soup.findAll('label', itemprop='recipeIngredient')
        for i in ingredients:
            string = f"{i.findAll('span', class_='ingredients-table__td name')[0].text} {i.findAll('span', class_='value')[0].text}{i.findAll('span', class_='type')[0].text}"
            print(string)


        # steps
        steps = soup.findAll('div', class_='pr-steps__item')
        for step in steps:
            print(step.findAll('div', class_='pr-steps__content')[0].findAll('div', class_='pr-steps__body instruction')[0].text)

        category = \
        dom.xpath('/html/body/div[1]/main/section/div/div[1]/ol/li[2]/a/span')[0].text
        print(category)

    except: pass