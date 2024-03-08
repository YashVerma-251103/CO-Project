#Steps to do
#create a list of opp codes 
#create a Pattern for registers
#create a patter for memory
#work in out in a file handler.


# R - type Functions
def add(rs1,rs2,rd):
    value=isa_codes["add"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["add"]["f3"]+reg_codes[rd]+isa_codes["add"]["opcode"]
    return value
def sub(rs1,rs2,rd):
    value = isa_codes["sub"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sub"]["f3"]+reg_codes[rd]+isa_codes["sub"]["opcode"]
    return value
def sll(rs1,rs2,rd):
    value = isa_codes["sll"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sll"]["f3"]+reg_codes[rd]+isa_codes["sll"]["opcode"]
    return value
def slt(rs1,rs2,rd):
    value = isa_codes["slt"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["slt"]["f3"]+reg_codes[rd]+isa_codes["slt"]["opcode"]
    return value
def sltu(rs1,rs2,rd):
    value = isa_codes["sltu"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sltu"]["f3"]+reg_codes[rd]+isa_codes["sltu"]["opcode"]
    return value
def xor(rs1,rs2,rd):
    value = isa_codes["xor"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["xor"]["f3"]+reg_codes[rd]+isa_codes["xor"]["opcode"]
    return value
def srl(rs1,rs2,rd):
    value = isa_codes["srl"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["srl"]["f3"]+reg_codes[rd]+isa_codes["srl"]["opcode"]
    return value
def OR(rs1,rs2,rd): #This is or function
    value = isa_codes["or"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["or"]["f3"]+reg_codes[rd]+isa_codes["or"]["opcode"]
    return value
def AND(rs1,rs2,rd): #This is and function
    value = isa_codes["and"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["and"]["f3"]+reg_codes[rd]+isa_codes["and"]["opcode"]
    return value

# I - type Functions
def lw(imm,rs1,rd): #configure imm
    value=imm+reg_codes[rs1]+isa_codes["lw"]["f3"]+reg_codes[rd]+isa_codes["lw"]["opcode"]
    return value
def addi(imm,rs1,rd): #configure imm
    value=imm+reg_codes[rs1]+isa_codes["addi"]["f3"]+reg_codes[rd]+isa_codes["addi"]["opcode"]
    return value
def sltiu(imm,rs1,rd): #configure imm
    value=imm+reg_codes[rs1]+isa_codes["sltiu"]["f3"]+reg_codes[rd]+isa_codes["sltiu"]["opcode"]
    return value
def jalr(imm,rs1,rd): #configure imm
    value=imm+reg_codes[rs1]+isa_codes["jalr"]["f3"]+reg_codes[rd]+isa_codes["jalr"]["opcode"]
    return value

# S - type Functions
def sw(imm1,rs2,rs1,imm2): # configure imms   ||   imm1 --> 11:5   ||  imm2 --> 4:0 
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sw"]["f3"]+imm2+isa_codes["sw"]["opcode"]
    return value

# U - type
def lui(imm,rd): #configure imm  ||  31:12
    value=imm+reg_codes[rd]+isa_codes["lui"]["opcode"]
    return value
def auipc(imm,rd): #configure imm  ||  31:12
    value=imm+reg_codes[rd]+isa_codes["auipc"]["opcode"]
    return value

# B - type      # configure imms   ||   imm1 --> 12|10:5   ||  imm2 --> 4:1|11
def beq(imm1,rs1,rs2,imm2):
     value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["beq"]["f3"]+imm2+isa_codes["beq"]["opcode"]
     return value
def bne(rs1,rs2,imm1,imm2):
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bne"]["f3"]+imm2+isa_codes["bne"]["opcode"]
    return value
def blt(rs1,rs2,imm1,imm2):
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["blt"]["f3"]+imm2+isa_codes["blt"]["opcode"]
    return value
def bge(rs1,rs2,imm1,imm2):
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bge"]["f3"]+imm2+isa_codes["bge"]["opcode"]
    return value
def bltu(rs1,rs2,imm1,imm2):
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bltu"]["f3"]+imm2+isa_codes["bltu"]["opcode"]
    return value
def bgeu(rs1,rs2,imm1,imm2):
    value=imm1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bgeu"]["f3"]+imm2+isa_codes["bgeu"]["opcode"]
    return value

# J - type     #configure imm  ||  20|10:1|11|19:12
def jal(imm,rd):
    value=imm+reg_codes[rd]+isa_codes["jal"]["opcode"]
    return value

reg_codes = { 
              "R0" : "00000",
              "R1" : "00001",
              "R2" : "00010" , 
              "R3" : "00011" ,
              "R4" : "00100" ,
              "R5" : "00101" ,
              "R6" : "00110" ,
              "R7" : "00111" ,
              "R8" : "01000" ,
              "R9" : "01001" ,
             "R10" : "01010" ,
             "R11" : "01011" ,
             "R12" : "01100" ,
             "R13" : "01101" ,
             "R14" : "01110" ,
             "R15" : "01111" ,
             "R16" : "10000" ,
             "R17" : "10001" ,
             "R18" : "10010" ,
             "R19" : "10011" ,
             "R20" : "10100" ,
             "R21" : "10101" ,
             "R22" : "10110" ,
             "R23" : "10111" ,
             "R24" : "11000" ,
             "R25" : "11001" ,
             "R26" : "11010" ,
             "R27" : "11011" ,
             "R28" : "11100" ,
             "R29" : "11101" ,
             "R30" : "11110" ,
             "R31" : "11111" ,
             
             "FLAGS" : "111"}
isa_codes={
    # r type
     "add":{"opcode":"0110011","type":"r","f3":"000","f7":"0000000"},
     "sub":{"opcode":"0110011","type":"r","f3":"000","f7":"0100000"},
     "sll":{"opcode":"0110011","type":"r","f3":"001","f7":"0000000"},
     "slt":{"opcode":"0110011","type":"r","f3":"010","f7":"0000000"},
    "sltu":{"opcode":"0110011","type":"r","f3":"011","f7":"0000000"},
     "xor":{"opcode":"0110011","type":"r","f3":"100","f7":"0000000"},
     "srl":{"opcode":"0110011","type":"r","f3":"101","f7":"0000000"},
      "or":{"opcode":"0110011","type":"r","f3":"110","f7":"0000000"},
     "and":{"opcode":"0110011","type":"r","f3":"111","f7":"0000000"},
    # i
       "lw":{"opcode":"0000011","type":"i","f3":"010"},
     "addi":{"opcode":"0010011","type":"i","f3":"000"},
    "sltiu":{"opcode":"0010011","type":"i","f3":"011"},
     "jalr":{"opcode":"1100111","type":"i","f3":"000"},
    #  s 
       "sw":{"opcode":"","type":"s","f3":""},
    # b
      "beq":{"opcode":"1100011","type":"b","f3":"000"},
      "bne":{"opcode":"1100011","type":"b","f3":"001"},
      "blt":{"opcode":"1100011","type":"b","f3":"100"},
      "bge":{"opcode":"1100011","type":"b","f3":"101"},
     "bltu":{"opcode":"1100011","type":"b","f3":"110"},
     "bgeu":{"opcode":"1100011","type":"b","f3":"111"},
    # u
      "lui":{"opcode":"0110111","type":"u"},
    "auipc":{"opcode":"0010111","type":"u"},
    # J
      "jal":{"opcode":"1101111","type":"j"},
    # bonus -- configure -- special cases
     "mul":{},
     "rst":{},
    "halt":{},
    "rvrs":{}
}

instructions=list(isa_codes.keys())
registers=list(reg_codes.keys())
