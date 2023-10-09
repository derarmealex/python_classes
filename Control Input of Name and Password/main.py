#import stores_name_pas as stores
#import extract_dict
import input_name_pas
import stored_logins

#help(stores)

control = ""
while not control:
    log_data = input_name_pas.InNamePas()
    login, password = tuple(log_data.input_try())
    input_data = stored_logins.StoredLogins(login, password)
    key_word = ""
    key_word2 = ""
    control = input_data.input_ctr(login, password, key_word, key_word2)
if control: print("You're lucky")
else: print("Just 3 tries to connect per day unfortunately. See ya tomorrow. (:")

"""
dct = {
        'Radagast': {'Login': 'brown', 'Password': '123'},
        'Gandalf': {'Login': 'grey', 'Password': '456'},
        'Saruman': {'Login': 'white', 'Password': '789'}
                    }

dct = extract_dict.Extract(dct)
x = dct.items_dct_in_dct(dct)
print(list(x))
"""