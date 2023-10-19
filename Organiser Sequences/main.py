import ordering
#help(ordering)

stg = ordering.Order(" 0, -2,10,  1, -8,18, 3  ")

print(stg.ord_stg_to_stg_up())              # -8, -2, 0, 1, 3, 10, 18
print(stg.ord_stg_to_lst_up())              # [-8, -2, 0, 1, 3, 10, 18]
print(stg.ord_stg_to_stg_down())            # 18, 10, 3, 1, 0, -2, -8
print(stg.ord_stg_to_lst_down())            # [18, 10, 3, 1, 0, -2, -8]

stg = ordering.Order(3)                     # String needed. Your item -->3<-- can't be processed
print(stg.ord_stg_to_stg_up())
