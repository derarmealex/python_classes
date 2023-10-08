class DataStore:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        """
        set attributes for Extract
        ...
        Attributes
        --------------------------
        """
    def r(self, login, password, key_word, key_word2):
        import extract_dict
        extract = extract_dict.Extract(stored_logins_sep, key_word, key_word2)
        x = extract.vals_dct_in_dct()
        for item in x:
            if login == item[0]:
                print("correct")
                print(item)
                return item
        print("bad")


stored_logins_sep = {
        'Radagast': {'Login': 'brown', 'Password': '123'},
        'Gandalf': {'Login': 'grey', 'Password': '456'},
        'Saruman': {'Login': 'white', 'Password': '789'}
                    }
"""
key_word = ""
key_word2 = ""
DataStore.r("grey", "456", key_word, key_word2)
"""