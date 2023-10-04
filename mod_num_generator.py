class NumberGeneratorSearcher:
    """
    Generator of various number collections,
    or finder the numbers in existing collection
    ...
    Methods
    -------
    classic_input():

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

def find_odd(seq):
    for num in seq:
        if num % 2 != 0:
            yield num


x = find_odd(range(100))
print(next(x))
print(next(x))
print(next(x))
