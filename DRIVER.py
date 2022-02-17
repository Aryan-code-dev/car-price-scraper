import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path=r"C:\Users\Aryan Dande\Downloads\gecko\geckodriver.exe")
#url = "https://www.cardekho.com/used-cars+in+pune"
#url = "https://www.cars24.com/buy-used-car?sort=P&storeCityId=2423&pinId=411001"
#url=" https://droom.in/cars/used"
#url="https://www.olx.in/pune_g4059014/cars_c84"
#url = " https://www.ola.cars/listings/buy-used+city-is-pune"
#url="https://www.spinny.com/used-cars-in-pune/s/"
#url="https://www.carwale.com/used/cars-in-pune/"
urls = ["https://www.cardekho.com/used-cars+in+pune" ,"https://www.cars24.com/buy-used-car?sort=P&storeCityId=2423&pinId=411001","https://www.spinny.com/used-cars-in-pune/s/"]

for j in range(3):
    driver.maximize_window()
    driver.get(urls[j])
    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    time.sleep(5)
    if j == 0:
        set3 = soup.find_all("div", class_="holder hover",limit=100)
        for k in set3:
            print(k.getText())
    elif j == 1:
        set3 = soup.find_all("div", class_="_1l4fi")
        for k in set3:
            print(k.getText())
    else:
        set3 = soup.find_all("div", class_="styles__carDetailContainer")
        for k in set3:
            print(k.getText())


#print(soup.prettify())