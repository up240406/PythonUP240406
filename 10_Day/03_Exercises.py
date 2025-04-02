#1 Go to the data folder and use the countries.py file. Loop through the countries 
# and extract all the countries containing the word land.
import COUNTRIES as p
COUNTRIES = p.countries
for pais in COUNTRIES:
    if 'land' in pais:
        print("Paises que llevan 'land' en su nombre :"), pais

#2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for F in reversed(fruits):
    print(F)


#3 Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world

import COUNTRIES as lol
paises = lol.paiSES
idioms = list()
repTdioma=0
for pais in paises:
    for idioma in pais["languages"]:
        if idioma not in idioms:
            idioms.append(idioma)
        else:
            repTdioma+=1

print('El total de idiomas es: ',len(idioms))
print('La repetición de idiomas es de: ',repTdioma)

dcIdm={}
for idioma in idioms:
    dcIdm[idioma]=0

for idioma in dcIdm:
    for pais in paises:
        if idioma in pais["languages"]:
            dcIdm[idioma]+=pais["population"]

menorMayor=sorted(dcIdm.values(),reverse=True)
the10=menorMayor[0:10]

for valor in the10:
    for idioma in dcIdm:
        if valor==dcIdm[idioma]:
            print(idioma,valor)