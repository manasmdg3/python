#Sum of the series: 1-2/2!+3/3!-........n/n!
#Function to find and return factorial
def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

term = int(input("Enter number of terms in the series: "))
sum = 0
while term > 0:
    if term%2 != 0:
        sum += term/factorial(term)
    else:
        sum -= term/factorial(term)
    term -= 1
print("The Sum of the series is: "+str(sum))