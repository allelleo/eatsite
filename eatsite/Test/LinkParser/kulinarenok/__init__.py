from bs4 import BeautifulSoup
import requests
from lxml import etree

links = open(r'C:\Users\allelleo\Desktop\eat\eatsite\Test\LinkParser\Links.txt', 'r').readlines()
urls = []
counter = 1606
err = 0

def write(title, KitchenType, CookingTime, PortionCounter, CaloricContent, Squirrels, Fats,
          Carbohydrates, Water, ingredients, steps, category, photo, quote, url):
    global counter
    with open(f"recipes/{counter}.txt", "w") as f:
        f.write(str(title))
        f.write(str("\n"))
        f.write(str(KitchenType))
        f.write(str("\n"))
        f.write(str(CookingTime))
        f.write(str("\n"))
        f.write(str(PortionCounter))
        f.write(str("\n"))
        f.write(str(CaloricContent))
        f.write(str("\n"))
        f.write(str(Squirrels))
        f.write(str("\n"))
        f.write(str(Fats))
        f.write(str("\n"))
        f.write(str(Carbohydrates))
        f.write(str("\n"))
        f.write(str(Water))
        f.write(str("\n"))
        f.write(str("ING--#@"))
        f.write(str(ingredients))
        f.write(str("ING--#@"))
        f.write(str("STEPS--&%"))
        f.write(str(steps))
        f.write(str("STEPS--&%"))
        f.write(str("CAT--&%"))
        f.write(str(category))
        f.write(str("CAT--&%"))
        f.write(str("\n"))
        f.write(str("PH--&%"))
        f.write(str(photo))
        f.write(str("PH--&%"))
        f.write(str("\n"))
        f.write(str("QUOE--&%"))
        f.write(str(quote))
        f.write(str("QUOE--&%"))
        f.write(str("\n"))
        f.write(str(url))
    counter += 1


for link in links:
    if link:
        if link.strip():
            if link != "undefined" and not "undefined" in link:
                urls.append(link.replace("\n", "").replace(" ", ""))
urls = list(set(urls))
for url in urls:
    try:
        page = requests.get(url)
        if not page.status_code == 200:
            continue
        print(url)

    #if 1==1:
        soup = BeautifulSoup(page.text, "html.parser")
        dom = etree.HTML(str(soup))
        title = soup.findAll('h1', class_='card-wrap__title fn')[0].text
        if "5 рецептов" in title: continue
        if "5 простых" in title: continue
        if "5 самых" in title: continue
        if "5" in title: continue
        # print(title)
        KitchenType = soup.findAll('span', itemprop='recipeCuisine')[0].text
        # print(KitchenType)
        CookingTime = \
            dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/span[2]')[
                0].text.strip()
        # print(CookingTime.strip())
        PortionCounter = \
            dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[4]/span[2]')[
                0].text.strip()
        # print(PortionCounter.strip())

        CaloricContent = \
            dom.xpath('/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[5]/span[2]')[
                0].text.strip()
        # print(CaloricContent.strip())
        Squirrels = \
            dom.xpath(
                '/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[6]/div/span[2]')[
                0].text.strip()
        # print(Squirrels.strip())
        Fats = \
            dom.xpath(
                '/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[7]/div/span[2]')[
                0].text.strip()
        # print(Fats.strip())
        Carbohydrates = \
            dom.xpath(
                '/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[8]/div/span[2]')[
                0].text.strip()
        # print(Carbohydrates.strip())
        Water = \
            dom.xpath(
                '/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[9]/div/span[2]')[
                0].text.strip()
        # print(Water.strip())
        DietaryFiber = \
            dom.xpath(
                '/html/body/div[1]/main/section/div/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div[10]/div/span[2]')[
                0].text.strip()
        # print(DietaryFiber.strip())
        quote = soup.findAll('div', itemprop='description')[0].text
        # print(quote.text)

        ingredients = soup.findAll('label', itemprop='recipeIngredient')
        ing = ""
        for i in ingredients:
            string = f"{i.findAll('span', class_='ingredients-table__td name')[0].text} {i.findAll('span', class_='value')[0].text}{i.findAll('span', class_='type')[0].text}"
            ing += string + "\n\n"

        # steps
        steps = soup.findAll('div', class_='pr-steps__item')
        st = ""
        for step in steps:
            step_ = step.findAll('div', class_='pr-steps__content')[0].findAll('div', class_='pr-steps__body instruction')[0].text.strip()
            st += step_ + "\n\n"
            #print(step_)

        category = \
            dom.xpath('/html/body/div[1]/main/section/div/div[1]/ol/li[2]/a/span')[0].text
        # print(category)
        photo = soup.findAll('img', itemprop='resultPhoto')[0]
        link = "https://kulinarenok.ru" + photo['src']
        write(title, KitchenType, CookingTime, PortionCounter, CaloricContent, Squirrels, Fats, Carbohydrates, Water, ing, st, category, link, quote, url)

    except Exception as e:
        print(str(e) + str(err))
        print(url)
        err+=1
