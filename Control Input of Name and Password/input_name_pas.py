class InNamePas:
    """
    Log-in data input: name, password
    ...
    Methods
    -----------------------------------------------------
    input_try():
        Retrieves log-in data as name, password from user
    """
    def input_try(self):
        login = input("Enter your username: ")
        pas = input("Enter your password: ")
        return login, pas
