from bs4 import BeautifulSoup
import requests

url = r'https://startupdecks.co/bibles/zoe-financial/';

document = BeautifulSoup(requests.get(url).text , 'html.parser');


images = document.find_all(class_ = "grid-60 tablet-grid-50 mobile-grid-100 slide_image");

for image in images:
    link = image.contents[1]['src']
    
# print(document.prettify())  