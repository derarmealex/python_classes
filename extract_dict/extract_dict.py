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
