#1 Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count= count + 1

numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(numbers)

#2 Iterate 10 to 0 using for loop, do the same using while loop.
numberS = [10,9,8,7,6,5,4,3,2,1,0]
for numberS in numbers:
    print(numberS)


#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
t = 8
for i in range(t):
    for j in range(i):
        print('#', end = '')
    print()

#4 Use nested loops to create the following:
r = 8
for n in range(r):
    print('# '* r)
    
#5 Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
o = 0
for o in range (11):
    print(o, 'x', o, '=', o * o)

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
p = 0
if p % 2 == 0:
    for p in range(101):
        print(p)

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range (0, 100, 2):
    print(odd)
