import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name="h3", class_="title")
titles = titles[::-1]
# for title in titles:
#     print(f"{title.string}")

    
relative_path_name = "./045_webScraping/100movies/write_to/write_file.txt"
with open(relative_path_name,'w', encoding='utf-8') as write_file:
    for title in titles:
        write_file.write(f"{title.string}\n")