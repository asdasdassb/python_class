from bs4 import BeautifulSoup
import cfscrape
from datetime import datetime

localtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
for i in range(1,4):
    scraper=cfscrape.create_scraper()
    result=scraper.get('https://icook.tw/recipes/popular?page')
    soup=BeautifulSoup(result.text,"html.parser")
    find_id = soup.find('dl' , class_="dl-horizontal prevname h3")
    titles=soup.find_all("h2",attrs={"class":"browse-recipe-name"})

print('目前icook網站上的人氣食譜'+'\n'+'查詢時間為'+localtime)
for s in titles:
    print("標題:"+s.text.strip())

    