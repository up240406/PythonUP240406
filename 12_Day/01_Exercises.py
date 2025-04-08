#1 Writ a function which generates a six digit/character random_user_id.
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print("El random user id es :", generate_random_user_id())



#2 Modify the previous task. Declare a function named user_id_gen_by_user. 
#It doesn’t take any parameters but it takes two inputs using input(). 
#One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Agrega un numero de caracteres para el identificador de usuario:"))
    num_ids = int(input("agrega un numero de identificadores de usuario que desea generar:"))
    caracteres = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(caracteres) for _ in range(num_chars))
        user_ids.append(user_id)
    return user_ids
print("Los random user son:", user_id_gen_by_user())


#2 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
print("El rgb colors_gen es :", rgb_color_gen())

print("Revisado")