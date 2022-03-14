from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def extract_news(url):
    print('HN Top Stories:\n'+'-'*50+'\n'+'-'*50)
    content = urlopen(url).read()
    soup = bs(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        print(str(i+1)+' :: '+tag.text + '\n' + '-'*10) if tag.text!='More' else ''
    print('End') 
    
extract_news('https://news.ycombinator.com/')