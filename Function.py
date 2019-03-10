from Constant import S_BOX, NON_FIBONACCI_NUM
import math


class Function:
    def __init__(self, binary_plain, binary_key):
        if len(binary_plain) != 64 or len(binary_key) != 64: raise Exception()
        self.binary_plain = binary_plain
        self.binary_key = binary_key

        self.REPETITION = 2

    def __substitute_using_non_fibonacci_index(self):
        string = list(self.binary_plain)
        for num in NON_FIBONACCI_NUM:
            string[num] = "1" if string[num] == "0" else "0"

        self.binary_plain = "".join(string)

    def __substitute_using_s_box(self):
        string = split_string_into_list_of_length_n(self.binary_plain, 8)
        for index in range(len(string)):
            string[index] = str(S_BOX[int(string[index], 2)])
        for index in range(len(string)):
            string[index] = "{:08b}".format(int(string[index]))

        self.binary_plain = "".join(string)

    def __transpose(self):
        string = split_string_into_list_of_length_n(self.binary_plain, 8)
        string[0], string[3], string[4], string[7] = string[3], string[0], string[7], string[4]

        self.binary_plain = "".join(string)

    def __slide(self):
        string_on_the_left = split_string_into_list_of_length_n(self.binary_plain[:30], 5)
        string_on_the_right = split_string_into_list_of_length_n(self.binary_plain[34:], 5)
        string_on_the_center = self.binary_plain[30:-30]
        for index in range(len(string_on_the_left)):
            string_on_the_left[index] = switch_string_of_five(string_on_the_left[index])
        for index in range(len(string_on_the_right)):
            string_on_the_right[index] = switch_string_of_five(string_on_the_right[index])
        self.binary_plain = "".join(string_on_the_left) + string_on_the_center + "".join(string_on_the_right)

    def __xor_with_key(self):
        string = split_string_into_list_of_length_n(self.binary_plain, 4)
        string_key = split_string_into_list_of_length_n(self.binary_key, 4)
        for index in range(len(string)):
            string[index] = "{:04b}".format(int(string[index], 2) ^ int(string_key[len(string_key) - 1 - index], 2))

        self.binary_plain = "".join(string)

    def __generate_round_key(self):
        string = split_string_into_list_of_length_n(self.binary_plain, 8)
        string_key = split_string_into_list_of_length_n(self.binary_key, 8)
        for index in range(len(string_key)):
            num_1, num_2 = int(string[index], 2), int(string_key[index], 2)
            num_result = int(math.floor(math.sqrt((num_1 * num_1) + (num_2 * num_2)))) % 256
            string_key[index] = "{:08b}".format(num_result)

        self.binary_key = "".join(string_key)

    def run(self):
        for i in range(self.REPETITION):
            self.__substitute_using_non_fibonacci_index()
            self.__substitute_using_s_box()
            self.__slide()
            self.__xor_with_key()
        return self.binary_plain


def split_string_into_list_of_length_n(string, n):
    if (len(string) % n) != 0: raise Exception()
    return [string[i:i + n] for i in range(0, len(string), n)]

def switch_string_of_five(string):
    if len(string) != 5: raise Exception()
    return string[3] + string[4] + string[2] + string[0] + string[1]

if __name__ == "__main__":
    src = "1111000011110000111100001111000011110000111100001111000011110000"
    key = "0011001100110011001100110011001100110011001100110011001100110011"
    f = Function(src, key)
    print(f.run())