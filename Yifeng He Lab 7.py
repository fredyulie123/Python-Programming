#Yifeng He Lab 7
# Part A – Pandas
file_name = 'C:/Users/Yifeng He/Desktop/IO/tickerInfo.csv'
import pandas as pd
df = pd.read_csv(file_name)
max_close = df['Close'].max()
print(max_close)
closing_prices = list(df['Close'])

# Part B – MatPlotLib
import matplotlib.pyplot as plt
x = range(len(closing_prices))
plt.plot(x, closing_prices)
plt.show()

# Part C – NLTK
comment = 'It is a bad experience in this hotel, however, the room service is the best I\'ve ever experienced!'
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(comment)
print(sentiment_scores['compound'])

# Part D – Beautiful Soup
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://www.musicpriceguide.com'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
title_tags = soup.find_all(title = True)
for a in title_tags:
    print(a)
    
for a in title_tags:
    print(a.get_text())    