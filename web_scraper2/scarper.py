import requests
from bs4 import BeautifulSoup

domain ='https://en.wikipedia.org/'
maxico_history = f'{domain}/wiki/History_of_Mexico'
response = requests.get(maxico_history)


print(response.text)

html_text=response.text

with open("mexico_cite_quere.html",'w') as file:
    file.write(html_text)
print(html_text)

soup = BeautifulSoup(html_text, 'html.parser')
result = soup.find('div', id='results_inner_card')
jobs = result.find_all('li', class_='has-pointer-d')

def get_citations_needed_count(citations_contant):
    title=citations_contant.find()