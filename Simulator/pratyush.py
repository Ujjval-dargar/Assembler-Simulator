from constants import *
from Simulator import regs

# 32-bit line, .strip()
# line.reverse()
def U_type(line): 
    opcode = line[0:6+1]
    rd = line[7:11 +1]
    imm = line[12:31 + 1]



