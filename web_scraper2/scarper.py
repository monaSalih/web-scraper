import requests
from bs4 import BeautifulSoup

domain ='https://en.wikipedia.org/'
maxico_history = f'{domain}/wiki/History_of_Mexico'
response = requests.get(maxico_history)
 
print(response.text)