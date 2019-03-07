# split array every n element
def split_array(seq, num):
    out = []
    last = 0

    while last < len(seq):
        out.append(seq[int(last):int(last + num)])
        last += num
    return out