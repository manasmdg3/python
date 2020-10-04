print("Check Whether a number is Armstrong number or not\n******************************************************")
num = input("Enter any positive integer Number: ")
n = len(num)-1
sum = 0
while n >= 0 :
    sum = sum + pow(int(num[n]),len(num))
    n -= 1
if sum == int(num):
    print(num + " is an Armstrong Number.")
else:
    print(num + " is not an Armstrong Number.")