import stored_logins
import extract_dict
#help(stored_logins)
#help(extract_dict)

extract = extract_dict.Extract()
count = 3
input_control = ""
while not input_control and count > 0:
    login = input("Enter your username: ")
    password = input("Enter your password: ")
    stores = stored_logins.StoredLogins(login, password)
    input_control = stores.input_control(extract)
    count -= 1
if input_control: print("\n\tWelcome to app! You can go on...")
else: print("Just 3 tries to connect per day, unfortunately. See ya tomorrow. (:")
