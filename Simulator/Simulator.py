import sys
from constants import *
from function import *

input = sys.argv[-2]
output = sys.argv[-1]

setupDataMem()

with open(input) as input_file:
    input_lines = input_file.readlines()


while True:
    line_num = program_counter[0] // 4
    line = input_lines[line_num].strip()

    if line == "":
        continue

    # Virtual Halt
    if line == "00000000000000000000000001100011":
        program_counter[0] += 4
        appendReg(output)

        break

    opcode = line[-7:]
    instruction_type = Opcode_type[opcode]

    print(line_num)

    if instruction_type == "R":
        R_type(line)
        program_counter[0] += 4

    elif instruction_type == "I":
        I_type(line)
        program_counter[0] += 4
    
    elif instruction_type == "S":
        S_type(line)
        program_counter[0] += 4

    elif instruction_type == "B":
        B_type(line)

    elif instruction_type == "U":
        U_type(line)
        program_counter[0] += 4

    elif instruction_type == "J":
        J_type(line)

    # Write registers to file
    appendReg(output)

# Write data memory to file
appendDataMemory(output)