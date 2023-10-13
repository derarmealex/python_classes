import calc
#help(calc)

calc = calc.Calc()

x = (-1, 2, -3, 4, -5)
print(calc.plus(*x))
print(calc.minus(*x))
print(calc.mult(*x))
print(calc.divis(*x))
y = 0.5
n = 3
print(calc.expon(y, n))
print(calc.classic_input())
