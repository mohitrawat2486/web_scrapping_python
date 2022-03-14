import requests
import pandas as pd
from bs4 import BeautifulSoup
URL = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="_3Mn1Gg")
product_div = results[2]
infos = product_div.select('div[class="_1AtVbE col-12-12"]',limit=1)
#print(data)
for info in infos:
    #a_data = info.find('a')
    a_data = '<a><div class="_3pLy-c row"></div></a>'; 
    a_div = a_data.find('div',class_="_3pLy-c")
    #prod_name = a_div.find('div',class_="_4rR01T").text
    
    print(a_data)
    print()