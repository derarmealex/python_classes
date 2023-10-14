class LoginCtr:
    """
    Retrieves and controls log-in data
    as pair name, password
    ...
    Methods
    ----------------------------------------------
    __init__():
        retrieves user log-in data to control
    return_input_try():
        returns user login and password as entered
    search_matches():
        takes log-in data as pair name, password
        from user and seeks for matching pair
        in internal login database
    """
    login = None
    password = None

    __slots__ = ["__login", "__password"]

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def return_input_try(self):
        return self.__login, self.__password

    def search_matches(self, extract):
        from stored_logins import login_database
        extracted_logins = list(extract.vals_dct_in_dct(login_database))
        for log_pas in extracted_logins:
            if self.__login in log_pas[1] and self.__password in log_pas[1]:
                return log_pas
        print("\n\tUsername or password isn't OK!\n")
