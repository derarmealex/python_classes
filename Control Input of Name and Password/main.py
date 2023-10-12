import input_name_pas
import stored_logins

input_try = input_name_pas.InNamePas()

count = 3
input_ctr = ""
while not input_ctr and count > 0:
    login, password = input_try.input_try()
    count -= 1
    input_data = stored_logins.StoredLogins(login, password)
    input_ctr = input_data.input_ctr(login, password)
if input_ctr: print("\n\tWelcome to app! You can go on...")
else: print("Just 3 tries to connect per day unfortunately. See ya tomorrow. (:")
