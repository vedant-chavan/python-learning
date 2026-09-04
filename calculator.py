def add(a,b):
    c = a+b
    return c

def subtract(a,b):
    c = a-b
    return c

def multiply(a,b):
    c = a*b
    return c

def divide(a,b):
    c = a/b
    return c

while True:
    print("========== Calculator ==========")
    try:
        a = float(input("Please Enter first Number : "))
        b = float(input("Please Enter Second Number : "))
        
        operations = int(input("""Please Select Operations From This: 
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.exit
        Enter Here : """))

        if(operations == 1):
            print(add(a,b))
        elif(operations == 2):
            print(subtract(a,b))
        elif(operations == 3):
            print(multiply(a,b))
        elif(operations == 4):
            print(divide(a,b))
        elif(operations == 5):
            print("Exit The Calculator")
            break
        else:
            print("Invalid input Select Operation Again...")

        # match operations:
        #     case 1 :
        #         print(f"Result: {add(a,b)}")
        #     case 2 :
        #         print(f"Result: {subtract(a,b)}")
        #     case 3 :
        #         print(f"Result: {multiply(a,b)}")
        #     case 4 :
        #         print(f"Result: {divide(a,b)}")
        #     case _:
        #         print("Invalid operation")

    except ValueError:
        print("Please enter valid number")
    except ZeroDivisionError:
        print("You cannot divide the no by zero!")
  

