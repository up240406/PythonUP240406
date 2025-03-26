#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
# Output:
Edad = int(input("Ingresa tu edad"))
if Edad >= 18:
    print('Eres lo suficientemente grande para conducir')
else:
    print ("no eres lo suficientemente grande para conducir")


#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)?
#  Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
#  'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 18
your_age = int(input('Dame tu edad'))
if your_age > my_age:
    diff = your_age - my_age
    print('Eres mas grande que yo por {} años'.format(diff))
    if my_age > your_age:
        diff2 = my_age - your_age
        print('Soy {} mas grande que tu'.format(diff2))
else:
    print('Tenemos la misma edad.')

#Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = input("Ingresa un numero")
b = input("Ingresa un numero")
if a < b :
    print('{} es mas pequeño que {}'.format(b,a))
elif a > b :
    print ("{} es mas grande que {}" .format(b,a))
else:
 print ("Los numeros son iguales")