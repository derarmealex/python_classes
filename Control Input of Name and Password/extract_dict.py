class Extract:
    """
    Extract pairs login, password from
    internally stored login data database
    and compares every pair with
    log-in data from user to seek for match
    ...
    Methods
    -----------------------------------------------
    vals_dct_in_dct():
        Extract all values from immersed dictionary
        as pair login, password
    """
    dct = None

    def vals_dct_in_dct(self, dct):
        self.dct = dct
        vals = dct.values()
        for pair in vals:
            final = []
            for key in pair:
                final.append(pair[key])
            yield final
