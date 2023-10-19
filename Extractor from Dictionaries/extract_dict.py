class ExtractorDct:
    """
    Extract elements from dictionary
    ...
    OUTPUT:
    You should have variable as:
    x = extract.Extract.vals_dct_in_dct()
    then use ==> [print]next(x) <==
    to return every next element of sequence,
    or just use [print](x) to return sequence
    ...
    Methods
    ----------------------------------------------------
    keys_dct(dct):
        extract all keys from dictionary
    vals_dct(dct):
        extract all values from dictionary
    vals_dct_in_dct(dct):
        extract all values from immersed dictionary
        which is stored with keys matched to key_word(s)
    items_dct_in_dct(dct):
        extract all items from immersed dictionary
        which is stored with keys matched to key_word(s)
        and returned all items of every sub-dictionary
        that matched
    """
    def __init__(self, dct, key_word="", key_word2="", key_word3=""):
        self.dct = dct
        self.key_word = key_word
        self.key_word2 = key_word2
        self.key_word3 = key_word3

    def keys_dct(self):
        dct = self.dct.keys()
        for key in dct:
            yield key

    def vals_dct(self):
        dct = self.dct.values()
        for val in dct:
            yield val

    def vals_dct_in_dct(self, key_word="", key_word2="", key_word3=""):
        vals = self.dct.values()
        for item in vals:
            final = []
            for key in item:
                if key == key_word:
                    final.append(item[key])
                elif key == key_word2:
                    final.append(item[key])
#                elif key == key_word3:
#                    final.append(item[key])
                elif not key_word:
                    final.append(item[key])
            yield final

    def items_dct_in_dct(self, key_word="", key_word2="", key_word3=""):
        items = self.dct.items()
        for item in items:
            for key in item[1:]:
                final = []
                for x in key:
                    if x == key_word:
                        final.append(key[x])
                    elif x == key_word2:
                        final.append(key[x])
#                    elif x == key_word3:
#                        final.append(key[x])
                    elif not key_word:
                        final.append(key[x])
            yield item[0], final
