class NumGenSearch:
    """
    Generator of various number collections,
    or finder specific numbers in existing collection.
    OUTPUT:
    You should have variable as:
    x = mod_generator.NumGenSearch.find_odd()
    then use ==> [print]next(x) <==
    to return every next element of sequence,
    or just use [print](x) to return sequence
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
    def find_prime(self, seq):
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

    def find_odd(self, seq):
        for num in seq:
            if num % 2 != 0:
                yield num

    def find_even(self, seq):
        for num in seq:
            if num % 2 == 0:
                yield num


#import generator_num as gen
#help(gen)
#gen = NumGenSearch()

#lst = [1, 2, 3, 4, 17, 47, 50, 90, 101, 0]
#fin_lst = gen.gen.find_prime(lst)

#print(list(fin_lst))                               # [2, 3, 17, 47, 101]
# or
#print(next(fin_lst))                               # 2
#print(next(fin_lst))                               # 3
#print(next(fin_lst))                               # 17
#print(next(fin_lst))                               # 47
#print(next(fin_lst))                               # 101
#print(next(fin_lst))                               # StopIteration
