import DirectoryVariable

from selenium import webdriver   
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def getMoreStartups():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())

    driver.get(DirectoryVariable.url);

    time.sleep(DirectoryVariable.sleepDuration)

    # Using BeautifulSoup using Selenuim
    html = driver.page_source.encode('utf-8').strip()
    document = BeautifulSoup(html , "html.parser");

    # print(document.find(class_ = 'loadmore'))
    (driver.find_element(By.CLASS_NAME , 'loadmore').click())
    time.sleep(DirectoryVariable.sleepDuration)
    document = driver.page_source.encode('utf-8').strip()

    driver.quit();

    return document;