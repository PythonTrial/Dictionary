import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        response = input("Did you mean %s instead? Enter Y for Yes, or N for No:  " % get_close_matches(w, data.keys())[0])
        if response.upper() == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif response.upper() == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Entry not identified. Try again"
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")


print (translate(word))