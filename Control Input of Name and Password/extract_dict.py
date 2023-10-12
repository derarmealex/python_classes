class Extract:
    """
    Extract pair login, password from
    internally stored login data database
    and compares input log-in data
    from user with every pair to find match
    ...
    Methods
    ----------------------------------------------------
    vals_dct_in_dct():
        Extract all values from immersed dictionary
        as pair login, password
    """
    dct = None

    def vals_dct_in_dct(self, dct):
        self.dct = dct
        vals = dct.values()
        for item in vals:
            final = []
            for key in item:
                final.append(item[key])
            yield final
