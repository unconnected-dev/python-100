from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, 'html.parser') 


article_scores = soup.find_all(name='span', class_='score')
articles = soup.select(selector=".athing .title .titleline a")

# article_tags = soup.select(selector=".athing .title .titleline a")
# article_links = soup.select(selector=".athing .title .titleline a")
# article_scores = soup.select(selector="span .score")

smallest = min(len(articles), len(article_scores))
article_scores = [int(n.string.split()[0]) for n in article_scores]

if False:
    for i in range(smallest):
        print(f"{article_scores[i], articles[i].string}, {articles[i].get('href')}")

#Find highest scored
if True:
    i = article_scores.index(max(article_scores))
    print(f"{article_scores[i], articles[i].string}, {articles[i].get('href')}")