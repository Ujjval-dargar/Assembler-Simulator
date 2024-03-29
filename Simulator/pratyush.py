from constants import *
from Simulator import regs, program_counter

# 32-bit line, .strip()
# line.reverse() NOT
# reg data 
def U_type(line): 
    opcode = line[25 : 31 + 1]
    rd_addr = line[ 20 : 24 + 1 ]
    imm = line[0: 19 + 1]

    reg_name = Address_Register[rd_addr]

    bin_val = imm + 12 * "0"
    int_val = two_complement(bin_val, 32)

    # lui
    if (opcode == "0110111"):
        regs[reg_name] = int_val
        return

    # auipc
    elif (opcode == "0010111"):
        regs[reg_name] = program_counter + int_val


def J_type(line):
    opcode = line[25 : 31 + 1]
    rd_addr = line[ 20 : 24 + 1 ]
    imm = line[0: 19 + 1]

    reg_name = Address_Register[rd_addr]

    regs[reg_name] = program_counter + 4

    temp_program_counter = program_counter + two_complement(imm)

    bin_pc_str = bin(temp_program_counter)[2:]
    bin_pc_str = bin_pc_str[:-1] + "0"

    program_counter = int(bin_pc_str, 2)

    

    






