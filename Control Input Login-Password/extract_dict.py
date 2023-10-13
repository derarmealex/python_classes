class Extract:
    """
    Extract pairs of login, password from
    internally stored login data database
    and compares every pair with
    log-in data from user to seek for matching
    ...
    Methods
    -----------------------------------------------
    vals_dct_in_dct():
        Extract all values from immersed dictionary
        as pair login, password
    """
    dct = None

    def vals_dct_in_dct(self, dct):
        self.__dct = dct
        vals = self.__dct.values()
        for pair in vals:
            final = []
            for key in pair:
                final.append(pair[key])
            yield final
