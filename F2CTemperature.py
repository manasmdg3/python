def c2fConverter():
    temp = float(input("\nEnter Temperature in Celcius: "))
    print(str(temp)+" degree Celcius in Fahrenheit is: "+"{:.2f}".format((9*temp)/5+32))
def f2cConverter():
    temp = float(input("\nEnter Temperature in Fahrenheit: "))
    print(str(temp)+" degree Fahrenheit in Celcius is: "+"{:.2f}".format((temp-32)*5/9))

choice = int(input("Temperature Converter:\n1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\nEnter your choice: "))
if choice == 1:
    c2fConverter()
elif choice == 2:
    f2cConverter()
else:
    print("Wrong Choice!")