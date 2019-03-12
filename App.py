from Modes import *
from Feistel import *
import sys, getopt
import time

def get_option():
    print("Nomor pilihan : ")
    option = ["ECB","CBC","CFB","OFB","counter"]
    number = 1
    for mode in option:
        print(number, 'Enkripsi ' + mode)
        number += 1
        print(number, 'Dekripsi ' + mode)
        number += 1
    numb = input("Masukkan nomor pilihan : ")
    return numb

def get_filename():
    filename = input("Masukkan nama file : ")
    return filename

def get_key():
    key = input("Masukkan kunci : ")
    return key

def get_save_name():
    savename = input("Masukkan nama file setelah diproses : ")
    return savename

def savefile(e, savename):
    temp = []
    for i in split_string_into_list_of_length_n(change_ascii_to_bits(e),8):
        temp.append(int(i,2))
    save = bytes(temp)
    save_output_bytes(save,savename)

if __name__ == "__main__":
    opt = int(get_option())
    filename = str(get_filename())
    key = str(get_key())
    savename = str(get_save_name())
    input_plain = ''
    input_plain = read_input_bytes(filename)
    m = Modes(input_plain,key)
    start = time.time()
    if opt == 1:
        e = m.cbc_encrypt()
        savefile(e,savename)
    if opt == 2:
        e = m.cbc_decrypt()
        savefile(e,savename)
    if opt == 3:
        e = m.cbc_encrypt()
        savefile(e,savename)
    if opt == 4:
        e = m.cbc_decrypt()
        savefile(e,savename)
    if opt == 5:
        e = m.cfb_encrypt()
        savefile(e,savename)
    if opt == 6:
        e = m.cfb_decrypt()
        savefile(e,savename)
    if opt == 7:
        e = m.ofb_encrypt()
        savefile(e,savename)
    if opt == 8:
        e = m.ofb_decrypt()
        savefile(e,savename)
    if opt == 9:
        e = m.counter_encrypt()
        savefile(e,'encrypted')
    if opt == 10:
        e = m.counter_decrypt()
        savefile(e,savename)
    end = time.time()
    print("Waktu eksekusi = ", end-start)