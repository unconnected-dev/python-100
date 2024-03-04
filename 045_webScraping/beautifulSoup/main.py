from bs4 import BeautifulSoup

#lxml may be needed as a parser but requires pip install
# import lxml


relative_path_name = "./045_webScraping/beautifulSoup/website.html"
with open(relative_path_name, encoding='utf-8' ) as web_file:
    web_contents = web_file.read()

soup = BeautifulSoup(web_contents, 'html.parser')

if False:
    print(f"{soup.title}")#title tag
    print(f"{soup.title.name}")#name of the title tag
    print(f"{soup.title.string}")#contents of the tag

#Show all HTML in a formatted way
if False:
    print(f"{soup.prettify()}")


if False:
    print(f"{soup.p}")#Gets the first p tag