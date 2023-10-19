class Extract:
    """
    Extract pairs of login, password from
    internal login database
    and compares every pair with
    log-in data from user to seek for matching
    ...
    Methods
    -----------------------------------------------
    vals_dct_in_dct(dct):
        extract all values from immersed dictionary
        as name (code, id) and pair login, password
    """
    def vals_dct_in_dct(self, login_database):
        items = login_database.items()
        for item in items:
            for key in item[1:]:
                final = []
                for val in key:
                    final.append(key[val])
            yield item[0], final
