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

    startup_slides_link = []

    try:
        document = BeautifulSoup(requests.get(url).text , 'html.parser');
        # Can use the line below as well... However it may cause security breach
        # document = BeautifulSoup(requests.get(url , verify=False).text , 'html.parser');
    except:
        print("Internal Server Issues. Please try after some time")

    images = document.find_all(class_ = "grid-60 tablet-grid-50 mobile-grid-100 slide_image");
    for image in images:
        link = image.contents[1]['src']
        if link != '':
            startup_slides_link.append(link);
    
    startupName = ((str(document.title.string)).split(' - ')[0])
    if(len(startup_slides_link) == 0):
        print(f"No slides found for {startupName}. Heading towards the next startup...")
        return

    # saveLocation = DirectoryVariable.saveLocation + startupName + "/"
    saveLocation = os.path.join(DirectoryVariable.fileLocation , startupName)
    if not os.path.exists(saveLocation):
        os.makedirs(saveLocation)

    if not os.path.isdir(saveLocation):
        os.makedirs(saveLocation)

    index = 1;
    for link in startup_slides_link:
        # urllib.request.urlretrieve(link, "C:/Users/ADMIN/Desktop/Startup Decks/Images/Sample_" + str(index) + ".jpg")
        slideSaveDirectory = saveLocation + "/" + startupName + "-" + str(index) + ".jpg";
        try:
            urllib.request.urlretrieve(link, slideSaveDirectory)
        except:
            pass;
                
        index += 1;


    print(f'All Slides Captured for {startupName}.')
    Constants.totalTime = Constants.totalTime + (time.time() - start_time) 
    
