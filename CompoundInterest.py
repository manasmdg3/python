print("Compound Interest Calculation/n***********************************");
p = int(input("Enter Principle Value: "))
r =  float(input("Enter rate of Interest: "))
t = int(input("Enter the Term: "))
print("The Compound Interest for the Sum "+str(p)+" for "+str(t)+" years with rate of interest "+str(r)+" is: "+str(((p*pow(1+(r/100),t)))-p))