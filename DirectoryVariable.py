import os

fileLocation = os.path.join(os.getcwd() , r'Slides')
if not os.path.exists(fileLocation):
    os.makedirs(fileLocation)

# Make sure to add the "/" in the end as well
# fileLocation = r'C:/Users/ADMIN/Desktop/Startup Decks/Slides/'

# Not here. Thank You
# driverPath = r'C:\Users\ADMIN\Desktop\Startup Decks\Drivers\chromedriver.exe'

sleepDuration = 5;
numberOfStartups = 5;
