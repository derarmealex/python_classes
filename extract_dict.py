class Extract:
    """
    Extract elements from dictionary
    OUTPUT:
    You should have variable as:
    x = extract.extract.vals_dct_in_dct()
    then use ==> [print]next(x) <==
    to return every next element of sequence,
    or just use [print](x) to return sequence
    ...
    Methods
    -------
    def keys_dct(dct):
        Extract all keys from dictionary
    def vals_dct(dct):
        Extract all values from dictionary
    vals_dct_in_dct(dct, key_word):
        Extract all values from immersed dictionary
        which stored with keys matched to key_word
    """
    def keys_dct(self, dct):
        dct = list(dct)
        for key in dct:
            yield key

    def vals_dct(self, dct):
        dct = dct.values()
        for val in dct:
            yield val

    def vals_dct_in_dct(self, dct, key_word):
        vals = list(dct.values())
# [{'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}, {'Name': 'Matous' ...
        for item in vals:
            for key in item:
                if key == key_word:
                    yield item[key]


#import extract_dict as extract
#help(extract)
#extract = Extract()

# SIMPLE DICTIONARY - KEYS
#dct = {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}
#fin_lst = extract.extract.keys_dct(dct)

#print(list(fin_lst))                                   # ['Name', 'Surname', 'Email']
# or
#print(next(fin_lst))                                   # Name
#print(next(fin_lst))                                   # Surname
#print(next(fin_lst))                                   # Email
#print(next(fin_lst))                                   # StopIteration

# SIMPLE DICTIONARY - VALUES
#dct = {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}
#fin_lst = extract.extract.vals_dct(dct)

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
#fin_lst = extract.extract.vals_dct_in_dct(dct, key_word)
#print(list(fin_lst))
# ['marek.parek@gmail.com', 'matous.svatous@gmail.com', 'anna.rana@gmail.com', 'alex.brown@rhosgobel.com']
# or
#print(next(fin_lst))                                   # marek.parek@gmail.com
#print(next(fin_lst))                                   # matous.svatous@gmail.com
#print(next(fin_lst))                                   # anna.rana@gmail.com
#print(next(fin_lst))                                   # alex.brown@rhosgobel.com
#print(next(fin_lst))                                   # StopIteration
