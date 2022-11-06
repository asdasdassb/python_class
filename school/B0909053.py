from bs4 import BeautifulSoup
import cfscrape

scraper=cfscrape.create_scraper()
result=scraper.get('https://www.chinatimes.com/hotnews?chdtv')
soup=BeautifulSoup(result.text,"html.parser")
titles=soup.find_all("h3",attrs={"class":"title"})

print('中時新聞網熱門列表標題')
for a in titles:
    print("標題:"+a.text.strip())