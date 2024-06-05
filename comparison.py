from bs4 import BeautifulSoup
import requests

title = ''
titles = []
site_url = ''
site_urls = []



def start():
    site_url = input("Site URL:")
    if 'https://anilist.co/' in site_url:
        site_urls.append(site_url)
        start()
    elif site_url == 'done':
        print("anime")
    else:
        print("retry")
        start()


html_text = requests.get("https://anilist.co/anime/1689/5-Centimeters-per-Second/").text
soup = BeautifulSoup(html_text, 'lxml')
title = soup.find('h1', class_='').text
titles.append(title)
print(title)

