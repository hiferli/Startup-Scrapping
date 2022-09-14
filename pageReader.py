from bs4 import BeautifulSoup
import requests

url = r'https://startupdecks.co/bibles/zoe-financial/';

document = BeautifulSoup(requests.get(url).text , 'html.parser');

# print(document.prettify())  