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
        with new input data: number 2 and operator
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
                'Exponentiation:       "^"\n'
                '-------------------------\n'
                '\tYour expression to process now:', num1
            )
            oper = input("Choose the operation    : "
                "\nor enter 'stop' to stop calculating and take result: ").strip().lower()
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
                        print(f"\n\t{float(num1)} + {float(num2)} = {num1}\n")
                    case "-":
                        sub_num1_num2 = Calc.minus(num1, num2)
                        num1 = sub_num1_num2
                        print(f"\n\t{float(num1)} - {float(num2)} = {num1}\n")
                    case "*":
                        mult_num1_num2 = Calc.mult(num1, num2)
                        num1 = mult_num1_num2
                        print(f"\n\t{float(num1)} * {float(num2)} = {num1}\n")
                    case "/":
                        divis_num1_num2 = Calc.divis(num1, num2)
                        num1 = divis_num1_num2
                        try:
                            print(f"\n\t{float(num1)} / {float(num2)} = {num1}\n")
                        except ZeroDivisionError:
                            print("\n\tCouldn't be divided by 0! Enter a correct number\n")
                    case "^":
                        expon_num1_num2 = Calc.expon(num1, num2)
                        num1 = expon_num1_num2
                        print(f"\n\t{float(num1)} ^ {float(num2)} = {num1}\n")
                    case _:
                        print(f"\n\tWrong operator selected! --> ({oper}) <-- Try again\n")
            else:
                print("\n\tLeaving calculator now. See ya again!\n")
                print("Here's your result: ", end="")
                return num1
        exit()

    def plus(*x):
#        return f"\tSum of numbers -->{x}--> is ==>({sum(x)})<==\n"
        return sum(x)

#    def __init__(self, *x):
#        self.x = x

    def minus(*x):
        x = [-x for x in x]
# [-1, -2, 3, -4, 5]
        x[0] = -x[0]
# [1, -2, 3, -4, 5]
#        return f"\tDifference of numbers -->{x}--> is ==>({sum(x)})<==\n"
        return sum(x)

    def mult(*x):
        num = x[0]
        i = 0
        while i < len(x) - 1:
            num = num * x[i + 1]
            i += 1
#        return f"\tProduct of numbers -->{x}--> is ==>({num})<==\n"
        return num

    def divis(*x):
        num = x[0]
        i = 0
        while i < len(x) - 1:
            num = num / x[i + 1]
            i += 1
#        return f"\tQuotient of numbers -->{x}--> is ==>({num})<==\n"
        return num

    def expon(x, n):
        num = pow(x, n)
#        return f"\t{n} ** {x} = {num}\n"
        return num

#print(Calc.plus(1, 2, -3, 4, -5))
# Sum of numbers -->(1, 2, -3, 4, -5)--> is ==>(-1)<==
#print(Calc.minus(1, 2, -3, 4, -5))
# Difference of numbers -->[1, -2, 3, -4, 5]--> is ==>(3)<==
#print(Calc.mult(1, 2, -3, 4, -5))
# Product of numbers -->(1, 2, -3, 4, -5)--> is ==>(120)<==
#print(Calc.divis(1, 2, -3, 4, -5))
# Quotient of numbers -->(1, 2, -3, 4, -5)--> is ==>(0.008333333333333333)<==
#print(Calc.expon(2, -3))
# -3 ** 2 = 0.125
