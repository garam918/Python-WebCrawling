from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium import webdriver as wd

driver = wd.Chrome(r"C:\Users\ijy91\Downloads\chromedriver_win32\chromedriver.exe")

url = "https://www.youtube.com/watch?v=9YCAkdUljHM"
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
user_ID = []
comments = []

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    time.sleep(2.5)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source
driver.close()

soup = BeautifulSoup(html_source, "html.parser")
youtube_user_IDs = soup.select("div#header-author > a > span") # 유저의 ID
youtube_comments = soup.select("yt-formatted-string#content-text") # 댓글

for i in range(len(youtube_user_IDs)):
    user_ID.append(youtube_user_IDs[i].text.strip())
    comments.append(youtube_comments[i].text.strip())
    print(user_ID[i], ':' ,comments[i])

