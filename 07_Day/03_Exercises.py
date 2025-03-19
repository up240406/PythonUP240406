#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
setAge = set(age)
print(len(age))
print(len(setAge))
if len(age) > len(setAge):
    print("La lista mayor es: ", age)
if len(age) < len(setAge):
    print("El set mayor es: ", setAge)

#Explain the difference between the following data types: string, list, tuple and set
print("Un String es una cadena de caracteres")
print("Una lista es una estructura de datos que almacena elementos de manera ordnada")
print("Un tuple es lo mismo que une lista pero no se puede modificar")
print("Un set es una colección de elementos que; no se repiten y no tienen un orden y los sets"" " 
"son inmutables")

#I am a teacher and I love to inspire and teach people. 

# How many unique words have been used in the sentence? 

# Use the split methods and set to get the unique words.
word = "I am a teacher and I love to inspire and teach people"
totalWords = word.split()
print("Las palabras unicas son: ", len(totalWords))
print("Las palabras unicas son; ", totalWords)