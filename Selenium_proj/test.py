from selenium import webdriver
import time
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\19082\chromedriver.exe')

# Go to the page that we want to scrape
driver.get("https://www.thumbtack.com/instant-results/?zip_code=08831&keyword_pk=102906936653958006&project_pk=")

