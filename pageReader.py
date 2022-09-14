import os
from bs4 import BeautifulSoup
import requests
import urllib.request

url = r'https://startupdecks.co/bibles/zoe-financial/';
# url = r'https://startupdecks.co/bibles/zestful/';

document = BeautifulSoup(requests.get(url).text , 'html.parser');
startupName = ((str(document.title.string)).split(' - ')[0])

fileLocation = r'C:/Users/ADMIN/Desktop/Startup Decks/' + startupName + "/"

if not os.path.isdir(fileLocation):
   os.makedirs(fileLocation)

images = document.find_all(class_ = "grid-60 tablet-grid-50 mobile-grid-100 slide_image");

index = 1;
for image in images:
    link = image.contents[1]['src']
    # urllib.request.urlretrieve(link, "C:/Users/ADMIN/Desktop/Startup Decks/Images/Sample_" + str(index) + ".jpg")
    slideSaveDirectory = fileLocation + "/" + startupName + "-" + str(index) + ".jpg";
    urllib.request.urlretrieve(link, slideSaveDirectory)

    index += 1;