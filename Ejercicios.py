#Dia 3

#1 y 2Declare your age as integer variable
age = 18 
hight = 1.65
numcom = 8j
print (type(age), age)
print (type(hight), hight)
print (type(numcom), numcom)

# 3 Write a script that prompts the user to enter base and height 
# of the trianngle and calculate an area of this triangle
# (area = 0.5 x b x h). 
base = float(input ("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = print ("El area del triangulo es: ", base*altura/2)

# 4 Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#  Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = float (input("Ingresar el valor de sideA")) 
sideB = float (input("Ingresar el valor de sideB"))
sideC = float (input('Ingresar el valor de sideC'))
perimeter= print ("El valor del perimetro del triangulo es:", sideA + sideB + sideC )

# 5 Get length and width of a rectangle using prompt.
#  Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
largo = float (input("ingresa el largo del rectangulo"))
ancho = float(input("ingresa el ancho del triangulo"))
Area = print("El area del triangulo es de:", largo * ancho)
perimeter = print("El perimetro del triangulo es de:",2 * (largo + ancho))

# 6 Get radius of a circle using prompt.
#  Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = float (input("ingresa el valor del radio"))
Area = print("El area del circulo es de :", pi * r * r )
circunferencia = print("La circunferencia del circulo es de :", 2 * pi * r)
# 7 Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente1 = 2
interceptY = -2
interceptX = interceptY / pendiente1
print("la pendiente de la recta es de :", pendiente1)
print("La interseccion en el eje Y es:", interceptY)
print(" La interseccion en el eje X es:", interceptX)

# 8 Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point1 = (2, 2)
point2 = (6, 10)
X1 = point1 [0]
Y1 = point1 [1]
X2 = point2 [0]
Y2 = point1 [1]
pendiente2 =(Y2 - Y1 / X2 - X1)
Distancia = ((X2 - X1)** 2 + (Y2 - Y1))** 0.5
print ("La pendiente de los puntos es:", pendiente2)
print ("La distancia entre los puntos es:", Distancia)
 
# 9 Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente = 2
interceptY = -2
interceptX = interceptY / pendiente
print("la pendiente de la recta es de :", pendiente)
print("La interseccion en el eje Y es:", interceptY)
print(" La interseccion en el eje X es:", interceptX)

# 10 Compare the slopes in tasks 8 and 9.
print("pendientes son iguales "if pendiente2 == interceptX else "las pendientes son diferentes ")
print ("La pendiente 1 es menor que la pendiente 2")

# 11 Calculate the value of y (y = x^2 + 6x + 9).
#Try to use different x values and figure out at what x value y is going to be 0.
# Definir la función
x= int(input("Ingresar el valor de x:" ))
y= ((x**2)+(6*x)+9)
print ("El valor de y es :", " ", y)
if y==0: 
    print ("y es igual a 0.")
else: 
    print ("y no es igual a 0.")

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
longitud_python = len("python")
longitud_dragon = len("dragon")
print("longitud de python", longitud_python)
print("longitud de dragon", longitud_dragon)
#comparacion falsa
print("la longitud de pytho no es igual a la longitud de dragon", longitud_python!=longitud_dragon)

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon
print("on"in "phyton"and "on" in "dragon")

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
oracion = "I hope this course is not full in jargon" 

# 15 There is no 'on' in both dragon and python
print("on" not in "phyton" and "on" not in "dragon")
             

# 16 Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("phyton"))))



# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num =int(input("coloca un numero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")



# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
res = 7//3 == int(2.7)
print(res)



# 19 Check if type of '10' is equal to type of 10
res = type("10") == type(10)
print(res)



# 20 Check if int('9.8') is equal to 10
res = int("9.8") == 10
print(res)



# 21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
horas = float (input("Coloque horas trabajadas: "))
Tar = float (input("Ingrese la tarifa: "))
pagoTotal = horas * Tar
print ("El pago total es: ", pagoTotal)

#Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
años = int(input("Ingrese sus años vividos: "))
AñosM = 100
segXaños = 365 * 24 * 60 * 60
if años > AñosM:
    print("El maximo de años permitidos es {maxAños}. Se va a usar {maxAños} para el calculo")
    años = AñosM
seg = años * segXaños
print("En {años} años una persona puede vivir {seg} segundos.")

#Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")