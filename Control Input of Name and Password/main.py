#import stores_name_pas as stores
import stores
import control_name_pas as ctr
import extract_dict
#help(stores)

login = ctr.InNamePas()
x, y = tuple(login.input_ctr())

key_word = ""
key_word2 = ""
input_data = stores.DataStore(x, y)
controla = input_data.r(x, y, key_word, key_word2)


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