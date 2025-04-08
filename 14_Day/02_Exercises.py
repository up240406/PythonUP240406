#1 Use map to create a new list by changing each country to uppercase in the countries list
paises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def upper(paises):
    return paises.upper()
print ("La lista transofrmada en mayusculas queda asi:",list(map(upper, paises)))

#2 Use map to create a new list by changing each number to its square in the numbers list
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def nums_cuadrados(num):
    return num**2
print ("La lista de numeros al cuadrado queda asi:",list(map(nums_cuadrados, numeros)))

# 3 Use map to change each name to uppercase in the names list
nam = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def upper(nam):
    return nam.upper()
print ("La lista de nombres en mayusculas queda asi:",list(map(upper, nam)))

# 4 Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paises_terminacion_land(countries):
    return 'land' in countries
print ("La lista de paises que contienen 'land' queda asi:",list(filter(paises_terminacion_land, countries)))

# 5 Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paises_6_letras(countries):
    return len(countries) == 6
print ("La lista de paises con 6 letras queda asi:",list(filter(paises_6_letras, countries)))

# 6 Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paises_inician_con_E(countries):
    return countries.startswith('E')
print ("La lista de paises que inician con 'E' queda asi:",list(filter(paises_inician_con_E, countries)))

# 7 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
resultado = list(map(str.upper, filter(lambda country: len(country) != 6, countries)))
print(resultado) 

# 8 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


# 9 Use reduce to sum all the numbers in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce
def suma(x, y):
    return x + y
print ("La suma de todos los numeros es:",reduce(suma, numbers))

#10 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
resultado01 = reduce(lambda x, y: x + ', ' + y, countries) + ' son paises del norte de Europa'
print(resultado01) 
print("La concatenacion de los paises queda:", resultado01)


# 11 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorizar_paises(countries, pattern):
    return list(filter(lambda country: pattern in country, countries))
print (categorizar_paises(countries, 'land'))
 
#12 Create a function returning a dictionary, 
# where keys stand for starting letters of countries and values are the number of country names starting with that letter.'
def contar_paises_por_letra(countries):
    contador = {}
    for country in countries:
        letra = country[0].upper()
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador
print ("Conteo de los paises por letra:", contar_paises_por_letra(countries))

#13 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def obtener_primeros_diez_paises(countries):
    return countries[:10]
print ("Los primeros 10 paises son:", obtener_primeros_diez_paises(countries)) 

# 14 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def obtener_ultimos_diez_paises(countries):
    return countries[-10:]
print ("Los ultimos 10 paises son:", obtener_ultimos_diez_paises(countries))

print("Revisado")