import ordering
#help(order)
order = ordering.Order()

stg = " 0, -2,10,  1, -8,18, 3  "
print(order.org_stg_stg_up(stg))
print(order.org_stg_lst_up(stg))
print(order.org_stg_stg_down(stg))
print(order.org_stg_lst_down(stg))
