#Regex
#Regex, short for regular expression, is a sequence of characters that define a search pattern.
#It is a powerful tool for pattern matching and manipulating text.

#Python uses the re module for working with regular expressions
import re

#Basic Match
#The search function is used to search for a pattern within a string
if False:
    pattern = r'hello'
    text = "hello world"
    match = re.search(pattern, text)

    if match:
        print(f"Match: {match}")

#Character Classes
#These allow you to match any one of a set of characters
#They are contained within []
#Findall returns a list of non-overlapping matches in the string
if False:
    pattern = r'[aeiou]'
    text = "Hello, how are you today?"
    matches = re.findall(pattern, text)

    if matches:
        print(f"{matches}")

#Match checks for a match only at the beginning of the string
#It returns a match object if the pattern is found at the start of the string
if False:
    pattern = r'[aeiou]'
    text = "Hello, how are you today?"
    test_match = "ello, ello"

    match = re.match(pattern, test_match)
    if match:
        print(f"Match found at the beginning: {match.group()}")
    else:
        print(f"No match")

#Finditer returns an iterator yielding match objects over all non-overlapping
#matches in the string
if False:
    pattern = r'[aeiou]'
    text = "Hello, how are you today?"

    matches = re.finditer(pattern, text)
    for match in matches:
        print("Match found at index", match.start(), ":", match.group())