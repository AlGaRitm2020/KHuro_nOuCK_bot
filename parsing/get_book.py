from bs4 import BeautifulSoup
import requests
async def parse_book(query):
    url = 'https://www.labirint.ru/search/' + query
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, "html.parser")
    allImg = soup.findAll('img', class_='book-img-cover')
    allNames = soup.findAll('a', class_='product-title-link')
    allAuthors = soup.findAll('div', class_='product-author')
    
    data = allImg[0]
    begin_index = str(data).find('src') + 5
    end_index = 0
    for i in range(begin_index, len(str(data))):
        if str(data)[i] == '"':
            end_index = i
            break
    img_address = str(data)[begin_index:end_index]
    response = requests.get(img_address)
    byte_img = response.content
    
    name = allNames[0].find('span', class_='product-title').text
    author = allAuthors[0].find('span').text
    
    urlbook = soup.findAll('a', class_='product-title-link')
    begin_index = str(urlbook).find('href') + 6
    end_index = 0
    for i in range(begin_index, len(str(urlbook))):
        if str(urlbook)[i] == '"':
            end_index = i
            break
    newurl = str(urlbook)[begin_index:end_index]
    
    url = 'https://www.labirint.ru'+newurl
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    disc = soup.find('noindex').text
    disci = disc.find('...')
    disc = disc[0:disci]
    
    
    amount = soup.findAll('span', class_='js-open-block-page_count self analytics-click-js')
    begin_index = str(amount).find('data-pages') + 12
    end_index = 0
    for i in range(begin_index, len(str(amount))):
        if str(amount)[i] == '"':
            end_index = i
            break
    amount = str(amount)[begin_index:end_index]
    
    genre = soup.find('a', class_='books-rating__link')
    genre = genre.find('span')
    begin_index = str(amount).find('<') + 7
    for i in range(begin_index, len(str(genre))):
        if str(genre)[i] == '<':
            end_index = i
            break
    genre = str(genre)[begin_index:end_index]

    return name, author, byte_img, amount, genre, disc, url
    
    
    #genre - жанр
    #url - ссылка на книгу
    #byte_img - байт картинка
    #name - название книги
    #author - автор
    #disc - описание книги
    #amount - количество страниц
