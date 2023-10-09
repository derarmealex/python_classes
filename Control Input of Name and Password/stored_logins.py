class StoredLogins:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        """
        set attributes for Extract
        ...
        Attributes
        --------------------------
        """
    def input_ctr(self, login, password, key_word, key_word2):
        import extract_dict
        extract = extract_dict.Extract(stored_logins_sep, key_word, key_word2)
        x = extract.vals_dct_in_dct()
        for log_pas in x:
            if login == log_pas[0] and password == log_pas[1]:
                return log_pas
        print("bad")


stored_logins_sep = {
        'Radagast': {'Login': 'brown', 'Password': '123'},
        'Gandalf': {'Login': 'grey', 'Password': '456'},
        'Saruman': {'Login': 'white', 'Password': '789'}
                    }
"""
key_word = ""
key_word2 = ""
StoredLogins.input_ctr("grey", "456", key_word, key_word2)
"""