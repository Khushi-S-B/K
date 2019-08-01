#ERROR
import json

with open ('C:/Users/Ace/Documents/states.json') as f:
    data=json.load(f)

    for state in data['states']:
        print(state['name'])
        print(state['area_codes'])
        # mentioning only data
        # gives only key
        del state['area_codes']
with open('C:/Users/Ace/Documents/states2.json')
