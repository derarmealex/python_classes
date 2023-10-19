class Order:
    """
    Order your string
    ...
    Methods
    -----------------------------------------------
    org_stg_stg_up(str):
        arrange string numbers in ASCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as STRING
    org_stg_lst_up(str):
        arrange string numbers in ASCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as LIST
    org_stg_stg_down(str):
        arrange string numbers in DESCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as STRING
    org_stg_lst_down(str):
        arrange string numbers in DESCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as LIST
    """
    __slots__ = ["stg"]

    def __init__(self, stg):
        if isinstance(stg, str):
            self.stg = stg
        else:
            print(f"\n\tString needed. Your item -->{stg}<-- can't be processed")
            exit()

    def ord_stg_to_stg_up(self):
        split_stg = self.stg.split(",")             # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        final = ", ".join([str(x) for x in final])
        return final                                # -8, -2, 0, 1, 3, 10, 18

    def ord_stg_to_lst_up(self):
        split_stg = self.stg.split(",")             # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        return final                                # [-8, -2, 0, 1, 3, 10, 18]

    def ord_stg_to_stg_down(self):
        split_stg = self.stg.split(",")             # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)[::-1]
        final = ", ".join([str(x) for x in final])
        return final                                # 18, 10, 3, 1, 0, -2, -8

    def ord_stg_to_lst_down(self):
        split_stg = self.stg.split(",")             # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)[::-1]
        return final                                # [18, 10, 3, 1, 0, -2, -8]
