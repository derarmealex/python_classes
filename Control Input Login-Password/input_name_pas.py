class InNamePas:
    """
    Log-in data input: name, password
    ...
    Methods
    -----------------------------------------------------
    input_try():
        Retrieve log-in data as name, password from user
    control():
        Send log-in data to find matches in user database
    """
    login = None
    password = None

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def return_input_try(self):
        return self.__login, self.__password

    def control(self, stores):
        stores.input_data(self.__login, self.__password)
