from bs4 import BeautifulSoup
import requests
import urllib.request

url = r'https://startupdecks.co/bibles/zoe-financial/';

document = BeautifulSoup(requests.get(url).text , 'html.parser');


images = document.find_all(class_ = "grid-60 tablet-grid-50 mobile-grid-100 slide_image");

index = 1;
for image in images:
    link = image.contents[1]['src']
    urllib.request.urlretrieve(link, "C:/Users/ADMIN/Desktop/Startup Decks/Images/Sample_" + str(index) + ".jpg")
    index += 1;