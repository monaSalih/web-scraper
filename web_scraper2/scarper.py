import requests
from bs4 import BeautifulSoup

domain ='https://en.wikipedia.org/'
maxico_history = f'{domain}/wiki/History_of_Mexico'
# response = requests.get(maxico_history)


# print(response.text)

# html_text=response.text

# with open("mexico_cite_quere.html",'w') as file:
#     file.write(html_text)
# # print(html_text)

def get_citations_needed_count(maxico_url):
    response = requests.get(maxico_url)
    html_text=response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    result = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    return (len(result),"result for length")

def get_citations_needed_report(maxico_url):
    clean_report=[]
    response = requests.get(maxico_url)
    html_text=response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    result = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    for i in result:
        clean_report.append(i.parent.text.strip())

    return clean_report





print(get_citations_needed_count(maxico_history))
print(get_citations_needed_report(maxico_history))
# print ()
