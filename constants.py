Register_Address = {

    'zero': '00000',
    'ra': '00001',
    'sp': '00010',
    'gp': '00011',
    'tp': '00100',
    't0': '00101',
    't1': '00110',
    't2': '00111',
    's0': '01000',
    'fp': '01000',
    's1': '01001',
    'a0': '01010',
    'a1': '01011',
    'a2': '01100',
    'a3': '01101',
    'a4': '01110',
    'a5': '01111',
    'a6': '10000',
    'a7': '10001',
    's2': '10010',
    's3': '10011',
    's4': '10100',
    's5': '10101',
    's6': '10110',
    's7': '10111',
    's8': '11000',
    's9': '11001',
    's10': '11010',
    's11': '11011',
    't3': '11100',
    't4': '11101',
    't5': '11110',
    't6': '11111'

}

MNEMONICS_DICT = { 

    #R-TYPE MNEMONICS
	"add": {
        "type": "R",
        "funct3": "000",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "sub": {
        "type": "R",
        "funct3": "000",
        "funct7": "0100000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "sll": {
        "type": "R",
        "funct3": "001",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "slt": {
        "type": "R",
        "funct3": "010",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
        
    },

    "sltu": {
        "type": "R",
        "funct3": "011",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "xor": {
        "type": "R",
        "funct3": "100",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "srl": {
        "type": "R",
        "funct3": "101",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "or": {
        "type": "R",
        "funct3": "110",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "and": {
        "type": "R",
        "funct3": "111",
        "funct7": "0000000",
        "opcode":"0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    #I-TYPE MNEMONICS
    "lw": {
        "type": "I",
        "opcode": "0000011",
        "funct3": "010",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "addi": {
        "type": "I",
        "opcode": "0010011",
        "funct3": "000",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "sltiu": {
        "type": "I",
        "opcode": "0010011",
        "funct3": "011",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "jalr": {
        "type": "I",
        "opcode": "1100111",
        "funct3": "000",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    #U-TYPE MNEMONICS
    "auipc": {
        "type": "U",
        "opcode": "0010111",

        "funct3": None,
        "funct7": None,

        "textSyntax": ["REG", "IMM"]

    },

    "lui": {
        "type": "U",
        "opcode": "0110111",

        "funct3": None,
        "funct7": None,

        "textSyntax": ["REG", "IMM"]

    },

    #J-TYPE MNEMONICS
    "jal": {
        "type": "J",
        "opcode": "1101111",

        "funct3": None,
        "funct7": None,

        "textSyntax": ["REG", "IMM"]

    },

    #S-TYPE MNEMONICS
    "sw" : {
        "type" : "S",
        "opcode" : "0100011",
        "funct3" : "010",
        "funct7" : None,
        "textSyntax" : ["REG", "IMM", "REG"]
    },

    #B-TYPE MNEMONICS
    "beq" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "000" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    },

    "bne" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "001" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    },

    "blt" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "100" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    },

    "bge" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "101" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    },

    "bltu" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "110" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    },

    "bgeu" : {
        "type" : "B" ,
        "opcode" : "1100011",
        "funct3" : "111" ,
        "funct7" : None ,
        "textSyntax" : ["REG","REG","IMM"]
    }

}
