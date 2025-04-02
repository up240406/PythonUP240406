#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma = 0
for X in range(1,101):
    nu = X
    suma = suma + nu

print('La suma es: ',suma)



#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
Evens = 0
Odds= 0
for M in range(1,101):
    if M % 2 ==0:
        Evens += M
    else:
        Odds += M
print('La suma de pares es: ',Evens)
print('La suma de impares es: ',Odds)