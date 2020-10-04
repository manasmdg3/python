print("Print Fibonnaci series\n******************************************************")
end = int(input("Enter number of terms of the desired Fibonacci Series: "))
print("0 1 1", end=" ")
nTerm = 1
prevTerm = 1
count = 3
while count <= end:
    #temp = nTerm
    nTerm = nTerm + prevTerm
    prevTerm = nTerm - prevTerm
    #print(" "+str(nTerm))
    if count != end:
        print(nTerm, end=" ")
    else:
        print()
    count += 1