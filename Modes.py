from Function import *
from Feistel import *
import random

class Modes:
    def __init__(self, plain, key):
        self.plain = plain
        if len(key)>8:
            random.seed(key)
            self.key = ''.join(random.sample(key[:8]))
        else:
            # key < 8 bytes
            padding = 8-len(key)
            random.seed(padding)
            temp_key=''
            while len(temp_key) < 8:
                temp_key = key + ''.join(random.sample(key,len(key)))
            self.key = temp_key[:8]
        self.bplain = pkcs5_padding(change_ascii_to_bits(self.plain))
        self.bkey = change_ascii_to_bits(self.key)
    

    def ecb_encrypt(self):
        result = ''
        for i in self.bplain:
            f = Feistel(i,self.bkey)
            result += f.encrypt()
        return result

    def ecb_decrypt(self):
        cipher_arr = split_string_into_list_of_length_n(change_ascii_to_bits(self.plain),128)
        result = ""
        for i in cipher_arr:
            f = Feistel(i, self.bkey)
            result += f.decrypt()
        result = last_byte_check(result)
        return result
    
    def cbc_encrypt(self):
        # input_plain = split_string_into_list_of_length_n(self.bplain,64)
        iv = 'rypythencryption'
        index = 0
        result = ''

        for i in self.bplain:
            if index == 0:
                c = iv
            i = bin(int(i,2) ^ int(change_ascii_to_bits(c),2))[2:].zfill(128)
            f = Feistel(i,self.bkey)
            c = f.encrypt()
            result += c
            index += 1
        
        return result
    
    def cbc_decrypt(self):
        input_bcipher = split_string_into_list_of_length_n(change_ascii_to_bits(self.plain),128)
        iv = 'rypythencryption'
        index = 0
        result = ''

        for i in input_bcipher:
            f = Feistel(i,self.bkey)
            if index == 0:
                c = change_ascii_to_bits(iv)
                print(c)
            p = f.decrypt()
            p = bin(int(p,2) ^ int(c,2))[2:].zfill(128)
            c = i
            result += p
            index += 1

        result = last_byte_check(result)
        return result

    # def cfb_encrypt(self):

if __name__ == "__main__":
    m = Modes('abcdefghijklmnopq','abcdefgh')
    e = m.cbc_encrypt()
    print("hasil encrypt : ",e)
    n = Modes(e,'abcdefgh')
    d = n.cbc_decrypt()
    print("hasil decrypt : ",d)




