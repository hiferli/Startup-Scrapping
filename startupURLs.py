import DirectoryVariable

from selenium import webdriver   
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


    time.sleep(DirectoryVariable.sleepDuration)

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

    return set(DirectoryVariable.startups_links)