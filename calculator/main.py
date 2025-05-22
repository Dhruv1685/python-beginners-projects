def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    if b == 0:
        return "Error : Division by zero"
    return a/b

print("==Python-Calculator==")
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multi")
print("4. Divide")
print("5. Exit")


while True:

    choice = input("\nEnter your choice(1-5) : ")

    if choice == '5':
        print("Exiting Calculator. Good Bye!")
        break

    if choice in ['1','2','3','4']:
        try:
            num1 = int(input("Enter First Number : "))
            num2 = int(input("Enter Second Number : "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
    
        if choice == '1':
            print("Result : ", add(num1,num2))
        elif choice == '2':
            print("Result : ", sub(num1,num2))
        elif choice == '3':
            print("Result : ", multi(num1,num2))
        elif choice == '4':
            print("Result : ", div(num1,num2))
    else:
        print("Invalid choice. Please try again!")