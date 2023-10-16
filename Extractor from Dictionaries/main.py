import extract_dict
#help(extract_dict)

# SIMPLE DICTIONARY - KEYS
key_word = "Name"
key_word2 = "Email"

dct = {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}
dct = extract_dict.Extract(dct)

fin_lst = dct.keys_dct()
print(list(fin_lst))                                    # ['Name', 'Surname', 'Email']
# or
#print(next(fin_lst))                                   # Name
#print(next(fin_lst))                                   # Surname
#print(next(fin_lst))                                   # Email
#print(next(fin_lst))                                   # StopIteration

# SIMPLE DICTIONARY - VALUES
fin_lst = dct.vals_dct()
print(list(fin_lst))                                    # ['Marek', 'Parek', 'marek.parek@gmail.com']
# or
#print(next(fin_lst))                                   # Marek
#print(next(fin_lst))                                   # Parek
#print(next(fin_lst))                                   # marek.parek@gmail.com
#print(next(fin_lst))                                   # StopIteration

# DICTIONARY IN DICTIONARY - VALUES
dct = {
 'employee01': {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'},
 'employee02': {'Name': 'Matous', 'Surname': 'Svatous', 'Email': 'matous.svatous@gmail.com'},
 'employee03': {'Name': 'Anna', 'Surname': 'Rana', 'Email': 'anna.rana@gmail.com'},
 'employee04': {'Name': 'Alex', 'Surname': 'Brown', 'Email': 'alex.brown@rhosgobel.com'}
            }
dct = extract_dict.Extract(dct)

fin_lst = dct.vals_dct_in_dct(key_word2)
print(list(fin_lst))
# [['marek.parek@gmail.com'], ['matous.svatous@gmail.com'], ['anna.rana@gmail.com'], ['alex.brown@rhosgobel.com']]

# or
#print(next(fin_lst))                                   # marek.parek@gmail.com
#print(next(fin_lst))                                   # matous.svatous@gmail.com
#print(next(fin_lst))                                   # anna.rana@gmail.com
#print(next(fin_lst))                                   # alex.brown@rhosgobel.com
#print(next(fin_lst))                                   # StopIteration

# DICTIONARY IN DICTIONARY - ITEMS
fin_lst = dct.items_dct_in_dct(key_word, key_word2)
print(list(fin_lst))
# [('employee01', ['Marek', 'marek.parek@gmail.com']), ('employee02', ['Matous', 'matous.svatous@gmail.com']),
# ('employee03', ['Anna', 'anna.rana@gmail.com']), ('employee04', ['Alex', 'alex.brown@rhosgobel.com'])]

# or
#print(next(fin_lst))                                   # ('employee01', ('Marek', 'marek.parek@gmail.com'))
#print(next(fin_lst))                                   # ('employee02', ('Matous', 'matous.svatous@gmail.com'))
#print(next(fin_lst))                                   # ('employee03', ('Anna', 'anna.rana@gmail.com'))
#print(next(fin_lst))                                   # ('employee04', ('Alex', 'alex.brown@rhosgobel.com'))
#print(next(fin_lst))                                   # StopIteration
