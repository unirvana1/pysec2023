# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Izvēlies darbību.")
print("1.Saskaitīt")
print("2.Atņemt")
print("3.Reizināt")
print("4.Dalīt")

while True:
    # take input from the user
    choice = input("Izvēlies darbību ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ievadi pirmo skaitli: "))
            num2 = float(input("Ievadi otro skaitli: "))
        except ValueError:
            print("Šis nav skaitlis ievadi lūdzu skaitli.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Vai vēlies vēl rēķināt (jā/nē): ")
        if next_calculation == "nē":
          break
    else:
        print("Ievadi skaitli nevis kautko citu")