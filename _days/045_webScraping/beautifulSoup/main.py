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

if False:
    print(f"{soup.find_all(name='a')}")#Gets all tags

#Loop through tags
if False:
    all_tags = soup.find_all(name='a')
    #Get text of a tag
    for tag in all_tags:
        print(f"{tag.getText()}")
        
    #Or use
    for tag in all_tags:
        print(f"{tag.string}")

    #Get property of tag
    for tag in all_tags:
        print(f"{tag.get('href')}")

if False:
    heading = soup.find(name='h1',id='name')
    print(f"{heading.string}")

if False:
    #class_ is used as class is a keyword in python
    section_heading = soup.find(name='h3', class_='heading')
    print(f"{section_heading}")

#Narrowing to a specific element
if False:
    #select_one will give first item found
    company_url = soup.select_one(selector="p a")#looking for a tag in a p tag
    print(f"{company_url}")

if False:
    name = soup.select_one(selector = "#name")
    print(f"{name}")

if False:
    headings = soup.select(".heading")
    print(f"{headings}")