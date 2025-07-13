def star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i - 1):
            print(j, end="")
        print()

def reverse_star_pattern(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows-i) + "* " * i)

def alphabet_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(65, 65 + i):
            print(chr(j), end="")
        print()

def right_number_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + str(i) * i)

def menu():
    print("\n📌 Choose Pattern Type:")
    print("1. Increasing Star Pattern")
    print("2. Increasing Number Pattern")
    print("3. Reverse Star Pattern")
    print("4. Pyramid Star Pattern")
    print("5. Alphabet Pattern")
    print("6. Right-Aligned Number Triangle")
    print("0. Exit")

while True:
    menu()
    choice = int(input("👉 Enter your choice (0 to exit): "))
    
    if choice == 0:
        print("🔚 Exiting Pattern Printer. Goodbye!")
        break

    rows = int(input("🔢 Enter number of rows: "))
    
    print("\n🖨️ Generated Pattern:\n")

    if choice == 1:
        star_pattern(rows)
    elif choice == 2:
        number_pattern(rows)
    elif choice == 3:
        reverse_star_pattern(rows)
    elif choice == 4:
        pyramid_pattern(rows)
    elif choice == 5:
        alphabet_pattern(rows)
    elif choice == 6:
        right_number_triangle(rows)
    else:
        print("❌ Invalid choice. Please select a valid option.")