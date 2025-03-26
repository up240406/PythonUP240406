#1 Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

calificacion= float(input('tu calificacion es: '))
if calificacion>=80 and calificacion<=100:
    print('A')
elif calificacion>=70 and calificacion<=89:
    print('B')
elif calificacion>=60 and calificacion<=69:
    print('C')
elif calificacion>=50 and calificacion<=59:
    print('D')
elif calificacion>=0 and calificacion<=49:
    print('F')

#2 Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. 
#December, January or February, the season is Winter. 
#March, April or May, the season is Spring June, July or August, the season is Summer
mes = input('Dime un mes del año: ')
yesSeas = mes.capitalize()
autumn = ('September','Octover','November')
winter = ('December','January','February')
spring = ('March','April','May')
summer = ('June','July','August')
if yesSeas in autumn:
    print('The season is Autumn.')
elif yesSeas in winter:
    print('The season is Winter.')
elif yesSeas in spring:
    print('The season is Spring.')
elif yesSeas in summer:
    print('The season is Summer.')

#3 The following list contains some fruits:
frutas = ["'banana', 'orange', 'mango', 'lemon"]
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
nuevaFruta = input("Agrega otra fruta")
if nuevaFruta not in frutas:
    frutas.append(nuevaFruta)
    print(frutas)
else:
    print("La nueva fruta ya existe")
