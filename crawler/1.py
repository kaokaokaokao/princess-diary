from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import csv

driver = webdriver.Chrome("./chromedriver")
url = "https://www.baidu.com/"
driver.get(url)
time.sleep(2)
driver.find_element_by_css_selector('#kw').send_keys('上海外国语大学')
time.sleep(3)
driver.find_element_by_css_selector('#su').click()
time.sleep(2)
driver.find_element_by_css_selector('#\31  > div > div:nth-child(1) > h3 > a:nth-child(1)').click()
time.sleep(2)
# driver.close()