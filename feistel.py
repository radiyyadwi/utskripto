from tools import *
import random

def split_block(plain):
    bplain_arr = []
    i = 0
    temp = ''
    for x in plain:
        temp += format(ord(x), 'b').zfill(8)
        if i%16==15 or i==len(plain)-1 :
            bplain_arr.append(temp)
            temp = ''
        i+=1
    
    # PKCS5 padding
    if len(bplain_arr[-1]) < 128:
        # lack in bytes
        lack = int((128 - len(bplain_arr[-1])) / 8)
        for i in range(lack):
            bplain_arr[-1] += '{0:08b}'.format(lack)
    
    return bplain_arr

def feistel_encrypt(block, key):
    lrblock = [] #tuple of left right block
    result = []
    for i in block:
        lrblock.append(split_array(i,64))
    
    print(lrblock)

    for i in lrblock:
        for j in range(16)
            if j != 0:
                random.seed(16-j)
                key_feistel = random.sample(key,len(key))
            else:
                l = i[0]
                r = i[1]
                key_feistel = key
            # temp = feistel(r,key_feistel) ^ l
            l = r
            r = temp
        result.append(l)
        result.append(r)
    
    return result

# def feistel_decrypt(cipher, key):



    # bplain = ''.join(format(ord(x), 'b').zfill(8) for x in plain)
    # bkey = ''.join(format(ord(x), 'b').zfill(8) for x in key)

    # print("binary plain : ", bplain)
    # print("length of bplain : ", len(bplain))
    # print("binary key : ", bkey)
    # print("length of bkey : ", len(bkey))
    


# feistel("wkwkwkwk", "hehe")
a = split_block("wkwkwkwkwkinitesajayawkwkwkwkwkinitesajayawkwkwkwkwkinitesaj")
feistel(a)