#1 Create an empty dictionary called dog
Perro = {}

#2 Add name, color, breed, legs, age to the dog dictionary
Perro = {"Frank", "Negro", "Maltes", "4 patas", "1 age"}

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
Estudiante = {'firstName': 'Erika',
           'lastName':'Diaz',
           'Gender':'Mujer',
           'Age':18,
           'maritalStatus:':'Soltera',
           'Skills':['Dibujar'],
           'Country:':'Maxico',
           'City':'Aguascalientes',
           'Adress':'potreros'}

#4 Get the length of the student dictionary
print('La longitud del Diccionario es:', len(Estudiante))

#5 Get the value of skills and check the data type, it should be a list
print('Los valores de las HABILIDADES son:', Estudiante['Skills'])

#6 Modify the skills values by adding one or two skills
Estudiante['Habilidades'] = 'Dibujar'',''Matematicas','Pintar'
print(Estudiante)

#7 Get the dictionary keys as a list
claves = (Estudiante.keys())
print('Las claves son:', claves)

#8 Get the dictionary values as a list
values = (Estudiante.values())
print('Los valores son:', values)

#9 Change the dictionary to a list of tuples using items() method
print(Estudiante.items())

#10 Delete one of the items in the dictionary
del(Estudiante['Age'])
print(Estudiante)

#11 Delete one of the dictionaries
del(Estudiante)
