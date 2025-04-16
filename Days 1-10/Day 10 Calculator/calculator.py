def print_banner():
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
          """)
    
def number_select(first:bool = False) -> float:
    try:
        if first:
            return float(input("What's the first number?: "))
        else:
            return float(input("What's the second number?: "))
    except:
        print('An error occured, please try again.')
        return number_select(first=first)
    
def operation_select():
    operation = None
    valid_operations = ['+', '-', '*', '/']

    while operation is None:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        if operation not in valid_operations:
            print(f"{operation} is not a valid operation please try again.")
            operation = None

    return operation

def add(num1, num2):
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
    return answer

def minus(num1, num2):
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")
    return answer

def divide(num1, num2):
    answer = num1 + num2
    print(f"{num1} / {num2} = {answer}")
    return answer

def main():
    print_banner()
    num1 = number_select(True)
    cont_calc = True
    while cont_calc:
        operator = operation_select()
        num2 = number_select(False)
        if operator == "+":
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = minus(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)
        else:
            num1 = divide(num1, num2)
        cont = input(f"Type 'y' to continue calculation with {num1}, type 'n' to start a new calculation, or type anything else to exit: ").lower()
        if cont == 'y':
            cont_calc = True
        elif cont == 'n':
            return main()
        else:
            cont_calc = False

    print("Thank you for using the calculator, good bye.")

main()