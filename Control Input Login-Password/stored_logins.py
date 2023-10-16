class Storage:
    """
    Takes user's name (code, id), login, password
    and stores them here as dictionary
    ...
    Methods:
    -------------------------------------------------
    safe_data():
        takes user's name, log-in data and stores
        them as dictionary:
        {'Name': {'Login': "x", 'Password': "y"}}
    """
    __slots__ = ["__name", "__login", "__password"]

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        Storage.safe_data(self)

    def safe_data(self):
        name = dict()
        name["Login"] = self.__login
        name["Password"] = self.__password
        login_database[self.__name] = name

    def database():
        return login_database

    def __str__(self):
        return f"{self.__name} saved!"


login_database = dict()

# {'Radagast': {'Login': 'brown', 'Password': '123'},
# 'Gandalf': {'Login': 'grey', 'Password': '456'},
# 'Saruman': {'Login': 'white', 'Password': '789'}}
