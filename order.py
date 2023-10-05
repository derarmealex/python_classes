class Order:
    """
    Organiser of sequences
    ...
    Methods
    -------
    org_stg_stg(seq):
        arrange string numbers in ascending order.
        They have to be separated by commas.
        Sorted string will be returned as STRING
    org_stg_lst(seq):
        arrange string numbers in ascending order.
        They have to be separated by commas.
        Sorted string will be returned as LIST
    """
    def org_stg_stg(stg):
        split_stg = stg.split(",")                  # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        final = ", ".join([str(x) for x in final])
        return final                                # -8, -2, 0, 1, 3, 10, 18
    def org_stg_lst(stg):
        split_stg = stg.split(",")                  # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        return final                                # [-8, -2, 0, 1, 3, 10, 18]

#import order
#help(order)
#stg = " 0, -2,10,  1, -8,18, 3  "
#print(order.Order.org_stg_stg(stg))
#print(order.Order.org_stg_lst(stg))
