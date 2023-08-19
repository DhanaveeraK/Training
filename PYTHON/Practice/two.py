

story = "My name is K.DHANAVEERA, and I work at HallMark in  city. Wonderland is a city known for its beautiful gardens. My favorite flower is a rose. i living in Kakinada"
person = {
    "name": "K.DHANAVEERA",
    "company": "HallMark",
    "city": "ada  ",
    "favorite": "rose"
}

entities_list = []

for key, value in person.items():
    index = 0
    while index != -1:
        index = story.lower().find(value.lower(), index)
        print(index,story[index])
        # break
        if index != -1:
            entities_list.append([index, index + len(value), value])
            index += len(value)

print(entities_list)


#Output:-[[11, 23, 'K.DHANAVEERA'], [39, 47, 'HallMark'], [51, 59, 'Kakinada'], [144, 148, 'rose']]

