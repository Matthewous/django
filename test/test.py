import csv

print('проверка')

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))

    for phone in phones:
        print(phone['name'])

        
