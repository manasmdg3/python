print("Enter Marks of 3 Subjects:")
marks = []
for i in range(0,3):
    marks.insert(i,int(input("Enter Mark of the Subject "+str(i+1)+": ")))

while True:
    option = input('''Choose a option from below:
    1. View total Marks
    2. View percentage
    3. View Grade
    4. Exit
    ''')
    if option == '1':
        print("Your total mark is: "+str(sum(marks)))
    elif option == '2':
        print("Your percentage is: "+str(sum(marks)/3))
    elif option == '3':
        if(sum(marks)/3) >= 80:
            print("Your Grade is: A")
        elif(sum(marks)/3) >= 70:
            print("Your Grade is: B")
        elif(sum(marks)/3) >= 60:
            print("Your Grade is: C")
        elif(sum(marks)/3) >= 40:
            print("Your Grade is: D")
        else:
            print("Your Grade is: E")
    elif option =='4':
        exit()
    else:
        print("Invalid choice")

