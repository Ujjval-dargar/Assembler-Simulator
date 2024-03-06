from constants import *

# creating a function for calculating 2's complement of a number

def binary(num, n):

    # converting a string number into its binary number

    bin_str = str(bin(abs(int(num))))[2:] 

    # finding the length of the binary number

    l = len(bin_str)  

    #raising error if the binary representation of number is more than n bits long

    if (l > n or int(num) > 2**(n-1)-1 or int(num) < -2**(n-1)):            
        raise Exception("Invalid ")

    # appending leading zeros to the start of the string

    if (int(num) >= 0):
        bin_str = "0" * (n-l) + bin_str

    #for negative numbers
        
    else:

        bin_str = "0" * (n-l) + bin_str

        #converting binary string into list 

        bin_str = list(bin_str)

        #calculating  two's complement by flipping all the bits and adding one
        
        for i in range(len(bin_str)):

            if (bin_str[i] == '1'):
                bin_str[i] = '0'

            else:
                bin_str[i] = '1'

        bin_str = ''.join(bin_str)

        bin_str = int(bin_str, 2) + int("1", 2)

        bin_str = str(bin(bin_str))[2:]

    return bin_str


def S_Type( operands_lst, mnemonicInfo):

    if operands_lst[-1].count('(')!=1 or operands_lst[-1].count(')')!=1:
        raise Exception("Invalid operand")
    
    flag=False
    if ("zero" in operands_lst[-1]):
        flag=True

    if (operands_lst[-1][-1]!=')'):
        raise Exception("Invalid operand")
    if flag:
        if (operands_lst[-1][-6]!='('):
            raise Exception("Invalid operand")
    else:
        if (operands_lst[-1][-4]!='('):
            raise Exception("Invalid operand")
    
    operands_lst = " ".join(operands_lst).replace(
        "(", " ").replace(")", " ").split()

    if len(operands_lst) != len(mnemonicInfo["textSyntax"]):
        raise Exception("Invalid instruction: Missing operands")

    t=operands_lst[1].replace('-','')
    if (operands_lst[0] not in Register_Address or operands_lst[2] not in Register_Address or t.isnumeric() == False):
        raise Exception("Invalid operand")

    imm = binary(operands_lst[1], 12)

    bin_line = imm[:7] +" "+ Register_Address[operands_lst[0]] +" "+ \
        Register_Address[operands_lst[2]]+" " + \
        mnemonicInfo["funct3"]+" "+imm[7:]+" "+mnemonicInfo["opcode"]
    
    return bin_line

def U_Type( operands_lst, mnemonicInfo):

    if len(operands_lst) != 2:
        raise Exception("Invalid Instruction: Incorrect operands")
    
    t=operands_lst[1].replace('-','')
    if (operands_lst[0] not in Register_Address) or (t.isnumeric()==False):
        raise Exception("Invalid instruction: wrong operands given")
    
    rd, imm = operands_lst

    # Checking for validity
    if rd not in Register_Address:
        raise Exception("Invalid operand")
    
    bin_rd = Register_Address[rd]

    # Raises error if incorrect immediate
    # 32-bit immediate with no padding bits 
    # binary() returns MSB at 0-index but we want MSB at 31-index
    bin_imm = binary(imm, 32)[::-1]

    # We use only upper 20 bits of 32-bit immediate, discarding lower 12 bits
    return bin_imm[32:11:-1] + bin_rd + mnemonicInfo["opcode"]
    

def J_Type(operands_lst, mnemonicInfo):

    if len(operands_lst) != 2:
        raise Exception("Invalid Instruction: Incorrect operands")
    
    t=operands_lst[1].replace('-','')
    if (operands_lst[0] not in Register_Address) or (t.isnumeric()==False):
        raise Exception("Invalid instruction: wrong operands given")
    
    rd, imm = operands_lst

    # Checking for validity
    if rd not in Register_Address:
        raise Exception("Invalid operand")
    
    bin_rd = Register_Address[rd]

    # Raises error if incorrect immediate
    # 32-bit immediate +  1 padding bit (sign-extension) = 33 bits
    # binary() returns MSB at 0-index but we want MSB at 31-index
    bin_imm = binary(imm, 33)[::-1] 

    return bin_imm[20] + bin_imm[10:0:-1] + bin_imm[11] + bin_imm[19:11:-1] + bin_rd + mnemonicInfo["opcode"]

def B_Type(operands_lst, mnemonicInfo):

    if len(operands_lst)!=len(mnemonicInfo["textSyntax"]):
        raise Exception("Invalid instruction: invalid number of operands")

    t=operands_lst[2].replace('-','')
    if (operands_lst[0] not in Register_Address) or (operands_lst[1] not in Register_Address) or (t.isnumeric()==False):
        raise Exception("Invalid instruction: wrong operands given")
    
    
    #Making binary conversion of B-Type instructions
    binline=mnemonicInfo["opcode"]
    
    imm = binary(operands_lst[2],12)

    binline=imm[7:]+binline
    binline=mnemonicInfo["funct3"]+binline
    binline=Register_Address[operands_lst[0]]+binline
    binline=Register_Address[operands_lst[1]]+binline
    binline=imm[:7]+binline

    return binline


def R_Type(operands_lst,mnemonicInfo):

    if len(operands_lst) != len(mnemonicInfo["textSyntax"]):
        raise  Exception("Invalid instruction: Invalid number of operands")
    
    for i in operands_lst:

        if (i not in Register_Address):
            raise Exception ("Invalid instruction: invalid register name given")
    
    
    bin_line = (mnemonicInfo["funct7"] + Register_Address[operands_lst[2]] + Register_Address[operands_lst[1]]+mnemonicInfo["funct3"]+ Register_Address[operands_lst[0]]+mnemonicInfo["opcode"])
    return bin_line 


def I_Type (mnemonic,operands_lst,mnemonicInfo):
    if mnemonic=='lw':
        if operands_lst[-1].count('(')!=1 or operands_lst[-1].count(')')!=1:
            raise Exception("Invalid operand")
    
        flag=False
        if ("zero" in operands_lst[-1]):
            flag=True

        if (operands_lst[-1][-1]!=')'):
            raise Exception("Invalid operand")
        if flag:
            if (operands_lst[-1][-6]!='('):
                raise Exception("Invalid operand")
        else:
            if (operands_lst[-1][-4]!='('):
                raise Exception("Invalid operand")
        
        operands_lst = " ".join(operands_lst).replace(
            "(", " ").replace(")", " ").split()
    
    if len(operands_lst)!=len(mnemonicInfo["textSyntax"]):
        raise Exception("Invalid instruction: invalid number of operands")
    
    if mnemonic=='lw':
        t=operands_lst[1].replace('-','')

        if (operands_lst[0] not in Register_Address) or (operands_lst[2] not in Register_Address) or (t.isnumeric()==False):
            raise Exception("Invalid instruction: wrong operands given")
        
        imme=binary(operands_lst[1],12)

        bin_line= (imme+Register_Address[operands_lst[2]]+mnemonicInfo["funct3"]+Register_Address[operands_lst[0]]+mnemonicInfo["opcode"])

    else:
        t=operands_lst[2].replace('-','')

        if (operands_lst[0] not in Register_Address) or (operands_lst[1] not in Register_Address) or (t.isnumeric()==False):
            raise Exception("Invalid instruction: wrong operands given")
    
        imme=binary(operands_lst[2],12)

        bin_line= (imme+Register_Address[operands_lst[1]]+mnemonicInfo["funct3"]+Register_Address[operands_lst[0]]+mnemonicInfo["opcode"])
    
    return bin_line
