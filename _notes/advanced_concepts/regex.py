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


#Quantifiers
#These specify the number of occurences of a character or group in a pattern
# * matches zero or more occurrences
# + matches one or more occurrences
# ? matches zero or one occurrence
# {} allows you to specify exact occurrences or a range
if False:
    pattern = r'a*'
    text = "aaaabbb"
    matches = re.findall(pattern, text)
    print("Matches found:", matches)  #Output: ['aaaa', '', '', '', '', '']

if False:
    pattern = r'a*'
    text = "aaaabbbab"
    matches = re.findall(pattern, text)
    print(f":Matches found: {matches}") #Output: ['aaaa', '', '', '', 'a', '', '']


#Anchors
#These are special characters in regular expressions that allow you to specify
#the position in the text where the pattern should match
# ^ (caret) anchor matches the start of the string
# Example: ^hello matches "hello" only if it appears at the beginning of a string
if False:
    pattern = r'^hello'
    text = "hello world"
    match = re.search(pattern, text)
    if match:
        print("Pattern found at the beginning of the string!")

# $ (dollar) anchor matches the end of the string
# Example: world$ matches "world" only if it appears at the end of a string
if False:
    pattern = r'world$'
    text = "hello world"
    match = re.search(pattern, text)
    if match:
        print("Pattern found at the end of the string!")

# \b (word boundary) anchor matches a word boundary
# It matches a position where a word character (letter, digit, underscore, etc)
# is not followed or preceeded by another word character
# Example:  \bword\b matches "word" only if it appears as a whole word in the string
if False:
    pattern = r'\bworld\b'
    text = "hello world"
    match = re.search(pattern, text)
    if match:
        print("Pattern found as a whole word!")

# \B (non-word boundary) anchor matches a position where a word character is followed
# or preceeded by a word character. It is the opposite of \b
# Example: \Bword\B matches "word" only if it appears as part of another word in the string 
if False:
    pattern = r'\Bworld\B'
    text = "hello-world"
    match = re.search(pattern, text)
    if match:
        print("Pattern found as part of another word!")


#Escaping Special Characters
#These have special meanings and are used to define the pattern to match
#To match a special character literally, you need to escape it by preceeding it with a \
#Escaping a special character tells the regular expression engine to treat it as a normal
#character rather than interpreting its special meaning
#For example a literal dot . would be \.
        
#In python it is recommended to use raw strings r'...' to avoid double escaping
#Raw strings treat backslashes as literal characters and prevent python from interpreting
#them as escape sequences
#Example: r'\.' is '\\.' but using raw strings is cleaner and less error prone

#List of escaping special characters
# . (Dot): Matches any single character except newline
# ^ (Caret): Matches the start of the string
# $ (Dollar): Matches the end of the string
# * (Asterisk): Matches zero or more occurrences of the preceding character or group
# + (Plus): Matches one or more occurrences of the preceding character or group
# ? (Question Mark): Matches zero or one occurrence of the preceding character or group
# { (Left Curly Brace): Marks the start of a quantifier or specifies a range
# } (Right Curly Brace): Marks the end of a quantifier or specifies a range
# [ (Left Square Bracket): Marks the start of a character class
# ] (Right Square Bracket): Marks the end of a character class
# \ (Backslash): Escapes a special character, or indicates a special sequence (e.g., \d for digit)
# | (Vertical Bar): Acts as an OR operator, matching either the expression before or after it
# ( (Left Parenthesis): Marks the start of a capturing group
# ) (Right Parenthesis): Marks the end of a capturing group