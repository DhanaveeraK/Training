# # #Dictinary:-

import re

story = "My name is Dhanaveera, and I work at HallMark in Kakinada city. Kakinada is a city known for its beautiful . My favorite sweet is a Kaja, and Kaja are abundant here in Kakinada."
person = {
    "name": "Dhanaveera",
    "company": "HallMark",
    "city": "Kakinada",
    "favorite": "Kaja"
}

entities_list = []
for key, value in person.items():
    matches = re.finditer(r'\b{}\b'.format(re.escape(value)), story, re.IGNORECASE)
    for match in matches:
        entities_list.append([match.start(), match.end(), value])

print(entities_list)
#------------------------
#r'\b{}\b'.format(re.escape(value)): This regular expression pattern is constructed dynamically based on the value from the dictionary. Let's break it down:
#story: This is the input text where we want to search for matches
 #re.IGNORECASE: This flag is used to make the search case-insensitive, meaning that the pattern will match regardless of whether the characters are uppercase or lowercase.    
#re.finditer: This method returns an iterator that yields match objects for all occurrences of the pattern in the input string. It's a useful way to find all occurrences of a specific pattern within the text.