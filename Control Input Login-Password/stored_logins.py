class StoredLogins:
    """
    Retrieve and control log-in data
    as pair name, password
    ...
    Methods
    ---------------------------------------------
    __init__():
        retrieve user log-in data to control
    return_input_try():
        return user login and password as entered
    input_control():
        take log-in data as pair name, password
        from user and seek for matching pair
        in internally stored login data database
    """
    login = None
    password = None

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def return_input_try(self):
        return self.__login, self.__password

    def input_control(self, extract):
        extracted_logins = extract.vals_dct_in_dct(stored_logins)
        for log_pas in extracted_logins:
            if self.__login == log_pas[0] and self.__password == log_pas[1]:
                return log_pas
        print("\n\tUsername or password isn't OK!\n")


stored_logins = {
        'Radagast': {'Login': 'brown', 'Password': '123'},
        'Gandalf': {'Login': 'grey', 'Password': '456'},
        'Saruman': {'Login': 'white', 'Password': '789'}
                }
