print("="*35,"Simple Calculator","="*35)
while True:
    try:
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
        choice=int(input("Enter your Choice="))
        if choice>0 and choice<5:
            num1=float(input("Enter your first number="))
            num2=float(input("Enter your second number="))
            if choice==1:
                print("-"*85)
                print(f"Addition of {num1} and {num2} = {num1+num2}")
                print("-"*85)
            elif choice==2:
                print("-"*85)
                print(f"Subtraction of {num1} and {num2} = {num1-num2}")
                print("-"*85)
            elif choice==3:
                print("-"*85)
                print(f"Multiplication of {num1} and {num2} = {num1*num2}")
                print("-"*85)
            else:
                try:
                    print("-"*85)
                    print(f"Division of {num1} and {num2} = {num1/num2}")
                    print("-"*85)
                except ZeroDivisionError:
                    print("-"*85)
                    print("Number can't be divided by zero ")
                    print("-"*85)
        elif choice==5:
            print("Thank You")
            break
        else:
            print("-"*85)
            print("Please give Correct Choice Number")
            print("-"*85)
    except ValueError:
        print("-"*85)
        print("Please give only numerical value in input!")
        print("-"*85)
