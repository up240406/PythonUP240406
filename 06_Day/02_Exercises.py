#1 Unpack siblings and parents from family_members
Family_members = ("Paola", "Arturo", "Max", "Manel", "Paula", "Alonso")
ParentsFamily_members = Family_members[4:6]
print("Los padres son:",ParentsFamily_members)
Family_members= ("Paula","Alonso","Paola", "Arturo", "Max", "Manuel")
SiblingsFamily_members = Family_members[2:6]
print("Los hermanos son:", SiblingsFamily_members)

#2 Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
fruits =("guayaba", "platano", "fresa", "manzana")
vegetables = ("Tomate", "apio", "berenjena")
animals = ("leche", "huevos")
foodStuffTp = animals + fruits + vegetables
print(foodStuffTp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
foodStuffLt = list(foodStuffTp)
print(foodStuffLt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = foodStuffTp[5]
print(middle)

#5 Slice out the first three items and the last three items from food_staff_lt list
firstThree = foodStuffTp[0:3]
lastThree = foodStuffTp[-3:-1]
print(firstThree)
print(lastThree)

#6 Delete the food_staff_tp tuple completely
del foodStuffTp

#7 Check if an item exists in tuple:
if "fresa" in foodStuffLt:
    print("si, fresa esta en la lista de frutas")

# Check if 'Estonia' is a nordic country
nordicCountries = ("Denmark", "Finland", "Iceland")
if "Iceland" in nordicCountries:
    print("Iceland es un pais nordico")
#9 Check if 'Iceland' is a nordic country
if "Estonia" in nordicCountries:

    print("Estonia es un pais nordico")
else:
    print("Estonia no es un pais nordico")