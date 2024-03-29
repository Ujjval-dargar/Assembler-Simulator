from constants import *


def binary(num, n):

    # converting a string number into its binary number
    bin_str = str(bin(abs(int(num))))[2:]

    # finding the length of the binary number
    l = len(bin_str)

    # raising error if the binary representation of number is more than n bits long
    if (l > n or int(num) > 2**(n-1)-1 or int(num) < -2**(n-1)):
        raise AssemblerException("Invalid immediate: Out of range")

    # appending leading zeros to the start of the string
    if (int(num) >= 0):
        bin_str = "0" * (n-l) + bin_str

    # for negative numbers
    else:

        bin_str = "0" * (n-l) + bin_str

        # converting binary string into list
        bin_str = list(bin_str)

        # calculating  two's complement by flipping all the bits and adding one
        for i in range(len(bin_str)):

            if (bin_str[i] == '1'):
                bin_str[i] = '0'

            else:
                bin_str[i] = '1'

        bin_str = ''.join(bin_str)
        bin_str = int(bin_str, 2) + int("1", 2)
        bin_str = str(bin(bin_str))[2:]

    return bin_str


def bin_dec(s):

    if s[0] == '0':
        return int(s, 2)
    
    else:
        # converting binary string into list
        s = list(s)

        # calculating  two's complement by flipping all the bits and adding one
        for i in range(len(s)):

            if (s[i] == '1'):
                s[i] = '0'

            else:
                s[i] = '1'

        s = ''.join(s)
        s = int(s, 2) + int("1", 2)

        return -1*s


def sext(line, bits):
    if line[0] == '0':
        line = (bits-len(line))*'0'+line
    else:
        line = (bits-len(line))*'1'+line
    return line


def S_type(line):
    opcode = line[-7:]

    funct3 = line[-15:-12]

    rs1 = line[-20:-15]
    rs2 = line[-25:-20]

    imm = line[-12:-7]+line[-32:-25]

    s = sext(imm, 32)

    mem = register_value[Address_Register[rs1]] + sext(imm, 32)

    # data_memory[mem] = register_value[Address_Register[rs2]]


# ins = "00000010011000010010000000100011"
# # ins="0000 0010 0110 00010 010 00000 0100011"
# print(ins)
# S_type(ins)
