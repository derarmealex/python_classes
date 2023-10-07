import gen_find_num
#help(gen)
gen = gen_find_num.GenFindNum()

lst = [1, 2, 3, 4, 17, 47, 50, 90, 101, 0]
fin_lst = gen.find_prime(lst)

#print(list(fin_lst))                               # [2, 3, 17, 47, 101]
# or
print(next(fin_lst))                               # 2
print(next(fin_lst))                               # 3
print(next(fin_lst))                               # 17
print(next(fin_lst))                               # 47
print(next(fin_lst))                               # 101
print(next(fin_lst))                               # StopIteration
