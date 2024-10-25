# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu

import json

kategories = None
inputSet = None
with open('..\\dane\\kategorie.json', encoding='utf-8') as file:
    kategories = json.load(file)

sortedKategories = sorted(kategories, key=lambda x: -x["Wartość za uncję (USD)"])[0:5]

with open('..\\dane\\zbiór_wejściowy.json', encoding='utf-8') as file:
    inputSet = json.load(file)

header = f"{'Typ':<15}{'Czystość':<15}{'Wartość za uncję (USD)':<25}{'Masa':<15}{'Barwa':<15}{'Pochodzenie':<15}{'Właściciel':<25}"
print(header)
print(len(header) * '-')
for rKat in sortedKategories:
    first = True
    for rInput in inputSet:
        if rKat['Typ'] == rInput['Typ'] and rKat['Czystość'] == rInput['Czystość']:
            if first == True:
                print(f"{rKat['Typ']:<15}{rKat['Czystość']:<15}{rKat['Wartość za uncję (USD)']:<25}{rInput['Masa']:<15}{rInput['Barwa']:<15}{rInput['Pochodzenie']:<15}{rInput['Właściciel']:<15}")
                first = False
            else:
                print(f"{'':<55}{rInput['Masa']:<15}{rInput['Barwa']:<15}{rInput['Pochodzenie']:<15}{rInput['Właściciel']:<15}")