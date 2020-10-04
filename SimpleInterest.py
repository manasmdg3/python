print("Simple Interest Calculation/n***********************************");
p = int(input("Enter Principle Value: "))
r =  float(input("Enter rate of Interest: "))
t = int(input("Enter the Term: "))
with open("Interest_Log.txt", 'a') as file:
    file.write("\nThe Simple Interest for the Sum "+str(p)+" for "+str(t)+" years with rate of interest "+str(r)+" is: "+str((p*r*t/100)))
print("The Simple Interest for the Sum "+str(p)+" for "+str(t)+" years with rate of interest "+str(r)+" is: "+str((p*r*t/100)))