
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from sqlalchemy import create_engine
from selenium import webdriver
import xlsxwriter
import pyodbc
from pyodbc import *
from sqlalchemy import create_engine
start = time.time()
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
today_year = today[0:4]
today_month = today[5:7]

####### Import of Pages URL of Topics #######
url_address = pd.DataFrame()
url_address.loc[0 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/travel'
url_address.loc[0 , 'Topic'] = 'travel'
url_address.loc[1 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/art'
url_address.loc[1 , 'Topic'] = 'art'
url_address.loc[2 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/animals-pets'
url_address.loc[2 , 'Topic'] = 'animals-pets'
url_address.loc[3 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/architecture'
url_address.loc[3 , 'Topic'] = 'architecture'
url_address.loc[4 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/cars-motorcycles'
url_address.loc[4 , 'Topic'] = 'cars-motorcycles'
url_address.loc[5 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/celebrities'
url_address.loc[5 , 'Topic'] = 'celebrities'
url_address.loc[6 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/cooking'
url_address.loc[6 , 'Topic'] = 'cooking'
url_address.loc[7 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/design'
url_address.loc[7 , 'Topic'] = 'design'
url_address.loc[8 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/diy-crafts'
url_address.loc[8 , 'Topic'] = 'diy-crafts'
url_address.loc[9 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/education'
url_address.loc[9 , 'Topic'] = 'education'
url_address.loc[10 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/fashion'
url_address.loc[10 , 'Topic'] = 'fashion'
url_address.loc[11 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/film-music-books'
url_address.loc[11 , 'Topic'] = 'film-music-books'
url_address.loc[12 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/food-drink'
url_address.loc[12 , 'Topic'] = 'food-drink'
url_address.loc[13 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/game'
url_address.loc[13 , 'Topic'] = 'game'
url_address.loc[14 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/gardening'
url_address.loc[14 , 'Topic'] = 'gardening'
url_address.loc[15 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/hair-beauty'
url_address.loc[15 , 'Topic'] = 'hair-beauty'
url_address.loc[16 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/health-fitness'
url_address.loc[16 , 'Topic'] = 'health'
url_address.loc[17 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/humor'
url_address.loc[17 , 'Topic'] = 'humor'
url_address.loc[18 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/kids-parenting'
url_address.loc[18 , 'Topic'] = 'kids-parenting'
url_address.loc[19 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/nature-outdoors'
url_address.loc[19 , 'Topic'] = 'nature-outdoors'
url_address.loc[20 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/photography'
url_address.loc[20 , 'Topic'] = 'photography'
url_address.loc[21 , 'LinkAddress'] = 'https://starngage.com/app/global/influencer/ranking/iran-islamic-republic-of-persian-gulf/technology'
url_address.loc[21 , 'Topic'] = 'technology'

####### Crawl of Data #######
driver = webdriver.Chrome(executable_path= r'E:\python codes\shakh\chromedriver.exe')
data_primary_total = pd.DataFrame()
for j in range(0, len(url_address)):  # len(url_address)
    url_page = url_address.loc[j , 'LinkAddress']
    driver.get(url_page)
    time.sleep(10)
    data_primary = pd.DataFrame()
    for i in range(1, 101):
        print(j, '-----', i)
        data_primary.loc[i, 'Genre'] = url_address.loc[j , 'Topic']
#        try:
#            number = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[1]'.format(i))
#            data_primary.loc[i, 'number'] = number.text
#        except: pass
        try:
            Username = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[3]'.format(i))
            data_primary.loc[i, 'Username'] = Username.text
        except: pass
        try:
            Country = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[4]/div/span/a'.format(i))
            data_primary.loc[i, 'Country'] = Country.text
        except: pass
        try:
            Topics = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[5]'.format(i))
            data_primary.loc[i, 'Topics'] = Topics.text
        except: pass
        try:
            Followers = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[6]'.format(i))
            data_primary.loc[i, 'Followers'] = Followers.text
        except: pass
        try:
            Engagement_Rate = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[7]'.format(i))
            if Engagement_Rate.text != '':
                data_primary.loc[i, 'EngagementRate'] = Engagement_Rate.text
            else:
                for counter in range(5):
                    time.sleep(2)
                    Engagement_Rate = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/table/tbody/tr[{}]/td[7]'.format(i))
                    if Engagement_Rate.text != '':
                        data_primary.loc[i, 'EngagementRate'] = Engagement_Rate.text
                        break
        except: pass
    data_primary_total = data_primary.append([data_primary_total])

data_primary_total_save = data_primary_total.copy()
####### Import of Date and Time #######
data_primary_total['DateTime_year'] = today_year  # change year
data_primary_total['DateTime_month'] = today_month   # change month
print(data_primary_total['DateTime_month'])
data_primary_total['DateTime_day'] = '01'
data_primary_total['DateTime_time'] = '01'
data_primary_total['DateTime'] = data_primary_total['DateTime_year']+data_primary_total['DateTime_month']+data_primary_total['DateTime_day']+data_primary_total['DateTime_time']
del data_primary_total['DateTime_year']
del data_primary_total['DateTime_month']
del data_primary_total['DateTime_day']
del data_primary_total['DateTime_time']
data_primary_total = data_primary_total.reset_index()
del data_primary_total['index']

####### Cleaning Followers #######
data_primary_total['Followers1'] = data_primary_total['Followers']
data_primary_total['Followers2'] = data_primary_total['Followers']
data_primary_total['Followers1'] = data_primary_total['Followers1'].str.replace('M', '')
data_primary_total['Followers1'] = data_primary_total['Followers1'].str.replace('K', '')
data_primary_total['Followers1'] = data_primary_total['Followers1'].astype(float)
data_primary_total['Followers2'] = data_primary_total['Followers2'].fillna('NoData')
data_primary_total = data_primary_total [~data_primary_total.Followers2.str.contains('NoData')]
data_primary_total_1 = data_primary_total [data_primary_total.Followers.str.contains('M')]
data_primary_total_2 = data_primary_total [data_primary_total.Followers.str.contains('K')]
data_primary_total_1['Followers1'] = data_primary_total['Followers1']*1000000
data_primary_total_2['Followers1'] = data_primary_total['Followers1']*1000
data_primary_total = data_primary_total_1.append([data_primary_total_2])
del data_primary_total['Followers']
del data_primary_total['Followers2']
data_primary_total = data_primary_total.rename(columns={"Followers1":"Followers"})
data_primary_total = data_primary_total.reset_index()
del data_primary_total['index']
#del data_primary_total['number']

####### Export to SQL Server #######
drivers = pyodbc.drivers()
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=localhost;'
                      'Database=ShakhInstagram;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
for index, row in data_primary_total.iterrows():
    cursor.execute("INSERT INTO ShakhInstagram.dbo.ShakhInstagram (Topics,Genre,Country,Username,EngagementRate,Followers,DateTime) values(?,?,?,?,?,?,?)", row.Topics,row.Genre,row.Country,row.Username,row.EngagementRate,row.Followers,row.DateTime)
    conn.commit()

####### Export to Postgres #######
engine = create_engine('postgresql://postgres:12344321@10.32.141.17/Moein01',pool_size=20, max_overflow=100,)
con=engine.connect()
data_primary_total.to_sql('ShakhInstagram',con,if_exists='append', index=False)
con.close()

####### End #######

print("--- %s seconds ---" % (time.time() - start))


#print(data_primary_total.loc[600, 'EngagementRate'])






