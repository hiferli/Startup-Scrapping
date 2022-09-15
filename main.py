import pageReader
import DirectoryVariable

from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = r'https://startupdecks.co/bibles/zoe-financial/';

# Selenium Work Here
driver.get(url);

# Using BeautifulSoup using Selenuim
html = driver.page_source
document = BeautifulSoup(html , "html.parser");

driver.quit();

# url_1 = r'https://startupdecks.co/bibles/zoe-financial/';
# url_2 = r'https://startupdecks.co/bibles/zestful/';

# pageReader.SlideCapture(url_1)
# pageReader.SlideCapture(url_2)