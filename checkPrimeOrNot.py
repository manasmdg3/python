#import math
print("Check Whether a number is Prime or not\n******************************************************")
num = int(input("Enter any positive integer Number: "))
isPrime = True
if num == 0 or num == 1:
    print(str(num)+" is neither prime or non prime number.")
elif num == 2:
    print(str(num)+" is prime number.")
else:
    i = 2
    #while i <= math.sqrt(num):
    while i <= pow(num,0.5):
        if num % i == 0:
            isPrime = False
            break
        i += 1
    if isPrime:
        print(str(num)+" is Prime Number.")
    else:
        print(str(num)+" is non Prime Number.")
