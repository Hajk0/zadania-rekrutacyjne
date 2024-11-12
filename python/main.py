# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu

import json
import re

def ctToOunce(ct: float) -> float:
    return 0.00705479239 * ct

def gToOunce(g: float) -> float:
    return 0.352739619 * g

def getMass(massString: str) -> float:
    r = re.search(r'\d+[,\.]?\d*', massString)
    if r:
        strFloat = r.group().replace(',', '.')
        return float(strFloat)
    return None

def calculateValue(row, converter):
    mass = getMass(row['Masa'])
    totalValue = converter(mass) * row['Wartość za uncję (USD)']
    return totalValue

def combineRow(rKat, rInput):
    row = rInput.copy()
    row['Wartość za uncję (USD)'] = int(rKat['Wartość za uncję (USD)'])
    if row['Masa'][-1] == 'g':
        row['Wartość'] = calculateValue(row, gToOunce)
    else:
        row['Wartość'] = calculateValue(row, ctToOunce)
    return row

kategories = None
inputSet = None
with open('..\\dane\\kategorie.json', encoding='utf-8') as file:
    kategories = json.load(file)

sortedKategories = sorted(kategories, key=lambda x: -x["Wartość za uncję (USD)"])[0:5]

with open('..\\dane\\zbiór_wejściowy.json', encoding='utf-8') as file:
    inputSet = json.load(file)



combinedSet = []
for rKat in kategories:
    for rInput in inputSet:
        if rKat['Typ'] == rInput['Typ'] and rKat['Czystość'] == rInput['Czystość']:
            row = combineRow(rKat, rInput)
            combinedSet.append(row)

sortedSet = sorted(combinedSet, key=lambda x: -x['Wartość'])
header = f"{'Typ':<15}{'Czystość':<15}{'Wartość za uncję (USD)':<25}{'Masa':<15}{'Barwa':<15}{'Pochodzenie':<15}{'Właściciel':<50}{'Wartość':<10}"
print(header)
print(len(header) * '-')
for row in sortedSet[:5]:
    print(f"{row['Typ']:<15}{row['Czystość']:<15}{row['Wartość za uncję (USD)']:<25}{row['Masa']:<15}{row['Barwa']:<15}{row['Pochodzenie']:<15}{row['Właściciel']:<50}{row['Wartość']:<10.2f}")
