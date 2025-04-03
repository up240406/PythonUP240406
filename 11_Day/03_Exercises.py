#1 Write a function called is_prime, which checks if a number is prime.
def isPrime(p):
    if p<2:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
pop = int(input('Give a number: '))
if isPrime(pop):
    print(f'{pop} es un número primo.')
else:
    print(f'{pop} no es un número primo')



#2 Write a functions which checks if all items are unique in the list.
def uniqueData(lista):
    return len(lista)==len(set(lista))
print(uniqueData([1,2,3,5,6,4,2,2]))
print(uniqueData([1,5,4,2,]))



#3 Write a function which checks if all the items of the list are of the same data type.
def sameType(lista):
    return all(isinstance(i, type(lista[0])) for i in lista)
print(sameType([1,8,9]))
print(sameType([1,'nein',78]))



#4 Write a function which check if provided variable is a valid python variable
import keyword
def validVar(nombre):
    return nombre.isidentifier() and not keyword.iskeyword(nombre)
print(validVar('mi_variable'))
print(validVar('2var'))
print(validVar('for'))



#5 Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
import COUNTRIES as lol
def mostSpokenLanguages():
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
