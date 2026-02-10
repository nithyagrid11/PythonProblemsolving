import requests
import bs4

result = requests.get("https://www.example.com/")
#print(type(requests))
#print(result.text) #the content in that page is stored as a gaint string
soup = bs4.BeautifulSoup(result.text,"lxml")
'''print(soup)
print(soup.select('title')) #prints in list and prints the tags too
print(soup.select('p'))
print(soup.select('title')[0].getText()) #will give text in the title tag without printing title tag
site_paragraphs = soup.select('p')
print(site_paragraphs) #will give a list
print(site_paragraphs[0].getText()) #will give the text in string format
print(site_paragraphs[0]) #will give the text with p tag'''

#res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
#soup = bs4.BeautifulSoup(res.text,"lxml")
#print(soup)
#print(res.status_code)
#print(res.text[:403])
#print(soup.select('.vector-toc-text'))

#grabing an image.   #image can give copyright
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,"lxml")
#print(soup)
print(soup.select('img '))