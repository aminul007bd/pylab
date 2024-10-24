import csv
import json
import requests
from pprint import pprint
# names = ['John', 'Paul', 'George', 'Ringo']
# age = [20, 31, 34, 35]

# i = 0
# while i < len(names):
#     print(f'Names: {names[i]} and Age: {age[i]}')
#     i += 1
     
# for name in reversed(names):
#     print(f'{name}')

# for i in range(5):
#     print(i);

# with open("data/laureates.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)

#     laureates_beg_with_a = []

# for laureate in laureates:
#     if laureate['name'][0] == 'A':
#         laureates_beg_with_a.append(laureate)

# with open("data/laureates_beg_with_a.json", 'w') as f:
#     json.dump(laureates_beg_with_a, f, indent=2)
    
# with open("data/laureates.json", 'w') as f:
#     json.dump(laureates, f, indent=2)
# for laureate in laureates:
#     if laureate['surname'] == 'Einstein':
#         print(laureate)
#         break

response = requests.get("http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

print(last_twenty_years)