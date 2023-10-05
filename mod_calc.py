class Calc:
    """
    Homemade calculator
    ...
    Methods
    -------
    classic_input():
        classic step-by-step input of two numbers
        and operator between them to calculate.
        Returned number (number 1) can be calculated right away
        with new input data: new number 2 and operator,
        or just returned without further calculating
    plus(x):
        return sum of entered numbers or collection
    minus(x):
        return difference of entered numbers or collection
    mult(x):
        return product of entered numbers or collection
    divis(x):
        return quotient of entered numbers or collection
    expon(x, n):
        return power of entered number and exponent
    """
    def classic_input():
        num1 = ""
        while not num1:
            try:
                num1 = float(input("Enter your first number : "))
            except ValueError:
                print("\n\tIncorrect number! Try again\n")
        while True:
            print(
                'Summation:            "+"\n'
                'Subtraction:          "-"\n'
                'Multiplication:       "*"\n'
                'Division:             "/"\n'
                'Exponent:             "^"\n'
                '-------------------------\n'
                '\tYour expression to process now:', num1
            )
            oper = input("Choose the operation    : "
                "\nor enter 'stop' to stop calculating and taking result: ").strip().lower()
            if oper != "stop":
                try:
                    num2 = float(input("Enter your second number: "))
                except ValueError:
                    print("\n\tIncorrect number! Try again\n")
                    continue
                match oper:
                    case "+":
                        summ_num1_num2 = Calc.plus(num1, num2)
                        num1 = summ_num1_num2
                    case "-":
                        sub_num1_num2 = Calc.minus(num1, num2)
                        num1 = sub_num1_num2
                    case "*":
                        mult_num1_num2 = Calc.mult(num1, num2)
                        num1 = mult_num1_num2
                    case "/":
                        try:
                            divis_num1_num2 = Calc.divis(num1, num2)
                            num1 = divis_num1_num2
                        except ZeroDivisionError:
                            print("\n\tCouldn't be divided by 0. Correct divisor needed\n")
                    case "^":
                        expon_num1_num2 = Calc.expon(num1, num2)
                        num1 = expon_num1_num2
                    case _:
                        print(f"\n\tWrong operator selected! --> ({oper}) <-- Try again\n")
            else:
                print("\n\tLeaving calculator now. See ya again!\n")
                print("Here's your result: ", end="")
                return num1
        exit()

    def plus(*x):
        print(f"\tSum of numbers -->{x}<-- is ==>({sum(x)})<==\n")
        return sum(x)

    def minus(*x):
        x = [-x for x in x]
        x[0] = -x[0]
        print(f"\tAbsolute sum of numbers -->{x}<-- is ==>({sum(x)})<==\n")
        return sum(x)

    def mult(*x):
        num = x[0]
        i = 0
        while i < len(x) - 1:
            num *= x[i + 1]
            i += 1
        print(f"\tProduct of numbers -->{x}<-- is ==>({num})<==\n")
        return num

    def divis(*x):
        num = x[0]
        i = 0
        while i < len(x) - 1:
            num /= x[i + 1]
            i += 1
        print(f"\tQuotient of numbers -->{x}<-- is ==>({num})<==\n")
        return num

    def expon(x, n):
        print(f"\t{x} ^ {n} = {pow(x, n)}\n")
        return pow(x, n)


#import mod_calc as calc
#help(calc)
#print(calc.Calc.plus(*x))
#print(calc.Calc.minus(*x))
#print(calc.Calc.mult(*x))
#print(calc.Calc.divis(*x))
#print(calc.Calc.expon(y, n))
#print(calc.Calc.classic_input())
#x = calc.Calc.plus(1, 2, 3, 4, 5)
#x = calc.Calc.classic_input()
#print(x)
