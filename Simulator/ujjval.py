def S_type(line):
    opcode=line[0:6+1]
    imm=line[7:11+1]+line[25:31+1]
    rs1=line[15:19+1]
    rs2=line[20:25+1]

    