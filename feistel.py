from Function import *
import random

def change_ascii_to_bits(string):
    result = ''
    i=0
    for x in string:
        result += format(ord(x), 'b').zfill(8)
        i+=1
    
    return result


def pkcs5_padding(bplain):    
    # PKCS5 padding
    if len(bplain) % 128 != 0:
        # lack in bytes
        lack = int((128 - (len(bplain)%128)) / 8)
        for i in range(lack):
            bplain += '{0:08b}'.format(lack)
    else:
        for i in range(128):
            bplain += '{0:08b}'.format(128)
    bplain_arr = split_string_into_list_of_length_n(bplain,128)
    return bplain_arr

# def split_block(plain):
#     bplain_arr = []
#     i = 0
#     temp = ''
#     for x in plain:
#         temp += format(ord(x), 'b').zfill(8)
#         if i%16==15 or i==len(plain)-1 :
#             bplain_arr.append(temp)
#             temp = ''
#         i+=1
    
#     # PKCS5 padding
#     if len(bplain_arr[-1]) < 128:
#         # lack in bytes
#         lack = int((128 - len(bplain_arr[-1])) / 8)
#         for i in range(lack):
#             bplain_arr[-1] += '{0:08b}'.format(lack)
    
    return bplain_arr

def feistel(r_block,key):
    r_blockint = int(r_block,2)
    keyint = int(key,2)
    result = r_blockint ^ keyint
    return result

def feistel_encrypt(block, key):
    lrblock = [] #tuple of left right block
    result = []
    resultbits = ''
    resultascii = ''
    for i in block:
        lrblock.append(split_string_into_list_of_length_n(i,64))   

    for i in lrblock:
        for j in range(16):
            if j != 0:
                random.seed(16-j)
                key_feistel = ''.join(random.sample(key,len(key)))
            else:
                l = i[0]
                r = i[1]
                key_feistel = key
            temp = bin(feistel(r,key_feistel) ^ int(l,2))[2:].zfill(64)
            l = r
            r = temp  
        result.append(l)
        result.append(r)
    
    for i in result:
        resultbits += i
    resultascii = change_bits_to_ascii(resultbits)
    return resultascii

def feistel_decrypt(cipher, key):
    lrblock = [] #tuple of left right block
    result = []
    resultstr = ''
    for i in cipher:
        lrblock.append(split_string_into_list_of_length_n(i,64))

    for i in lrblock:
        l = i[0]
        r = i[1]
        for j in range(15,-1,-1):
            if j != 0:
                random.seed(16-j)
                key_feistel = ''.join(random.sample(key,len(key)))
            else:
                key_feistel = key
            temp = bin(feistel(l,key_feistel) ^ int(r,2))[2:].zfill(64)
            r = l
            l = temp
        result.append(l)
        result.append(r)
    for i in result:
        resultstr += i
    print(len(resultstr))
    resultstr = last_byte_check(resultstr)
    return resultstr

def last_byte_check(btext):
    btext = split_string_into_list_of_length_n(btext,8)
    count = int(btext[-1],2)
    bits = ''.join(btext[:len(btext)-count])
    result = change_bits_to_ascii(bits)
    return result

def change_bits_to_ascii(bits):
    result = ''
    ascii = split_string_into_list_of_length_n(bits,8)
    for i in ascii:
        result += chr(int(i,2))

    return result

if __name__ == "__main__":
    plain  = "abcdefghijklmnopq"
    key = "abcdefgh"
    bplain = pkcs5_padding(change_ascii_to_bits(plain))
    bkey = change_ascii_to_bits(key)
    # parameter encrypt dan decrypt udh bentuk bits dan kebagi dalam block2 @64bit
    a = feistel_encrypt(bplain,bkey)
    print('hasil encrypt : ', a)
    ablock = split_string_into_list_of_length_n(change_ascii_to_bits(a),128)
    b = feistel_decrypt(ablock,bkey)
    print('hasil decrypt : ', b)
