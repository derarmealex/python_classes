class StoredLogins:
    """
    Log-in data control: name, password
    ...
    Methods
    --------------------------------------------
    input_ctr():
        Takes log-in data as pair name, password
        from user and seek for a matching pair
        in internally stored login data database
    """
    login = None
    password = None

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        """
        set attributes for Extract
        ...
        Attributes
        --------------------------
        """
    def input_ctr(self, login, password):
        import extract_dict
        extract = extract_dict.Extract()
        extracted_logins = extract.vals_dct_in_dct(stored_logins)
        for log_pas in extracted_logins:
            if login == log_pas[0] and password == log_pas[1]:
                return log_pas
        print("\n\tUsername or password isn't OK!\n")


stored_logins = {
        'Radagast': {'Login': 'brown', 'Password': '123'},
        'Gandalf': {'Login': 'grey', 'Password': '456'},
        'Saruman': {'Login': 'white', 'Password': '789'}
                }
