def add(x,y):
    result = x + y
    return result

def subtract(a,b):
    result = a-b
    return result

def divide(c,d):
    result = c / d
    return result  

def multiply(e,f):
     result = e * f
     return result 

def remainder(g,h):
     result = g % h
     return result  

def power_of(j,k):
    result = j ** k
    return result   

def sum(*numbers):
    total = 0
    for number in numbers:
        total +=number
    return total

def multiply_many(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def is_prime_while_loop(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
# Test the function
num = 37
if is_prime_while_loop(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")    

  