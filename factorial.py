print("Factorial Calculation with While Loop")
print("*****************************************************")
n = int(input("Enter Number: "))
m = n
c = 1
while n > 1:
    c = c*n
    n-=1
print("Factorial of "+str(m)+" is: "+str(c))