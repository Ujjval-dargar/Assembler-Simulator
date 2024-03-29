MNEMONICS_DICT = {

    # R-TYPE MNEMONICS
    "add": {
        "type": "R",
        "funct3": "000",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "sub": {
        "type": "R",
        "funct3": "000",
        "funct7": "0100000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "sll": {
        "type": "R",
        "funct3": "001",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "slt": {
        "type": "R",
        "funct3": "010",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]

    },

    "sltu": {
        "type": "R",
        "funct3": "011",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "xor": {
        "type": "R",
        "funct3": "100",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "srl": {
        "type": "R",
        "funct3": "101",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "or": {
        "type": "R",
        "funct3": "110",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    "and": {
        "type": "R",
        "funct3": "111",
        "funct7": "0000000",
        "opcode": "0110011",
        "textSyntax": ["REG", "REG", "REG"]
    },

    # I-TYPE MNEMONICS
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

    # U-TYPE MNEMONICS
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

    # J-TYPE MNEMONICS
    "jal": {
        "type": "J",
        "opcode": "1101111",

        "funct3": None,
        "funct7": None,

        "textSyntax": ["REG", "IMM"]

    },

    # S-TYPE MNEMONICS
    "sw": {
        "type": "S",
        "opcode": "0100011",
        "funct3": "010",
        "funct7": None,
        "textSyntax": ["REG", "IMM", "REG"]
    },

    # B-TYPE MNEMONICS
    "beq": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "000",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "bne": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "001",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "blt": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "100",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "bge": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "101",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "bltu": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "110",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    },

    "bgeu": {
        "type": "B",
        "opcode": "1100011",
        "funct3": "111",
        "funct7": None,
        "textSyntax": ["REG", "REG", "IMM"]
    }

}


OPCODE_DICT = {'0110011': {'0110011': {'type': 'R', 'funct3': '111', 'funct7': '0000000', 'textSyntax': ['REG', 'REG', 'REG'], 'mnemonic': 'and'}}, '0000011': {'0000011': {'type': 'I', 'funct3': '010', 'funct7': None, 'textSyntax': ['REG', 'REG', 'IMM'], 'mnemonic': 'lw'}}, '0010011': {'0010011': {'type': 'I', 'funct3': '011', 'funct7': None, 'textSyntax': ['REG', 'REG', 'IMM'], 'mnemonic': 'sltiu'}}, '1100111': {'1100111': {'type': 'I', 'funct3': '000', 'funct7': None, 'textSyntax': ['REG', 'REG', 'IMM'], 'mnemonic': 'jalr'}}, '0010111': {'0010111': {'type': 'U', 'funct3': None, 'funct7': None, 'textSyntax': ['REG', 'IMM'], 'mnemonic': 'auipc'}}, '0110111': {'0110111': {'type': 'U', 'funct3': None, 'funct7': None, 'textSyntax': ['REG', 'IMM'], 'mnemonic': 'lui'}}, '1101111': {'1101111': {'type': 'J', 'funct3': None, 'funct7': None, 'textSyntax': ['REG', 'IMM'], 'mnemonic': 'jal'}}, '0100011': {'0100011': {'type': 'S', 'funct3': '010', 'funct7': None, 'textSyntax': ['REG', 'IMM', 'REG'], 'mnemonic': 'sw'}}, '1100011': {'1100011': {'type': 'B', 'funct3': '111', 'funct7': None, 'textSyntax': ['REG', 'REG', 'IMM'], 'mnemonic': 'bgeu'}}}

def generate_dict():
    for mnemonic, mnemonic_dict in MNEMONICS_DICT.items():
        opcode_str = mnemonic_dict["opcode"]

        mnemonic_dict.pop("opcode")
        mnemonic_dict["mnemonic"] = mnemonic

        new_dict = { opcode_str :  mnemonic_dict  }
        OPCODE_DICT[opcode_str] = new_dict

generate_dict()
print(OPCODE_DICT)


Address_Register = {

    '00000': 'zero',
    '00001':  'ra',
    '00010':  'sp',
    '00011':  'gp',
    '00100':  'tp',
    '00101':  't0',
    '00110':  't1',
    '00111':  't2',
    '01000':  's0',
    '01000':  'fp',
    '01001':  's1',
    '01010':  'a0',
    '01011':  'a1',
    '01100':  'a2',
    '01101':  'a3',
    '01110':  'a4',
    '01111':  'a5',
    '10000':  'a6',
    '10001':  'a7',
    '10010':  's2',
    '10011':  's3',
    '10100':  's4',
    '10101':  's5',
    '10110':  's6',
    '10111':  's7',
    '11000':  's8',
    '11001':  's9',
    '11010': 's10',
    '11011': 's11',
    '11100':  't3',
    '11101':  't4',
    '11110':  't5',
    '11111':  't6'

}

