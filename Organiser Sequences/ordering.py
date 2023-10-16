class Order:
    """
    Organiser sequences
    ...
    Methods
    ------------------------------------------------
    org_stg_stg_up():
        arranges string numbers in ASCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as STRING
    org_stg_lst_up():
        arranges string numbers in ASCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as LIST
    org_stg_stg_down():
        arranges string numbers in DESCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as STRING
    org_stg_lst_down():
        arranges string numbers in DESCENDING order.
        They have to be separated by commas.
        Sorted string will be returned as LIST
    """
    __slots__ = ["stg"]

    def __init__(self, stg):
        self.stg = stg

    def org_stg_stg_up(self):
        split_stg = self.stg.split(",")           # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        final = ", ".join([str(x) for x in final])
        return final                                # -8, -2, 0, 1, 3, 10, 18

    def org_stg_lst_up(self):
        split_stg = self.stg.split(",")           # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)
        return final                                # [-8, -2, 0, 1, 3, 10, 18]

    def org_stg_stg_down(self):
        split_stg = self.stg.split(",")           # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)[::-1]
        final = ", ".join([str(x) for x in final])
        return final                                # 18, 10, 3, 1, 0, -2, -8

    def org_stg_lst_down(self):
        split_stg = self.stg.split(",")           # [' 0', ' -2', '10', '  1', ' -8', '18', ' 3  ']
        final = []
        for number in split_stg:
            number = number.strip()
            final.append(int(number))
        final = sorted(final)[::-1]
        return final                                # [18, 10, 3, 1, 0, -2, -8]
