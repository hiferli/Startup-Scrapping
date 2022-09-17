import os
import time
from bs4 import BeautifulSoup
import requests
import urllib.request

# Directory for File Location 
import DirectoryVariable
import Constants

def SlideCapture(url):

    start_time = time.time()
    
    document = BeautifulSoup(requests.get(url).text , 'html.parser');
    startupName = ((str(document.title.string)).split(' - ')[0])

    saveLocation = DirectoryVariable.fileLocation + startupName + "/"

    if not os.path.isdir(saveLocation):
        os.makedirs(saveLocation)

    images = document.find_all(class_ = "grid-60 tablet-grid-50 mobile-grid-100 slide_image");

    index = 1;
    for image in images:
        link = image.contents[1]['src']
        
        if link != '':
            # urllib.request.urlretrieve(link, "C:/Users/ADMIN/Desktop/Startup Decks/Images/Sample_" + str(index) + ".jpg")
            slideSaveDirectory = saveLocation + "/" + startupName + "-" + str(index) + ".jpg";
            try:
                urllib.request.urlretrieve(link, slideSaveDirectory)
            except:
                pass;
                
        index += 1;

    print(f'All Slides Captured for {startupName}.')
    Constants.totalTime = Constants.totalTime + (time.time() - start_time) 
    