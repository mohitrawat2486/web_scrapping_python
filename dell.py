import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd

cnx=mysql.connector.connect(user="root",password='',host='127.0.0.1',database='test')
cursor=cnx.cursor()

url='https://www.dell.com/en-in/shop/laptops-2-in-1-pcs/sr/laptops/inspiron-laptops'
content = requests.get(url).text

soup = BeautifulSoup(content, "html.parser")

df = {'Title':[],'Price':[],'Configuration':[]}

for article in soup.find_all('article',attrs={'class':'stack-system ps-stack'}):
    titleTag = article.find('h3') 
    #title = titleTag.find('a').text
    df['Title'].append(titleTag.find('a').text)


    priceTag = article.find('div',attrs={'class':'ps-price'})
    priceSpan = priceTag.find('div',attrs={'class':'ps-dell-price'})
    #price = priceSpan.find('span',attrs={'class':'sr-only'}).findNext('span').text

    df['Price'].append(priceSpan.find('span',attrs={'class':'sr-only'}).findNext('span').text)

    ##config
    configDiv = article.find('div',attrs={'class':'iconography-feature-specs'})
    configDivSp = configDiv.find('div',attrs={'class':'ps-short-specs'})
    configstr1 = []
    for config in configDivSp.find_all('div'):
        configstr1.append(config.text.strip())
    
    configDivSp2 = configDiv.find('div',attrs={'class':'ps-features-icon'})
    configstr2 = []
    for config in configDivSp2.find_all('div'):
        configstr2.append(config.text.strip())
    
    configuration =  configstr1+configstr2
    configuration = '|'.join(str(x) for x in configuration)

    df['Configuration'].append(configuration)    
    #cursor.execute("INSERT INTO dell (title,price,configuration) VALUES ('"+title+"', '"+price+"','"+configuration+"')")

df2=  pd.DataFrame(df).set_index('Title')
print(df2)
df2.to_csv('dell.csv', encoding='utf-8')

#cnx.commit()
#cnx.close()      

    
