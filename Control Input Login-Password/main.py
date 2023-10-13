import input_name_pas
import stored_logins
import extract_dict
#help(input_name_pas)
#help(stored_logins)
#help(extract_dict)

extract = extract_dict.Extract()
stores = stored_logins.StoredLogins()
count = 3
control_result = ""
while not control_result and count > 0:
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    input_try = input_name_pas.InNamePas(login, password)
    input_control = input_try.control(stores)
    control_result = stores.input_control(extract)
    count -= 1
if control_result: print("\n\tWelcome to app! You can go on...")
else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")
