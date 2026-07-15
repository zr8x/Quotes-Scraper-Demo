import json

content = ''
with open("quotes.json", "r") as file:
    content = file.read()

data = json.loads(content)

while True:
    print("\n\n\n\nPlease select which method you would like to use to search for quotes:\n")
    print("1. Name of author  2. Tags  3. Exit")

    method = input("Selection: ")

    if method == "1":
        authors = sorted({author for quote in data["author"]})
        name = input("\nPlease type the name of the person you would like to look up: ")
        if name in authors:
            quotes = filter(lambda arr: arr["author"] == name, data)

            for quote in quotes:
                print("\nBy " + quote["author"] + ", " + quote["text"])
        else:
            print("\nNot an author, please try again.\n")
        continue
    elif method == "2":
        tags = sorted({tag for quote in data for tag in quote["tags"]})

        print("\nHere is a list of tags, please type the tag you would like to look up:\n")

        for tag in tags:
            print(tag + " ")

        chosen = input("\nType here: ")
        
        if chosen in tags:
            quotes = filter(lambda arr: chosen in arr["tags"], data)

            for quote in quotes:
                print("\nBy " + quote["author"] + ", " + quote["text"])
        else:
            print("\nNot a tag, please try again.\n")
            
        continue
    elif method == "3":
        break
    else:
        print("Not a valid selection, try again.")
        continue
