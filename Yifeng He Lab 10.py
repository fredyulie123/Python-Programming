# Yifeng He Lab 10
fileName = 'C:/Users/Yifeng He/Desktop/IO/jazz.html'
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
## Extra Challenge ##
pageNum = int(input('Please tell us page number you need to scrape: \n>>'))
for k in range( 0, pageNum):
    if k == 0:
       url = 'https://www.yelp.com/biz/jazz-standard-new-york'
    else:
        url = 'https://www.yelp.com/biz/jazz-standard-new-york?start=' + str(k*20)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    with open(fileName, 'a', encoding = 'utf-8') as jazzHTML:
        jazzHTML.write(soup.prettify())
# url = 'https://www.yelp.com/biz/jazz-standard-new-york' #Yelp site
# page = urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
# prettified = soup.prettify()
# with open (fileName, 'w', encoding = 'utf-8') as jazzHTML:
    #jazzHTML.write(prettified)

with open(fileName, 'r', encoding = 'utf-8') as jazzHTML:
    page = jazzHTML.read()
soup = BeautifulSoup(page, 'html.parser')
# soup.find(itemprop='description')
# comment = soup.find(itemprop='description').get_text()
# print(comment)
# soup.find(itemprop='datePublished')
# date = soup.find(itemprop='datePublished')['content']
# author = soup.find(itemprop='author')['content']
# stars = soup.find(itemprop='ratingValue')['content']
# print(date,author,stars)
allReviews = []

reviews = soup.find_all(itemprop='review')
for review in reviews:
    comment = review.find(itemprop='description').get_text()
    date = review.find(itemprop='datePublished')['content']
    author = review.find(itemprop='author')['content']
    stars = review.find(itemprop='ratingValue')['content']
    allReviews.append([comment, date, author, stars])
    
reviewFrame = pd.DataFrame(allReviews)
print(reviewFrame)


