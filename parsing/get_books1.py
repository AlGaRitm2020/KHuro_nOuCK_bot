from bs4 import BeautifulSoup
import requests
import random

import json
import asyncio


async def get_books(query):
    # get dict from json
    with open("data/categories1.json", "r", encoding="utf-8") as categories:
        url_dict = json.load(categories)
        print(url_dict)
    page = str(random.randint(1, 51))
    url = url_dict[query] + page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_books= soup.findAll('table', class_='island')
    indexes=[random.randint(0, 24) for _ in range(1)]
    book_list = []
    blacklist = ["Эротика", "Порно"]
    for i in indexes:
        book = all_books[i]
        name = book.find("span", itemprop="name").text
        try:
            rate = book.find("span", class_="orange_desc").text
        except Exception:
            rate = "Оценки нет"
        author = book.find("span", itemprop="author").text
        genre = book.find("span", itemprop="genre").text.replace("...","")
        is_bad = False
        for black in blacklist:
            if black in genre:
                is_bad = True
        if is_bad == True:
            continue
        about = (book.find("div", itemprop="description").text.replace("\xa0", "").replace("\n", ""))[:1000]
        try:
            link = url[:url.index("e/")+1] + book.find("a", class_="read")["href"]
        except Exception:
            link = 'https://www.litmir.me/'
        pages = book.findAll("span", class_="desc2")[-1].text
        img = url[:url.index("e/")+1] + book.findAll("img", alt=f"{name}")[0]["data-src"]
        book = {"name":name,
                "rate":rate,
                "genre":genre,
                "author":author,
                "about":about,
                "link":link,
                "pages":pages,
                "img":img}
        book_list.append(book)
    return book_list

