def basic_calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None
    
def main():
    print(basic_calculator(23, '*', 4))

if __name__ == "__main__":
    main()