class StoredLogins:
    """
    Takes user's name (code, id), login, password
    and stores them here in dictionary
    ...
    Methods:
    ---------------------------------------------------
    input_data_sep():
        takes user's name and log-in data,
        send them to dictionary, where stored
        separately as: {'Login'="x", 'Password'="y"}.
    input_data_tog():
        takes user's name and log-in data,
        send them to dictionary, where stored them
        separately, as: {'Name': {'Login': 'Password'}}
    """
    name = None
    login = None
    password = None

    def __init__(self, name, login, password):
        self._name = name
        self.__login = login
        self.__password = password
        StoredLogins.input_data_sep(self, name, login, password)
        StoredLogins.input_data_tog(name, login, password)

    def input_data_sep(self, name, login, password):
        """
        login data stores as: {'Login'="x", 'Password'="y"}
        """
        name = dict()
        name["Login"] = login
        name["Password"] = password
        stored_logins_sep[self._name] = name

    def input_data_tog(self, login, password):
        """
        login data stores as: {'Name': {'Login': 'Password'}}
        """
        stored_logins_tog.update({login: password})


stored_logins_tog = dict()
stored_logins_sep = dict()

user1 = StoredLogins("Radagast", "brown", "123")
user2 = StoredLogins("Gandalf", "grey", "456")
user3 = StoredLogins("Saruman", "white", "789")

if __name__ == "__main__":
#    help(StoredLogins)
    print(stored_logins_sep)
# {'Radagast': {'Login': 'brown', 'Password': '123'},
# 'Gandalf': {'Login': 'grey', 'Password': '456'},
# 'Saruman': {'Login': 'white', 'Password': '789'}}
    print(stored_logins_tog)
# {'brown': '123', 'grey': '456', 'white': '789'}
