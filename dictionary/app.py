import json
from difflib import SequenceMatcher,get_close_matches

data = json.load(open('data.json'))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:       #in case user enters words like Texas or Delhi
        return data[word.title()]
    elif word.upper() in data:         #in case user enters words like USA or NATO
        return data[word.upper()]
    else:
        related_words = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
        if len(related_words) > 0:
            user_input = str(input('Did you mean \'{}\' instead? Enter \'Y\' if yes, \'N\' if no:'.format(related_words[0])))
            if user_input.upper()=='Y':
                return data[related_words[0]]
            elif user_input.upper() != 'N':
                return 'Invalid Input!'
        return 'Word not found! Please double check.'

word = input('Enter a word : ').lower()
output = translate(word)

if type(output) is list:
    for value in output:
        print(value)
else:        
    print(output)