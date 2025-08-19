print()
print("Welcom to calculator...")
print()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def power(a,b):
    return a**b

def rem(a,b):
    return a%b

print("1. Addition.")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Modulus")

while True:
    choice = input("Enter the Operation(1/2/3/4/5/6): ")
    
    if choice in ('1','2','3','4','5','6'):
        a,b = map(float,input("Enter the numbers: ").split())
        if choice == '1':
            print(f"{a} + {b} = {add(a,b)}")
        elif choice == '2':
            print(f"{a} - {b} = {sub(a,b)}")
        elif choice == '3':
            print(f"{a} * {b} = {multi(a,b)}")
        elif choice == '4':
            print(f"{a} / {b} = {div(a,b)}")
        elif choice == '5':
            print(f"{a} ^ {b} = {power(a,b)}")
        elif choice == '6':
            print(f"{a} % {b} = {rem(a,b)}")
        
        next = input("Want more caculation (Yes/No): ").lower()
        if next == 'no':
            print("Thank you for Visiting.")
            break
    else:
        print("Invalid Choice, Try Again..")
