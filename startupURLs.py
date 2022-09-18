import DirectoryVariable
import Constants

from selenium import webdriver   
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

def GetStartups():
    numberOfStartups = DirectoryVariable.numberOfStartups;

    # Selenium Work Here
    driver.get(Constants.url);
    time.sleep(DirectoryVariable.sleepDuration)


    # Extract more codes 
    while(numberOfStartups > 0):
        driver.find_element(By.CLASS_NAME , 'loadmore').click()
        time.sleep(DirectoryVariable.sleepDuration)
        numberOfStartups = numberOfStartups - 15

    # Using BeautifulSoup using Selenuim
    html = driver.page_source
    document = BeautifulSoup(html , "html.parser");
    numberOfStartups = numberOfStartups - 15

    # Main code here
    startup_cards = document.find_all(class_ = 'deck_list_item');
    # print((startup_cards));

    countOfStartups = 0;
    for startup in startup_cards:
        if countOfStartups <= DirectoryVariable.numberOfStartups:
            # pageReader.SlideCapture(startup.find('a').get('href'))
            Constants.startups_links.add(startup.find('a').get('href'));
            countOfStartups = countOfStartups + 1;
        else:
            break;
            
    driver.quit();
    return Constants.startups_links;

