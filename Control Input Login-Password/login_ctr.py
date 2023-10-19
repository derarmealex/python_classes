class LoginCtr:
    """
    Retrieve and control log-in data as pair name, password
    ...
    Methods
    --------------------------------------------------
    input_try():
         enter user's login and password, send them
         to control and
    search_matches():
        take log-in data as pair name, password
        from user and seeks for matching pair
        in internal login database
    """
    def __init__(self):
        LoginCtr.input_try(self)

    def input_try(self):
        self.input_tries = 3
        self.__log_pas = ""
        while not self.__log_pas and self.input_tries > 0:
            self.__login = input("Enter your username: ")
            self.__password = input("Enter your password: ")
            LoginCtr.search_matches(self)
        if self.__log_pas: print("\n\tWelcome to app, " + self.__log_pas[0] + "! You can go on...")
        else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")


    def search_matches(self):
        import extract_dict
        from stored_logins import login_database
        extracted_logins = list(extract_dict.Extract.vals_dct_in_dct(self, login_database))
        for log_pas in extracted_logins:
            if self.__login in log_pas[1] and self.__password in log_pas[1]:
                self.__log_pas = log_pas
                break
        else:
            print("\n\tUsername or password isn't OK!\n")
            self.input_tries -= 1

    def __str__(self):
        return f"{self.__log_pas}"
