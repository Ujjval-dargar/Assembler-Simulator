from constants import *

def update_PC():
    program_counter[0]+=1

def appendReg():

    s = str(program_counter)+' '

    for k, v in register_value.items():
        s += str(v)+' '

    with open("output.txt", 'a') as f:
        f.write(s+'\n')


def sext(line, bits):

    if line[0] == '0':
        line = (bits-len(line))*'0'+line

    else:
        line = (bits-len(line))*'1'+line

    return line


def binary(num, n):

    # converting a string number into its binary number
    bin_str = str(bin(abs(int(num))))[2:] 


    # finding the length of the binary number
    l = len(bin_str)  


    #raising error if the binary representation of number is more than n bits long
    if (l > n or int(num) > 2**(n-1)-1 or int(num) < -2**(n-1)):            
        raise AssemblerException("Invalid immediate: Out of range")


    # appending leading zeros to the start of the string
    if (int(num) >= 0):
        bin_str = "0" * (n-l) + bin_str


    #for negative numbers
    else:

        bin_str = "0" * (n-l) + bin_str

        #converting binary string into list 
        bin_str = list(bin_str)

        #calculating  two's complement by flipping all the bits and adding one
        for i in range(len(bin_str)):

            if (bin_str[i] == '1'):
                bin_str[i] = '0'

            else:
                bin_str[i] = '1'

        bin_str = ''.join(bin_str)
        bin_str = int(bin_str, 2) + int("1", 2)
        bin_str = str(bin(bin_str))[2:]

    return bin_str


def bintodec(line):

    dec = int(line[0])*(2**(len(line)-1))*(-1)

    for i in range(1, len(line)):

        dec = dec+(int(line[i])*(2**((len(line)-1)-i)))
    return dec


def S_type(line):
    opcode = line[-7:]

    funct3 = line[-15:-12]

    rs1 = line[-20:-15]
    rs2 = line[-25:-20]

    imm = line[-12:-7]+line[-32:-25]

    s = sext(imm, 32)
    mem = register_value[Address_Register[rs1]] + bintodec(sext(imm, 32))

    data_memory[mem] = register_value[Address_Register[rs2]]

def B_type(line):
    opcode = line[-7:]
    imm=line[0]+line[-8]+line[1:7]+line[-12:-7]
    func3=line[-15:-12]
    rs1=line[-20:-15]
    rs2=line[-25:-20]
    
B_type("00001100111101101100010001100011")
appendReg()
