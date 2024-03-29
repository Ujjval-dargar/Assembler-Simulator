from constants import *

def sext(line,bits):
    if line[0]==0:
        line=(bits-len(line))*'0'+line
    else:
        line=(bits-len(line))*'1'+line
    return line


def S_type(line):
    opcode=line[-7:]
    imm=line[7:11+1]+line[25:31+1]
    rs1=line[15:19+1]
    rs2=line[20:25+1]
    mem=register_value[Address_Register[rs1]]+sext(imm,32)
    data_memory[mem]=register_value[Address_Register[rs2]]