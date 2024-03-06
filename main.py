from constants import *
from functions import *

labels_dict = {}
halt_found = False
program_counter = 0

with open("input.txt", "r") as input_file, open("intermediate.txt", "w") as intermediate_file:

      for line in input_file:

        # Blank line
        if line.isspace():
            continue

        # ~ Not blank ~

        # Removing leading and trailing whitespace
        # Input: "   <opcode> <operand>, <operand>, ..., <operand>    "
        # Output: "<opcode> <operand>, <operand>, ..., <operand>"
        line = line.strip()
        line = line.lower()


        # Check for labels of following two types (input):
        # "<label>: <opcode> <operand>, <operand>, ..."
        # "<label>:<opcode> <operand>, <operand>, ..."

        # Convert to function that returns processed label line
        if ":" in line:
            colonIndex = line.index( ":" )

            # Check if there is space in between
            possibleLabel = line[ : colonIndex ] # Exclude colon

            if possibleLabel.count(" ") != 0:
                raise Exception("Invalid Instruction: Label has space in between")

            if possibleLabel in labels_dict:
                raise Exception("Invalid instruction: Multiple labels defined")

            # Output: "<opcode> <operand>, <operand>, ..."
            line = line[colonIndex + 1: ] # Discard label and colon
            line = line.lstrip() # Get rid of leading whitespace

            labels_dict[ possibleLabel ] = program_counter

        line = line.replace(",", " ")
        line = " ".join(line.split())


        intermediate_file.write(line+"\n")
        program_counter += 4 # Each instruction is stored at 4 memory location

        if line == "beq zero zero 0":
          halt_found = True
          break

# Preliminary error handling
if ( not (halt_found and program_counter < 64) ):
    raise Exception("Virtual Halt missing or not used as last instruction")


# Second pass
program_counter = 0
with open("intermediate.txt") as intermediate_file, open("intermediate2.txt", "w") as intermediate2_file:
    
    for line in intermediate_file:

        label = ""

        for iter_label in labels_dict:
            if iter_label in line:
                jump = labels_dict[iter_label] - program_counter
                line = line.replace( iter_label, str( jump ) )

        intermediate2_file.write(line)
        program_counter += 4



# Third pass
program_counter = 0

with open("intermediate2.txt") as intermediate_file2, open("output.txt", "w") as output_file:

    for line in intermediate_file2:

        # Split only at first space
        # [ "opcode", "<operand> <operand> ..." ]
        tokens = line.split( maxsplit = 1 )

        if len(tokens) < 2:
            raise Exception("Invalid instruction: Missing opcode or no space between opcode and operands")

        mnemonic = tokens[0]
        operands_str = tokens[1]

        operands_lst = operands_str.split()

        if mnemonic not in MNEMONICS_DICT:
            raise Exception("Invalid instruction: Unknown mnemonic")

        # Get information about instruction
        mnemonicInfo = MNEMONICS_DICT[mnemonic]

        instructionType = mnemonicInfo[ "type" ]
       
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

        
        output_file.write(line + "\n")
        program_counter += 4

