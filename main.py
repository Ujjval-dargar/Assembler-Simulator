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


        # Check for labels of following two types (input):
        # "<label>: <opcode> <operand>, <operand>, ..."
        # "<label>:<opcode> <operand>, <operand>, ..."

        # Convert to function that returns processed label line
        if ":" in line:
            colonIndex = line.index( ":" )

            # Check if there is space in between
            possibleLabel = line[ : colonIndex ] # Exclude colon

            if  has_space(possibleLabel):
                raise Exception("Invalid Instruction: Label has space in between")

            if possibleLabel in labels_dict:
                raise Exception("Invalid instruction: Multiple labels defined")

            # Output: "<opcode> <operand>, <operand>, ..."
            line = line[colonIndex + 1: ] # Discard label and colon
            line = line.lstrip() # Get rid of leading whitespace

            labels_dict[ possibleLabel ] = program_counter

        if line == "beq zero,zero,0x00000000":
          halt_found = True
          break

        intermediate_file.write(line)
        program_counter += 1 # Each instruction is stored at one memory location


# Preliminary error handling
if ( not (halt_found and program_counter < 64) ):
    raise Exception("Virtual Halt missing or not used as last instruction")