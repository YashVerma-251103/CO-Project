# ask if the valid checks are required?
# arguement instruction needs to be sliced accordingly

import numpy
import sys
input_file=sys.argv[1]
output_file=sys.argv[2]



def number_convert(number,Format=False): #False for int to binary and true for binary to int
    if (Format):
        pass
    else:
        Binary_number=numpy.binary_repr(number, width=32)
        return Binary_number # will be returned as a string

# R type functions
def add(rs1,rs2,rd):
    global reg_codes
    # give a max condition! for overflow...
    reg_codes[rd]=reg_codes[rs1]+reg_codes[rs2]
    return
def sub(rs1,rs2,rd):
    if (rs1=="00000"):
        # have to make the 2's complement of rs2 and store it in rd
        pass
    else:
        pass
def sll(rs1,rs2,rd):
    pass
def slt(rs1,rs2,rd):
    pass
def sltu(rs1,rs2,rd):
    pass
def xor(rs1,rs2,rd):
    pass
def srl(rs1,rs2,rd):
    pass
def OR(rs1,rs2,rd):
    pass
def AND(rs1,rs2,rd):
    pass

# I type functions
def lw(instruction):
    pass
def addi(rs1,rd,imm):
    pass
def sltiu(rs1,rd,imm):
    pass
def jalr(instruction):
    pass

# S type functions
def sw(instruction):
    pass

# B type functions
def beq(rs1,rs2,imm):
    pass
def bne(rs1,rs2,imm):
    pass
def blt(rs1,rs2,imm):
    pass
def bge(rs1,rs2,imm):
    pass
def bltu(rs1,rs2,imm):
    pass
def bgeu(rs1,rs2,imm):
    pass

# U type functions
def lui(instruction):
    pass
def auipc(instruction):
    pass

# J type functions
def jal(instruction):
    pass


Opcodes={
    # R Type functions
    "0110011":{
        "000":{"0000000":add,"0100000":sub},
        "001":sll,
        "010":slt,
        "011":sltu,
        "100":xor,
        "101":srl,
        "110":OR,
        "111":AND
        },
    
    # I Type functions
    "0000011":lw,
    "0010011":{"000":addi,"011":sltiu},
    "1100111":jalr,
    
    # S Type functions
    "0100011":sw,
    
    # B Type functions
    "1100011":{
        "000":beq,
        "001":bne,
        "100":blt,
        "101":bge,
        "110":bltu,
        "111":bgeu,
    },
    
    # U Type functions
    "0110111":lui,
    "0010111":auipc,
    
    # J Type functions
    "1101111":jal    
    }

reg_codes = { # format of save: binary code : value 
            # i dont know if i should keep this in string to maintain binary format or in integer to maintain decimal numbers
             "00000"  : "0" ,  # "zero"  =  x0   
             "00001"  : "0" ,  # "ra"    =  x1
             "00010"  : "0" ,  # "sp"    =  x2
             "00011"  : "0" ,  # "gp"    =  x3
             "00100"  : "0" ,  # "tp"    =  x4
             "00101"  : "0" ,  # "t0"    =  x5
             "00110"  : "0" ,  # "t1"    =  x6
             "00111"  : "0" ,  # "t2"    =  x7
             "01000"  : "0" ,  # "s0"    =  x8
             "01000"  : "0" ,  # "fp"    =  x8
             "01001"  : "0" ,  # "s1"    =  x9
             "01010"  : "0" ,  # "a0"    =  x10
             "01011"  : "0" ,  # "a1"    =  x11
             "01100"  : "0" ,  # "a2"    =  x12
             "01101"  : "0" ,  # "a3"    =  x13
             "01110"  : "0" ,  # "a4"    =  x14
             "01111"  : "0" ,  # "a5"    =  x15
             "10000"  : "0" ,  # "a6"    =  x16
             "10001"  : "0" ,  # "a7"    =  x17
             "10010"  : "0" ,  # "s2"    =  x18
             "10011"  : "0" ,  # "s3"    =  x19
             "10100"  : "0" ,  # "s4"    =  x20
             "10101"  : "0" ,  # "s5"    =  x21
             "10110"  : "0" ,  # "s6"    =  x22
             "10111"  : "0" ,  # "s7"    =  x23
             "11000"  : "0" ,  # "s8"    =  x24
             "11001"  : "0" ,  # "s9"    =  x25
             "11010"  : "0" ,  # "s10"   =  x26
             "11011"  : "0" ,  # "s11"   =  x27
             "11100"  : "0" ,  # "t3"    =  x28
             "11101"  : "0" ,  # "t4"    =  x29
             "11110"  : "0" ,  # "t5"    =  x30
             "11111"  : "0" ,  # "t6"    =  x31
}


