instructions = {
    'binary': {
        "move": 0x00,
        "add": 0x10,
        "addc": 0x20,
        "sub": 0x30,
        "and": 0x40,
        "or": 0x50,
        "xor": 0x60,
        "cmp": 0x70,
        "st": 0xA0,
        "ld": 0xB0,
        "ldc": 0xF0
    },
    'unary': {
        "not": 0x80,
        "neg": 0x84,
        "dec": 0x88,
        "inc": 0x8C,
        "shr": 0x90,
        "shla": 0x94,
        "shra": 0x98,
        "rol": 0x9C,
        "push": 0xC0,
        "pop": 0xC4,
        #    "stsp":	0xC8,un),  # mark 3 Architecture # Not needed as macro replacements done: Mick June 2018
        #    "ldsp":	0xCC,un),  # mark 3 Architecture
        # "ldsa": 0xC8,  # mark 4 architecture
        # "ldi": 0xD0,
    },

    'zero': {
        "pushall": 0xCE,  # mark 4 architecture
        "popall": 0xCF,  # mark 4 architecture
        "rts": 0xD7,

        # interrupts
        "ioi": 0xD8,
        "rti": 0xD9,
        "crc": 0xDA,
        "halt": 0xD4,
        "wait": 0xD5,
    },
    # 'spmove': {
    #     "addsp": 0xCC,  # mark 4 architecture
    #     "setsp": 0xCD,  # mark 4 architecture
    # },
    'branch': {
        "jsr": 0xD6,
        # branches
        "beq": 0xE0,
        "bz": 0xE0,
        "bne": 0xE1,
        "bnz": 0xE1,
        "bhs": 0xE2,
        "bcs": 0xE2,
        "blo": 0xE3,
        "bcc": 0xE3,
        "bmi": 0xE4,
        "bpl": 0xE5,
        "bvs": 0xE6,
        "bvc": 0xE7,
        "bhi": 0xE8,
        "bls": 0xE9,
        "bge": 0xEA,
        "blt": 0xEB,
        "bgt": 0xEC,
        "ble": 0xED,
        "br": 0xEE,
        # "nop": 0xEF,
        # "lchk": 0,
    },
    # 'osix': {
    #     "osix": 0xDB,
    # }
    'dc':{'dc':0},
    'ldi':{'ldi':0xd0}

}
