print("Factorial Calculation in FOR Loop")
print("*****************************************************")
n = int(input("Enter Number: "))
m = n
c = 1
for x in range(1,n+1):
    c = c*x
print("Factorial of "+str(m)+" is: "+str(c))