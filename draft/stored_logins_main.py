import stored_logins
import login_ctr
import extract_dict
#help(stored_logins)
#help(login_ctr)
#help(extract_dict)

user1 = stored_logins.Storage("Radagast", "brown", "123")
user2 = stored_logins.Storage("Gandalf", "grey", "456")
user3 = stored_logins.Storage("Saruman", "white", "789")
#print(stored_logins.Storage.database())
# {'Radagast': {'Login': 'brown', 'Password': '123'},
# 'Gandalf': {'Login': 'grey', 'Password': '456'},
# 'Saruman': {'Login': 'white', 'Password': '789'}}
extract = extract_dict.Extract()

input_try = 3
control_result = ""
while not control_result and input_try > 0:
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    input_control = login_ctr.LoginCtr(login, password)
    control_result = input_control.search_matches(extract)
    input_try -= 1
if control_result: print("\n\tWelcome to app, " + control_result[0] + "! You can go on...")
else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")



class LoginCtr:
    """
    Retrieves and controls log-in data
    as pair name, password
    ...
    Methods
    ------------------------------------------------
    __init__():
        retrieves user's log-in data to control
    return_input_try():
        returns user's login and password as entered
    search_matches():
        takes log-in data as pair name, password
        from user and seeks for matching pair
        in internal login database
    """
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
