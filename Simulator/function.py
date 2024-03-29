from constants import * 


def sext(line, bits):
    if line[0] == '0':
        line = (bits-len(line))*'0'+line
    else:
        line = (bits-len(line))*'1'+line
    return line

def bintodec(line):
    dec=int(line[0])*(2**(len(line)-1))*(-1)
    for i in range(1,len(line)):
        dec=dec+(int(line[i])*(2**((len(line)-1)-i)))
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
    imm=line[-9:-13:-1]+line[-26:-32:-1]+line[-1]+line[-32]
    func3=line[-15:-12]
    rs1=line[-20:-15]
    rs2=line[-25:-20]
    
B_type("00001100111101101100010001100011")
#"0000 1100 1111 0110 1100 0100 0110 0011"

# ins = "00000010011000010010000000100011"
# # ins="0000 0010 0110 00010 010 00000 0100011"
# print(ins)
# S_type(ins)
