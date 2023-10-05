class Extract:
    """
    Extractor elements from dictionary
    ...
    Methods
    -------
    def keys_dct(dct):
        Extract all keys from dictionary
    def vals_dct(dct):
        Extract all values from dictionary
    vals_dct_in_dct(dct):
        Extract all values from immersed dictionary
        which stored with keys matched to key_word
    """
    def keys_dct(dct):
        dct = list(dct)
        for key in dct:
            yield key

    def vals_dct(dct):
        dct = dct.values()
        for val in dct:
            yield val

    def vals_dct_in_dct(dct):
        vals = list(dct.values())
# [{'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}, {'Name': 'Matous' ...
        for item in vals:
            for key_word in item:
                if key_word == "Email":
                    yield item[key_word]


#import extract_dict as extract
#help(extract)

# SIMPLE DICTIONARY - KEYS
#dct = {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}
#fin_lst = Extract.keys_dct(dct)

#print(list(fin_lst))                                   # ['Name', 'Surname', 'Email']
# or
#print(next(fin_lst))                                   # Name
#print(next(fin_lst))                                   # Surname
#print(next(fin_lst))                                   # Email
#print(next(fin_lst))                                   # StopIteration

# SIMPLE DICTIONARY - VALUES
#dct = {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}
#fin_lst = extract.Extract.vals_dct(dct)

#print(list(fin_lst))                                   # ['Marek', 'Parek', 'marek.parek@gmail.com']
# or
#print(next(fin_lst))                                   # Marek
#print(next(fin_lst))                                   # Parek
#print(next(fin_lst))                                   # marek.parek@gmail.com
#print(next(fin_lst))                                   # StopIteration

# DICTIONARY IN DICTIONARY - VALUES

#dct = {
# 'employee01': {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'},
# 'employee02': {'Name': 'Matous', 'Surname': 'Svatous', 'Email': 'matous.svatous@gmail.com'},
# 'employee03': {'Name': 'Anna', 'Surname': 'Rana', 'Email': 'anna.rana@gmail.com'},
# 'employee04': {'Name': 'Alex', 'Surname': 'Brown', 'Email': 'alex.brown@rhosgobel.com'}
#            }
#key_word = "Email"
#fin_lst = extract.Extract.vals_dct_in_dct(dct)
#print(list(fin_lst))
# ['marek.parek@gmail.com', 'matous.svatous@gmail.com', 'anna.rana@gmail.com', 'alex.brown@rhosgobel.com']
# or
#print(next(fin_lst))                                   # marek.parek@gmail.com
#print(next(fin_lst))                                   # matous.svatous@gmail.com
#print(next(fin_lst))                                   # anna.rana@gmail.com
#print(next(fin_lst))                                   # alex.brown@rhosgobel.com
#print(next(fin_lst))                                   # StopIteration
