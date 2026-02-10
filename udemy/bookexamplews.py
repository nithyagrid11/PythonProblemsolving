import requests
import bs4


'''base_url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
page_num = 12
base_url.format(page_num)
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,"lxml")
products = soup.select('.product_pod')
#print(products)
example = products[0]
#print(type(example))
#print(example.attrs)
#print(example.select('.star-rating.Four'))
#print(example.select('.star-rating.Two'))
#print([] == example.select('.star-rating.Two'))
print(example.select('a')[1])
print(example.select('a')[1]['title'])'''

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
#print(soup.select('.author'))

'''quotes = []
for name in soup.select('.text'):
    quotes.append(name.text)
print(quotes)'''

'''for name in soup.select('.tag-item'):
    print(name.text)'''

url = 'http://quotes.toscrape.com/page/'
#print(url + str(10))
authors = set()
for page in range(1,10):
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    for name in soup.select('.author'):
        authors.add(name.text)
print(authors)
