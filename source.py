from tools import *
import math

def transpose(bin_str):
    temp = hex(int(bin_str,2))
    temp = temp[2:]
    temp = split_array(temp, 4)
    result_trans = ""
    result = ""
    print(temp)

    for c in temp:
        # transpose
        result_trans += c[3] + c[1] + c[2] + c[0]
    
    print(result_trans)
    
    # for i in split_array(bin(int(result_trans,16))[2:],8):
    #     result += i.zfill(8)
    result = bin(int(result_trans,16))[2:]
    if  len(result) % 8 != 0:
        result = result.zfill(len(result) + 8 - (len(result)%8))
    return result

def xor_key(bin_str,key):
    bin_arr = split_array (bin_str,4)
    key_arr = split_array (key[::-1],4)
    result = ""

    for i in range(8):
        result += bin(int(bin_arr[i],2) ^ int(key_arr[i],2))[2:].zfill(4)

    return result

def generate_rkey(cbin,key):
    cbin_arr = split_array (cbin,8)
    key_arr = split_array (key ,8)
    result = ''

    for i in range(4):
        result += bin(math.floor(math.sqrt(int(cbin_arr[i],2)**2 + int(key_arr[i],2)**2)%256))[2:].zfill(8)

    return result

# test
# transpose('0010010111110000') = '0000010111110010'
# xor_key ('10000000100000001000000010000000', '11110000111100001111000011110000') = '10001111100011111000111110001111'
print(generate_rkey('10001011100010111000101110001011', '11001100110011001100110011001100'))