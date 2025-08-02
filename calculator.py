# print("=============AI CALCULATOR================")
# def add():
#     num_a = float(input("Enter the first number: "))
#     num_b = float(input("Enter the second number: "))
#     result = num_a + num_b
#     print(result)

# def sub():
#     num_a = float(input("Enter the first number: "))
#     num_b = float(input("Enter the second number: "))
#     result = num_a - num_b
#     print(result)

# def mult():
#     num_a = float(input("Enter the first number: "))
#     num_b = float(input("Enter the second number: "))
#     result = num_a * num_b
#     print(result)

# def div():
#     num_a = float(input("Enter the first number: "))
#     num_b = float(input("Enter the second number: "))
#     try: num_a/num_b
#     except ZeroDivisionError:
#         return "CAN'T DIVIDE BY ZERO.......IDIOT!"
#     result = num_a / num_b
#     print(result)

# def pow():
#     num_a = float(input("Enter the first number: "))
#     num_b = float(input("Enter the second number: "))
#     result = num_a ** num_b
#     print(result)


# input_operator = input("Enter the operator (+, -, *, /, **): ")
# if input_operator == "+":
#     add()
# elif input_operator == "-":
#     sub()
# elif input_operator == "*":
#     mult()
# elif input_operator == "/":
#     div()
# elif input_operator == "**":
#     pow()
# else:
#     print("PLEASE ENTER A VALID OPERATOR (+, -, *, /, **)")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "CAN'T DIVIDE BY ZERO.......IDIOT!"
    
def pow(a,b):
    return a ** b

def menu():
    choice = int(input("Enter 1 for Addition \n 2 for Subtraction \n 3 for Multiplication \n 4 for Division \n 5 for Power: "))
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if choice ==1:
        print(add(a,b))
    elif choice ==2:
        print(sub(a,b))
    elif choice ==3:
        print(mul(a,b))
    elif choice ==4:
        print(div(a,b))
    elif choice ==5:
        print(pow(a,b))

menu()