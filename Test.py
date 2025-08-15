from Test_02 import fun
def addition(a, b):
    return a+b
def substraction(a , b):
    return a-b

def multiplication (a, b):
    return a*b
def division(a,b):
    if b==0:
        return "Devision can not be performed by zero"
    else:
        return a/b

def main():
    a = 5
    b = 3
    print(f"Addition of the two numbers is: {addition(a,b)}")
    print(f"Substraction of the two numbers is: {substraction(a,b)}")
    print(f"Multiplication of the two numbers is :{multiplication(a,b)}")
    print(f"Division of the two numbers is: {division(a,b)}")
    print(f"function from Test_02.py: {fun(a,b )}")



if __name__ == "__main__":
    main()