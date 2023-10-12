import input_name_pas
import stored_logins

stores = stored_logins.StoredLogins()
count = 3
result_control = ""
while not result_control and count > 0:
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    input_try = input_name_pas.InNamePas(login, password)
    input_control = input_try.control(stores)
    result_control = stores.input_control()
    count -= 1
if result_control: print("\n\tWelcome to app! You can go on...")
else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")
