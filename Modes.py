from Function import *
from Feistel import *
import random

class Modes:
    def __init__(self, plain, key):
        self.plain = plain
        if len(key>8):
            random.seed(key)
            self.key = ''.join(random.sample(key[:8]))
        else:
            # key < 8 bytes
            padding = 8-len(key)
            random.seed(padding)
            while len(temp_key) < 8:
                temp_key = key + ''.join(random.sample(key))
            self.key = temp_key[:8]
        self.bplain = pkcs5_padding(change_ascii_to_bits(self.plain))
        self.bkey = change_ascii_to_bits(self.key)
    

    def ecb_encrypt(self):
        f = Feistel(self.bplain,self.bkey)
        return f.encrypt()
    
    def cbc_encrypt(self):
        input_plain = split_string_into_list_of_length_n(self.bplain,64)
        iv = 'rypythencryption'
        index = 0
        result = ''

        for i in input_plain:
            if index == 0:
                c = iv
            i = i ^ c
            f = Feistel(i,self.bkey)
            c = f.encrypt()
            result += c
            index += 1
        
        return result



