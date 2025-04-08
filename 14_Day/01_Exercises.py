# 1 Explain the difference between map, filter, and reduce.
numerosS = ['1', '2', '3', '4', '5']  
numerosi= map(int, numerosS)
print(list(numerosi))   
print('El mapa aplica una función a cada elemento de una lista y devuelve una nueva lista con los resultados.') 

#filter function
numeros = [1, 2, 3, 4, 5]  
def es_numero_impar (num):
    if num % 2 != 0:
        return True
    return False

es_numero_impar = filter(es_numero_impar, numeros)
print("La lista de numeros impares es:",list(es_numero_impar))
print('El filtro aplica una función a cada elemento de una lista y devuelve una nueva lista con los elementos que cumplen la condición') 

#reduce function
from functools import reduce
producto = reduce((lambda x, y: x * y),[1,2,3,4])  
print (producto)
                  
print(' La reducción aplica una función acumulativa a los elementos de una lista y devuelve un solo valor')

#2 Explain the difference between higher order function, closure and decorator
#Higher order function
def sum_numbers(nums):  
    return sum(nums)    

def higher_order_function(f, lst):  
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)
print('Una función de orden superior es una función que toma otra función como argumento o devuelve una función como resultado.')
#closure function
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  
print(closure_result(10)) 
print('Una función de cierre es una función que recuerda el entorno en el que se creó, incluso después de que se haya ejecutado.')
#decorator function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())  
print("Un decorador es una función que toma otra función como argumento y extiende su comportamiento sin modificarla directamente.")



# 3 Define a call function before map, filter or reduce, see examples.
numbers_str = ['1', '2', '3', '4', '5']  
numbers_int = map(int, numbers_str) # Convierte cada elemento de la lista de str a un entero
print(list(numbers_int))

numbers = [1, 2, 3, 4, 5] 
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) 

from functools import reduce
producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(producto)

# 4 Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# 5 Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

# 6 Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

print("Revisado")