from constants import *

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
    mem = register_value[Address_Register[rs1]] + bin_dec(sext(imm, 32))

    data_memory[mem] = register_value[Address_Register[rs2]]

