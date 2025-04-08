#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and
#  it counts number of evens and odds in the number.
def evenAndOdds(u):
    if not isinstance(u,int) or u<=0:
        return'Agrega un número entero positivo'
    evens=0
    odds=0
    for digit in str(u):
        if int(digit)%2==0:
            evens+=1
        else:
            odds+=1
    return f'Dígitos pares: {evens}, Dígitos impares: {odds}'
print(evenAndOdds(156))




#2 Call your function factorial, it takes a whole number as a parameter and
#  it return a factorial of the number
numero=int(input('Put a number: '))
def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial
print(factorial(numero))




#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
put=input('Put something: ')
def isEmpty(something):
    if put=="":
        return "Empty(you didn't put somenthing)."
    else:
        return "Not empty."
print(isEmpty(put))




#4 Write different functions which take lists. They should calculate_mean,
#  calculate_median, calculate_mode, calculate_range, calculate_variance,
#  calculate_std (standard deviation).
vals=[6,9,35,37,43,95,38,14]
def calMean(mean):
    return f'The mean value is {sum(vals)/len(vals)}'
print(calMean(vals))

def calMedian(median):
    vals.sort()
    l=len(vals)
    mitad=int(l/2)
    # Si la longitud es par,se  promediam los elementos centrales
    if l%2==0:
        mediana=(vals[mitad - 1]+vals[mitad]) / 2
    else:
        # Si no, es la que esta en el centro
        mediana = vals[mitad]
    return f'The median value is {mediana}'
print(calMedian(vals))

def calMode(moda):
        from statistics import mode
        mod=mode(vals)
        return f'The mode is {mod}'    
print(calMode(vals))

def calRange(range):
    r=max(vals)-min(vals)
    return f'The range is {r}'
print(calRange(vals))

def calVariance(var):
    from statistics import variance
    v=variance(vals)
    return f'The variance is {v}'
print(calVariance(vals))

def calStd(stt):
    from statistics import stdev
    st=stdev(vals)
    return f'The Standard deviation is {st}'
print(calStd(vals))

print("Revisado")