import gen_find_num
#help(gen_find_num)

lst = [1, 2, 3, 4, 17, 47, 50, 90, 101, 0]
gen = gen_find_num.GenFindNum(lst)

fin_lst = gen.find_prime()
print(list(fin_lst))                                # [2, 3, 17, 47, 101]
# or
#print(next(fin_lst))                                # 2
#print(next(fin_lst))                                # 3
#print(next(fin_lst))                                # 17
#print(next(fin_lst))                                # 47
#print(next(fin_lst))                                # 101
#print(next(fin_lst))                                # StopIteration

lst = range(1, 99)
gen = gen_find_num.GenFindNum(lst)

prime = gen.find_prime()
#print(list(prime))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
gen = gen_find_num.GenFindNum(prime)
prime_odd = gen.find_odd()
# [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(list(prime_odd))
