import stored_logins
import login_ctr
import extract_dict
#help(stored_logins)
#help(login_ctr)
#help(extract_dict)

user1 = stored_logins.Storage("Radagast", "brown", "123")
print(user1)
user2 = stored_logins.Storage("Gandalf", "grey", "456")
print(user2)
user3 = stored_logins.Storage("Saruman", "white", "789")
print(user3)
#print(stored_logins.Storage.database())
# {'Radagast': {'Login': 'brown', 'Password': '123'},
# 'Gandalf': {'Login': 'grey', 'Password': '456'},
# 'Saruman': {'Login': 'white', 'Password': '789'}}

try_input_login_password = login_ctr.LoginCtr()

print(try_input_login_password)
