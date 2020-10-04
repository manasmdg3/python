print("Print all the prime numbers in an interval\n******************************************************")
start = int(input("Enter the interval:\nStarting number(Positive Integer): "))
end = int(input("Ending Number(Positive Integer): "))+1
for num in range(start,end):
    isPrime = True
    if num == 1 or num == 0:
        continue
    elif num == 2:
        print(str(num)+" is prime number.")
    else:
        i = 2
        #while i <= math.sqrt(num):
        while i <= pow(num,0.5):
            if num % i == 0:
                #print(str(num)+ "in If in While")
                isPrime = False
            i += 1
        if isPrime:
            print(str(num)+" is Prime Number.")