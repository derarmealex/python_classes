import stored_logins
import login_ctr
import extract_dict
#help(stored_logins)
#help(login_ctr)
#help(extract_dict)

extract = extract_dict.Extract()

user1 = stored_logins.Storage("Radagast", "brown", "123")
user2 = stored_logins.Storage("Gandalf", "grey", "456")
user3 = stored_logins.Storage("Saruman", "white", "789")
#print(stored_logins.Storage.database())
# {'Radagast': {'Login': 'brown', 'Password': '123'},
# 'Gandalf': {'Login': 'grey', 'Password': '456'},
# 'Saruman': {'Login': 'white', 'Password': '789'}}

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
