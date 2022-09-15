import pageReader
import DirectoryVariable

from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = r'https://startupdecks.co/bibles/zoe-financial/';
driver.get(url);

driver.quit();

# url_1 = r'https://startupdecks.co/bibles/zoe-financial/';
# url_2 = r'https://startupdecks.co/bibles/zestful/';

# pageReader.SlideCapture(url_1)
# pageReader.SlideCapture(url_2)