data_memory={
   "00010000":"00000000000000000000000000000000", # 0x00010000:0b00000000000000000000000000000000,
   "00010004":"00000000000000000000000000000000", # 0x00010004:0b00000000000000000000000000000000,
   "00010008":"00000000000000000000000000000000", # 0x00010008:0b00000000000000000000000000000000,
   "0001000c":"00000000000000000000000000000000", # 0x0001000c:0b00000000000000000000000000000000,
   "00010010":"00000000000000000000000000000000", # 0x00010010:0b00000000000000000000000000000000,
   "00010014":"00000000000000000000000000000000", # 0x00010014:0b00000000000000000000000000000000,
   "00010018":"00000000000000000000000000000000", # 0x00010018:0b00000000000000000000000000000000,
   "0001001c":"00000000000000000000000000000000", # 0x0001001c:0b00000000000000000000000000000000,
   "00010020":"00000000000000000000000000000000", # 0x00010020:0b00000000000000000000000000000000,
   "00010024":"00000000000000000000000000000000", # 0x00010024:0b00000000000000000000000000000000,
   "00010028":"00000000000000000000000000000000", # 0x00010028:0b00000000000000000000000000000000,
   "0001002c":"00000000000000000000000000000000", # 0x0001002c:0b00000000000000000000000000000000,
   "00010030":"00000000000000000000000000000000", # 0x00010030:0b00000000000000000000000000000000,
   "00010034":"00000000000000000000000000000000", # 0x00010034:0b00000000000000000000000000000000,
   "00010038":"00000000000000000000000000000000", # 0x00010038:0b00000000000000000000000000000000,
   "0001003c":"00000000000000000000000000000000", # 0x0001003c:0b00000000000000000000000000000000,
   "00010040":"00000000000000000000000000000000", # 0x00010040:0b00000000000000000000000000000000,
   "00010044":"00000000000000000000000000000000", # 0x00010044:0b00000000000000000000000000000000,
   "00010048":"00000000000000000000000000000000", # 0x00010048:0b00000000000000000000000000000000,
   "0001004c":"00000000000000000000000000000000", # 0x0001004c:0b00000000000000000000000000000000,
   "00010050":"00000000000000000000000000000000", # 0x00010050:0b00000000000000000000000000000000,
   "00010054":"00000000000000000000000000000000", # 0x00010054:0b00000000000000000000000000000000,
   "00010058":"00000000000000000000000000000000", # 0x00010058:0b00000000000000000000000000000000,
   "0001005c":"00000000000000000000000000000000", # 0x0001005c:0b00000000000000000000000000000000,
   "00010060":"00000000000000000000000000000000", # 0x00010060:0b00000000000000000000000000000000,
   "00010064":"00000000000000000000000000000000", # 0x00010064:0b00000000000000000000000000000000,
   "00010068":"00000000000000000000000000000000", # 0x00010068:0b00000000000000000000000000000000,
   "0001006c":"00000000000000000000000000000000", # 0x0001006c:0b00000000000000000000000000000000,
   "00010070":"00000000000000000000000000000000", # 0x00010070:0b00000000000000000000000000000000,
   "00010074":"00000000000000000000000000000000", # 0x00010074:0b00000000000000000000000000000000,
   "00010078":"00000000000000000000000000000000", # 0x00010078:0b00000000000000000000000000000000,
   "0001007c":"00000000000000000000000000000000"  # 0x0001007c:0b00000000000000000000000000000000
}


with open(input_file,"r") as file:
    data=file.readlines()

for program_counter in range(0,(len(data))):
    rs1,rs2,rd,valid_imm=False,False,False,False
    instruction=data[program_counter].rstrip()
    opcode=instruction[-7:] # got the opcode of the instruction
    if opcode=="0110011": # r type instructions given
        function_call=instruction[-15:-12]
        if function_call in Opcodes["0110011"].keys():
            rs1=instruction[-20:-15]
            rs2=instruction[-25:-20]
            rd=instruction[-12:-7]
            if function_call=="000":
                f7=instruction[-32:-25]
                Opcodes["0110011"]["000"][f7](rs1,rs2,rd)
            else:
                Opcodes["0110011"][function_call](rs1,rs2,rd)    
    elif opcode=="0010011": # addi and sltui
        function_call=instruction[-15:-12]
        rs1=instruction[-20:-15]
        rd=instruction[-12:-7]
        imm=instruction[-32:-20]
        Opcodes["0010011"][function_call](rs1,rd,imm)
    elif opcode=="1100011": # b type instructions were given
        function_call=instruction[-15:-12]
        rs1=instruction[-20:-15]
        rs2=instruction[-25:-20]
        imm=instruction[-32]+instruction[-8]+instruction[-31:-25]+instruction[-12:-8]
        Opcodes["1100011"][function_call](rs1,rs2,imm)
    else: #everything else
        Opcodes[opcode](instruction)
        
    

