#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
variable1 = "thirty "
variable2 = "days " 
variable3 = 'of '
variable4 = 'phyton'
print (variable1 + variable2 + variable3 + variable4)


#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1 = 'Coding '
string2 = 'for '
string3 = 'all'
print (string1 + string2 + string3)


#3 Declare a variable named company and assign it to an initial value "Coding For All".
empresa = "Coding for all"
print (empresa)


#4 Print the variable company using print().
print (empresa)


#5 Print the length of the company string using len() method and print().
print (len(empresa))

#6 Change all the characters to uppercase letters using upper() method.
print (empresa .upper())

#7 Change all the characters to lowercase letters using lower() method.
print (empresa .lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print (empresa .capitalize())
print (empresa .title())
print (empresa .swapcase())

#9 Cut(slice) out the first word of Coding For All string.
print (empresa [6:14])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(empresa.index('Coding'))
print('Coding ' in empresa)

#11 Replace the word coding in the string 'Coding For All' to Python.
print(empresa.replace('Coding','Phyton'))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
comp = "Python para todos"
print(comp.replace('Phyton','Todos'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print (empresa .split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
aplicacion = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(aplicacion.split(','))
