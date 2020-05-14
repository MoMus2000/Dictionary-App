import json
from difflib import get_close_matches
bool = True
data = json.load(open("/Users/a./Desktop/Dictionary/076 data.json"))


def Meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word,data.keys(),3,0.8):
        meant = get_close_matches(word,data.keys(),3,0.8)[0]
        print(" Did you mean " + meant)
        answer = input("Answer Y/N :")
        if answer == "Y" or "y":
            return data[meant]
        else:
            return "This word does not exist in our database"
    else:
        return "This Word doesnot exist in this dictionary"

user = input("Please enter your word :")
output =  Meaning(user)
if type(output) == list:
    for item in output:
        print(" "+ item.upper())
else:
    print(output)
