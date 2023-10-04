class NumberGeneratorSearcher:
    """
    Generator of various number collections,
    or finder the numbers in existing collection.
    You should have variable as
    x = mod_generator.NumberGeneratorSearcher.find_odd(seq)
    then use ==> print(next(x)) <==
    for return every next element of sequence
    ...
    Methods
    -------
    find_prime(seq):
        extract prime numbers from given sequence
    find_odd(seq):
        extract odd numbers from given sequence
    find_even(seq):
        extract even numbers from given sequence
    """
    def find_odd(seq):
        for num in seq:
            if num % 2 != 0:
                yield num

    def find_even(seq):
        for num in seq:
            if num % 2 == 0:
                yield num

    def find_prime(seq):
        num = 2
        while num < seq[-1]:
            for i in seq:
                if i != 0:
                    if num % i == 0:
                        break
                else:
                    continue
            else:
                print(num)
                yield num
            num += 1
