from xml.dom.minidom import DocumentFragment
import pageReader
import DirectoryVariable

from selenium import webdriver   
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

def getStartups():
    None;
    # Selenium Work Here
    driver.get(DirectoryVariable.url);


    time.sleep(5)

    # Using BeautifulSoup using Selenuim
    html = driver.page_source.encode('utf-8').strip()
    document = BeautifulSoup(html , "html.parser");

    # Main code here
    startup_cards = document.find_all(class_ = 'deck_list_item');
    # print((startup_cards));

    for startup in startup_cards:
        # pageReader.SlideCapture(startup.find('a').get('href'))
        DirectoryVariable.startups_links.add(startup.find('a').get('href'));

    driver.quit();