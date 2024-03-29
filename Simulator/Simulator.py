import sys
from constants import *
from function import *

input = sys.argv[-2]
output = sys.argv[-1]

with open(input) as input_file:

    for line in input_file:
        line = line.strip()

        opcode = line[-7:]
        instruction_type = Opcode_type[opcode]

        if instruction_type == "R":
            # R_type(line)
            pass
        elif instruction_type == "I":
            # I_type(line)
            pass
        
        elif instruction_type == "S":
            S_type(line)

        elif instruction_type == "B":
            B_type(line)

        elif instruction_type == "U":
            U_type(line)

        elif instruction_type == "J":
            J_type(line)

        appendReg(output)