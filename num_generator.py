class NumGenSearch:
    """
    Generator of various number collections,
    or finder specific numbers in existing collection.
    You should have variable as:
    x = mod_generator.NumGenSearch.find_odd(seq)
    then use ==> [print]next(x) <==
    to return every next element of sequence,
    or use res_output(seq) method here.
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

    def find_prime(seq):
        for num in seq:
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

    def find_odd(seq):
        for num in seq:
            if num % 2 != 0:
                yield num

    def find_even(seq):
        for num in seq:
            if num % 2 == 0:
                yield num


#import num_generator as gen
#help(gen)
#lst = [1, 2, 3, 4, 17, 47, 50, 90, 101, 0]
#x = gen.NumGenSearch.find_prime(lst)
#print(list(x))                             # [2, 3, 17, 47, 101]
# or
#print(next(x))                             # 2
#print(next(x))                             # 3
#print(next(x))                             # 17
#print(next(x))                             # 47
#print(next(x))                             # 101
#print(next(x))                             # StopIteration
