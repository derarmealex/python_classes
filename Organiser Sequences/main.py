import ordering
#help(ordering)

stg = " 0, -2,10,  1, -8,18, 3  "
order = ordering.Order(stg)

print(order.org_stg_stg_up())
print(order.org_stg_lst_up())
print(order.org_stg_stg_down())
print(order.org_stg_lst_down())
