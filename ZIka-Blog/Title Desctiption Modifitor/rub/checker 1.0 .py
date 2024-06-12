import requests
from bs4 import BeautifulSoup

def get_title_and_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    description = soup.find('meta', attrs={'name': 'description'})
    description_content = description['content'] if description else 'No description found'
    return title, description_content

url = 'https://woy.ai/pt/p/Deepshot-2-0'
title, description = get_title_and_description(url)
print(f'Title: {title}')
print(f'Description: {description}')
