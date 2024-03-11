import os
from constants import *
from functions import *
import sys

labels_dict = {}
halt_found = False
program_counter = -4
line_num=0

# Maintaning command-line arguements 
input = sys.argv[-2]
output = sys.argv[-1]

# Creating first pass function
def first_pass():
    global program_counter,line_num,halt_found,input,output

    with open(input, "r") as input_file, open("intermediate.txt", "w") as intermediate_file:

        for line in input_file:
            line_num+=1 #increasing line_num counter

            # If not a Blank line increase program counter
            if not line.isspace():
                program_counter+=4 # Each instruction is stored at 4 memory location

            # Removing leading and trailing whitespace
            # Input: "   <OPCODE> <operand>, <operand>, ..., <operand>    "
            # Output: "<opcode> <operand>, <operand>, ..., <operand>"
            line = line.strip()
            line = line.lower()

            # Check for labels of following two types (input):
            # Convert to function that returns processed label line
            if ":" in line:
                colonIndex = line.index( ":" )

                # Check if there is space in between
                possibleLabel = line[ : colonIndex ] # Exclude colon

                if possibleLabel.count(" ") != 0:
                    raise AssemblerException("Invalid Instruction: Label has space in between")

                if possibleLabel in labels_dict:
                    raise AssemblerException("Invalid instruction: Multiple labels defined")

                # Output: "<opcode> <operand>, <operand>, ..."
                line = line[colonIndex + 1: ] # Discard label and colon
                line = line.lstrip() # Get rid of leading whitespace

                # Maintaining Label Dictionary
                labels_dict[ possibleLabel ] = program_counter

            # Input: "<opcode> <operand>, <operand>, ..., <operand>"
            # Output: "<opcode> <operand> <operand>  ... <operand>"
            line = line.replace(",", " ")
            line = " ".join(line.split())


            intermediate_file.write(line+"\n")

            # Checking for halt variable
            halt_found = False
            
            if line == "beq zero zero 0":
                halt_found = True
                

    # Preliminary error handling
    if ( not (halt_found and program_counter < 64 * 4) ):
        raise AssemblerException("Virtual Halt missing or not used as last instruction")

# Creating Second pass funciton
def second_pass():
    global program_counter,line_num,input,output
    line_num=0
    program_counter = -4

    with open("intermediate.txt") as intermediate_file, open("intermediate2.txt", "w") as intermediate2_file:
        
        for line in intermediate_file:
            line_num+=1 # Increasing line_num counter

            if not line.isspace():
                program_counter+=4 # Each instruction is stored at 4 memory location

            #  Changing label name with appropriate label address
            for iter_label in labels_dict:
                if iter_label in line:
                    jump = labels_dict[iter_label]-program_counter
                    line = line.replace( iter_label, str( jump ) )

            # Creating intermediate-2 file
            intermediate2_file.write(line)

# Creating third pass function
def third_pass():
    global program_counter,line_num,input,output
    program_counter = -4
    line_num=0

    with open("intermediate2.txt") as intermediate_file2, open(output, "w") as output_file:

        for line in intermediate_file2:
            line_num+=1 # Increasing line_num counter

            if not line.isspace():
                program_counter+=4 # Each instruction is stored at 4 memory location

                # Split only at first space
                # Output : [ "opcode", "<operand> <operand> ..." ]
                tokens = line.split( maxsplit = 1 )

                if len(tokens) < 2:
                    raise AssemblerException("Invalid instruction: Missing opcode or no space between opcode and operands")

                mnemonic = tokens[0]
                operands_str = tokens[1]

                if '(' in operands_str:
                    operands_lst=operands_str.split(maxsplit=1)
                    operands_lst[-1]=operands_lst[-1].strip()
                else:
                    operands_lst = operands_str.split()

                if mnemonic not in MNEMONICS_DICT:
                    raise AssemblerException("Invalid instruction: Unknown mnemonic")

                # Get information about instruction
                mnemonicInfo = MNEMONICS_DICT[mnemonic]

                instructionType = mnemonicInfo[ "type" ]
            
                # Chaging asssembler code into binary code with proper functions made in functon.py
                if instructionType == "R":
                    line = R_Type(operands_lst, mnemonicInfo)

                elif instructionType == "I":
                    line = I_Type(mnemonic,operands_lst, mnemonicInfo)

                elif instructionType == "U":
                    line = U_Type(operands_lst, mnemonicInfo)

                elif instructionType == "B":
                    line = B_Type(operands_lst, mnemonicInfo)

                elif instructionType == "J":
                    line = J_Type(operands_lst, mnemonicInfo)

                elif instructionType == "S":
                    line = S_Type(operands_lst, mnemonicInfo)

                # Writing binary code into output.py
                output_file.write(line + "\n")

# __main__
try:
    first_pass()
    second_pass()
    third_pass()

    # To fix the extra blank line at end of output file
    f=open(output)
    txt=f.readlines();
    f.close()

    f=open(output,'w')
    f.writelines(txt[:-1])
    f.write(txt[-1].strip())
    f.close()

    # Removing error file
    try:
        os.remove("errors.txt")
    except:
        pass


except AssemblerException as err:
    
    msg = str(err)

    line =  f"Line number {line_num}: {msg}"
    print(line)
    
    with open("errors.txt", "w") as error_file:
        error_file.write( line )

    # Removing binary file
    try:
        os.remove(output)
    except:
        pass

try:
        
    os.remove("intermediate.txt")
    os.remove("intermediate2.txt")

except :
    pass    