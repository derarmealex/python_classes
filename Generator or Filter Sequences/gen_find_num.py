class GenFindNum:
    """
    Generator of various number collections,
    or finder specific numbers in existing collection.
    OUTPUT:
    You should have variable as:
    x = gen_find_num.GenFindNum.find_odd()
    then use ==> [print]next(x) <==
    to return every next element of sequence,
    or just use [print](x) to return sequence
    ...
    Methods
    -------
    find_prime(lst):
        extract prime numbers from given sequence
    find_odd(lst):
        extract odd numbers from given sequence
    find_even(lst):
        extract even numbers from given sequence
    """
    lst = None

    def __init__(self, lst):
        self.lst = lst
        """
        set attributes for GenFindNum
        ...
        Attributes
        ----------
        """
    def find_prime(self):
        for num in self.lst:
            if num > 1:
                ctr_num = 2
                while ctr_num < num:
                    prime_ctr = num % ctr_num
                    ctr_num += 1
                    if prime_ctr == 0:
                        break
                else:
                    yield num
            else:
                continue

    def find_odd(self):
        for num in self.lst:
            if num % 2 != 0:
                yield num

    def find_even(self):
        for num in self.lst:
            if num % 2 == 0:
                yield num
