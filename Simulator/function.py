import os
from constants import *

class AssemblerException(Exception):
    pass

def appendReg(output_file):

    if firstRun[0]:
        firstRun[0] = False

        try:
            os.remove(output_file)

        except FileNotFoundError:
            pass


    s = str(program_counter[0]) + ' '

    for k, v in register_value.items():
        s += str(v) + ' '

    with open(output_file, 'a') as f:
        f.write(s+'\n')


def appendDataMemory(output_file):

    if firstRun[0]:
        firstRun[0] = False

        try:
            os.remove(output_file)

        except FileNotFoundError:
            pass

    memory_keys = list( data_memory.keys() )
    memory_keys.sort()

    for memory_key in memory_keys:
        with open(output_file, 'a') as f:
            f.write( data_memory[memory_key] + "\n" )


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

 
def U_type(line): 
    opcode = line[25 : 31 + 1]
    rd_addr = line[ 20 : 24 + 1 ]
    imm = line[0 : 19 + 1] # MSB is at Python Index 0

    reg_name = Address_Register[rd_addr]

    bin_val = imm + 12 * "0"
    int_val = bintodec(bin_val)

    # lui
    if (opcode == "0110111"):
        register_value[reg_name] = int_val
        return

    # auipc
    elif (opcode == "0010111"):
        register_value[reg_name] = program_counter[0] + int_val


def J_type(line):
    opcode = line[25 : 31 + 1]
    rd_addr = line[ 20 : 24 + 1 ]

    temp_imm = line[0: 19 + 1]
    # imm[20|10 : 1|11|19 : 12]
    # index 0, 1 : 10, 11, 12 : 19
    
    # 20th bit of imm is at temp_imm[0] + 19:12 bit of imm is at temp_imm[-8:] + 11 bit of imm at temp_imm[11] + 10:1 bit of imm at temp[1:10]
    imm = temp_imm[0] + temp_imm[12:] + temp_imm[11] + temp_imm[1: 10 + 1] + "0"
    
    reg_name = Address_Register[rd_addr]
    register_value[reg_name] = program_counter[0] + 4

    temp_program_counter = program_counter[0] + bintodec(imm)

    bin_pc_str = bin(temp_program_counter)[2:]
    bin_pc_str = bin_pc_str[:-1] + "0"

    program_counter[0] = int(bin_pc_str, 2)

def B_type(line):
    opcode = line[-7:]
    imm=line[0]+line[-8]+line[1:7]+line[-12:-7]
    func3=line[-15:-12]
    rs1=line[-20:-15]
    rs2=line[-25:-20]
    
# B_type("00001100111101101100010001100011")
# appendReg()

def bits(n):
    lower=n % 100000
    return int(str(lower),2)


def R_TYPE(line):

    line=line[::-1]
    opcode=line[0:7]
    rd=line[7:12]
    funct3=line[12:15]
    rs1=line[15:20]
    rs2=line[20:25]
    funct7=line[25:32]
    reg_d=Address_Register[rd]
    reg_s1=Address_Register[rs1] 
    reg_s2=Address_Register[rs2]

    if (funct3 == "000"):

        if(funct7=="0000000"):
            # add function
            register_value[reg_d]=register_value[reg_s1]+register_value[reg_s2]
            regs[reg_d]=register_value[reg_d]
        elif(funct7=="0100000"):
            # sub function
            register_value[reg_d]=(register_value[reg_s1])-(register_value[reg_s2])
            regs[reg_d]=register_value[reg_d]
    
    elif (funct3 == "001"):

        #sll function
        reg1_bin=binary(register_value[reg_s1])
        reg2_bin=binary(register_value[reg_s2])
        shift_amount = bits(reg2_bin)
        reg1=str(reg1_bin)
        reg1=reg1[shift_amount:]+"0"*shift_amount
        register_value[reg_d]=bintodec(int(reg1))
        regs[reg_d]=register_value[reg_d]

    elif (funct3=="100"):

        #xor function
        register_value[reg_d]=register_value[reg_s1]^register_value[reg_s2]
        regs[reg_d]=register_value[reg_d]
    
    elif (funct3=="110"):

        #or function
        register_value[reg_d]=register_value[reg_s1]|register_value[reg_s2]
        regs[reg_d]=register_value[reg_d]
    
    elif(funct3=="111"):

        #and function
        register_value[reg_d]=register_value[reg_s1]&register_value[reg_s2]
        regs[reg_d]=register_value[reg_d]
    
    elif (funct3=="101"):

        #srl function
        reg1_bin=binary(register_value[reg_s1])
        reg2_bin=binary(register_value[reg_s2])
        shift_amount = bits(reg2_bin)
        reg1=str(reg1_bin)
        reg1="0"*(shift_amount)+reg1[:-shift_amount]
        register_value[reg_d]=bintodec(int(reg1))
        regs[reg_d]=register_value[reg_d]
    
    elif (funct3=="010"):

        #slt function
        if(register_value[reg_s2] > register_value[reg_s1]) :
            register_value[reg_d]=1
            regs[reg_d]=register_value[reg_d]
        else :
            register_value[reg_d]=0
            regs[reg_d]=register_value[reg_d]

        


    elif (funct3=="011"):

        #sltu function

        if(abs(register_value[reg_s2]) > abs(register_value[reg_s1]) ):
            register_value[reg_d]=1
            regs[reg_d]=register_value[reg_d]
        else :
            register_value[reg_d]=0
            regs[reg_d]=register_value[reg_d]
