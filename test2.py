import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("section", class_="job_list")
job_elements = results.find_all("div", class_="job")

# Defining of the dataframe
df = pd.DataFrame(columns=['Job title', 'Location', 'Date', 'Job Type', 'Company','Job Detail'])

for job_element in job_elements:
    title_element = job_element.find('h1').a.text
    infos = job_element.find_all('span',class_= "info")
    job_detail = job_element.find('p',class_= "detail").get_text()
    job_location = infos[0].get_text()
    job_date =infos[1].get_text()
    job_type = infos[2].get_text()
    company = infos[3].get_text() 

    df = df.append({'Job title':title_element, 'Location':job_location, 'Date':job_date, 'Job Type':job_type, 'Company':company,'Job Detail':job_detail}, ignore_index=True) 

#print(df)
df.to_csv('file_name.csv',index=False)
