import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def introduction():
    y = input("Can you write again? For me that word doesn't exist: ")
    return data[y]
 

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        x = input("Did you mean %s instead? If yes write Y, else write N: " % get_close_matches(w,data.keys())[0])

        if x == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif x == "N":
            z = introduction()
            print(z)
        else:
            return "we didn't understand your entry"
    else:
        z = introduction()
        print(z)


word = input("enter the word: ")

translate(word)

output = translate(word)

for item in output:
    print(item)