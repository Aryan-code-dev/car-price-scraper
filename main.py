import requests
import time
from bs4 import BeautifulSoup
url = "https://www.cardekho.com/used-cars+in+pune"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r = requests.get(url, headers=headers)
time.sleep(10)
soup = BeautifulSoup(r.content, 'html.parser')

set1 = soup.find_all("div", class_="gsc_col-xs-7 carsName",limit=100)
set2 = soup.find_all("span", class_="amnt",limit=100)
set3 = soup.find_all("div", class_="holder hover",limit=100)

for k in set3:
    print(k.getText())

