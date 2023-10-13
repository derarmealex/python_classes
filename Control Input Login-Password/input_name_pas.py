class InNamePas:
    """
    Log-in data input: name, password
    ...
    Methods
    -----------------------------------------------------
    input_try():
        retrieve log-in data as name, password from user
    return_input_try():
        return user login and password as entered
    control():
        send log-in data to find matches in user database
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
