from tools import *

def transpose(bin):
    temp = hex(int(bin,2))
    temp = temp.replace('0x','')
    temp = split_array(temp, 4)
    print(temp)
    result = []

    for c in temp:
        # transpose
        result_trans = c[3] + c[1] + c[2] + c[0]
        print(result_trans)
        result.append(result_trans)
    
    return result


# test
# transpose (25f0) = 05f2