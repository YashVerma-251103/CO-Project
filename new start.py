import numpy
import sys
IF=sys.argv[1] #Input File
OUT=sys.argv[2] #Output File

with open(IF,"r") as file: #Reading input file
    instructions=file.readlines()
total_instructions=len(instructions)
 
# Making Required Variables
Registers={
             "00000"  : "00000000000000000000000000000000" ,  
             "00001"  : "00000000000000000000000000000000" ,
             "00010"  : "00000000000000000000000000000000" ,
             "00011"  : "00000000000000000000000000000000" ,
             "00100"  : "00000000000000000000000000000000" ,
             "00101"  : "00000000000000000000000000000000" ,
             "00110"  : "00000000000000000000000000000000" ,
             "00111"  : "00000000000000000000000000000000" ,
             "01000"  : "00000000000000000000000000000000" ,
             "01000"  : "00000000000000000000000000000000" ,
             "01001"  : "00000000000000000000000000000000" ,
             "01010"  : "00000000000000000000000000000000" ,
             "01011"  : "00000000000000000000000000000000" ,
             "01100"  : "00000000000000000000000000000000" ,
             "01101"  : "00000000000000000000000000000000" ,
             "01110"  : "00000000000000000000000000000000" ,
             "01111"  : "00000000000000000000000000000000" ,
             "10000"  : "00000000000000000000000000000000" ,
             "10001"  : "00000000000000000000000000000000" ,
             "10010"  : "00000000000000000000000000000000" ,
             "10011"  : "00000000000000000000000000000000" ,
             "10100"  : "00000000000000000000000000000000" ,
             "10101"  : "00000000000000000000000000000000" ,
             "10110"  : "00000000000000000000000000000000" ,
             "10111"  : "00000000000000000000000000000000" ,
             "11000"  : "00000000000000000000000000000000" ,
             "11001"  : "00000000000000000000000000000000" ,
             "11010"  : "00000000000000000000000000000000" ,
             "11011"  : "00000000000000000000000000000000" ,
             "11100"  : "00000000000000000000000000000000" ,
             "11101"  : "00000000000000000000000000000000" ,
             "11110"  : "00000000000000000000000000000000" ,
             "11111"  : "00000000000000000000000000000000" ,
             "SP"     : "00000000000000000000000000000000" #Need to place this at its correct position
}
Data_Memory={
    "65536":"00000000000000000000000000000000",
    "65540":"00000000000000000000000000000000",
    "65544":"00000000000000000000000000000000",
    "65548":"00000000000000000000000000000000",
    "65552":"00000000000000000000000000000000",
    "65556":"00000000000000000000000000000000",
    "65560":"00000000000000000000000000000000",
    "65564":"00000000000000000000000000000000",
    "65568":"00000000000000000000000000000000",
    "65572":"00000000000000000000000000000000",
    "65576":"00000000000000000000000000000000",
    "65580":"00000000000000000000000000000000",
    "65584":"00000000000000000000000000000000",
    "65588":"00000000000000000000000000000000",
    "65592":"00000000000000000000000000000000",
    "65596":"00000000000000000000000000000000",
    "65600":"00000000000000000000000000000000",
    "65604":"00000000000000000000000000000000",
    "65608":"00000000000000000000000000000000",
    "65612":"00000000000000000000000000000000",
    "65616":"00000000000000000000000000000000",
    "65620":"00000000000000000000000000000000",
    "65624":"00000000000000000000000000000000",
    "65628":"00000000000000000000000000000000",
    "65632":"00000000000000000000000000000000",
    "65636":"00000000000000000000000000000000",
    "65640":"00000000000000000000000000000000",
    "65644":"00000000000000000000000000000000",
    "65648":"00000000000000000000000000000000",
    "65652":"00000000000000000000000000000000",
    "65656":"00000000000000000000000000000000",
    "65660":"00000000000000000000000000000000"
    }
Data_Memory_hex_Location=[
    "0x00010000",
    "0x00010004",
    "0x00010008",
    "0x0001000c",
    "0x00010010",
    "0x00010014",
    "0x00010018",
    "0x0001001c",
    "0x00010020",
    "0x00010024",
    "0x00010028",
    "0x0001002c",
    "0x00010030",
    "0x00010034",
    "0x00010038",
    "0x0001003c",
    "0x00010040",
    "0x00010044",
    "0x00010048",
    "0x0001004c",
    "0x00010050",
    "0x00010054",
    "0x00010058",
    "0x0001005c",
    "0x00010060",
    "0x00010064",
    "0x00010068",
    "0x0001006c",
    "0x00010070",
    "0x00010074",
    "0x00010078",
    "0x0001007c"
    ]

# Program Counter
PC=0

# Required Functions #

# Number Converter
def number_convert(number,Binary_to_integer_conversion=False,bits=0): 
    if (Binary_to_integer_conversion):
        assert len(number)<=bits
        n=int(number,2)
        s=1<<(bits-1)
        return ((n & s - 1) - (n & s))
    else:
        Binary_number=numpy.binary_repr(number, width=32)
        return Binary_number # will be returned as a string

#File Updater
def ouput_file_updator(Write_Register_Value=True):
    global Registers,Data_Memory,PC,OUT,Data_Memory_hex_Location
    with open(OUT, 'a') as file:
        if(Write_Register_Value):
            file.write("0b"+number_convert(PC,False)+" ")
            for i in Registers.keys():
                file.write("0b"+Registers[i]+" ")
        else:
            file.write("\n")
            keys=Data_Memory.keys()
            for i in range(0,len(Data_Memory_hex_Location)):
                location,value=Data_Memory_hex_Location[i],Data_Memory[keys[i]]
                file.write(location+":0b"+value+"\n")
            
# Instructions

# R-type instructions
def add(rs1,rs2,rd):# Trunkation Left!
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1+n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def sub(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1-n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def sll(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=int(Registers[rs2][-5:],2) # for unsigned value
    s=n1<<n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def slt(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    if(n1<n2):
        s=1
        Registers[rd]=number_convert(s)
    PC+=4
    return
def sltu(rs1,rs2,rd):
    global Registers,PC
    n1=int(Registers[rs1],2)
    n2=int(Registers[rs2],2)
    if(n1<n2):
        s=1
        Registers[rd]=number_convert(s)
    PC+=4
    return
def xor(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1^n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def srl(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=int(Registers[rs2][-5:],2) # for unsigned value
    s=n1>>n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def OR(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1|n2
    Registers[rd]=number_convert(s)
    PC+=4
    return
def AND(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1&n2
    Registers[rd]=number_convert(s)
    PC+=4
    return

# B-type instructions -- 32 may need to be replaced by len(imm)
def beq(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1],True,32), number_convert(Registers[rs2],True,32)
    if (n1==n2):
        imm10=number_convert(imm,True,32) # Might Need to change the 32 here
        PC+=imm10
        return
    PC+=4
    main(PC//4)
    return
def bne(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1],True,32), number_convert(Registers[rs2],True,32)
    if (n1!=n2):
        imm10=number_convert(imm,True,32) # Might need to change the 32 here
        PC+=imm10
        return
    PC+=4
    main(PC//4)
    return
def blt(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1], True ,32) , number_convert(Registers[rs2] , True ,32)
    if ((n1<n2)):
        imm10=number_convert(imm,True,32) # Might need to change the 32 here
        PC+=imm10
        return
    PC+=4
    main(PC//4)
    return
def bge(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1], True ,32) , number_convert(Registers[rs2], True ,32)
    if(n1>=n2):
        imm10=number_convert(imm,True,32)  # Might need to change the 32 here
        PC+=(imm10)
        return
    PC+=4
    main(PC//4)
    return
def bltu(rs1, rs2, imm):
    global PC, Registers
    n1,n2=int(Registers[rs1],2),int(Registers[rs2],2)
    if(n1 < n2):
        imm10=number_convert(imm,True,32) # Might need to change the 32 here
        PC += imm10
        return
    PC+=4
    main(PC//4)
    return
def bgeu(rs1, rs2, imm):
    global PC,Registers
    n1,n2=int(Registers[rs1],2),int(Registers[rs2],2)
    if(n1 >= n2):
        imm10=number_convert(imm,True,32) # Might need to change the 32 here
        PC+=imm10
        return
    PC+=4
    main(PC//4)
    return

# J-type instructions
def jal(rd, imm):
    global PC, Registers
    imm+="0" #Don't know if this shoud be done or not??
    imm10=number_convert(imm,True,len(imm))
    Registers[rd]=number_convert(imm10 + 4, False)
    PC=PC +imm10
    return
    
# I-type  Instructions
def lw(rd, rs, imm):
    global PC, Registers,Data_Memory
    PC+=4
    imm10=number_convert(imm,True,len(imm))
    rs10=number_convert(rs,True,len(rs))
    Registers[rd]=Data_Memory[imm10+rs10]
    return
def sltiu(rd, rs, imm):
    global PC,Registers
    rs10,imm10=int(rs,2),int(imm,2)
    if(rs10<imm10):
        Registers[rd]=number_convert(1,False)
        PC+=4
    return
def jalr(rd, rs, imm):
    global PC,Registers
    imm
    Registers[rd]=number_convert(PC+4,False)
    rs10,imm10=number_convert(rs,True,len(rs))+ number_convert(imm, True, len(imm))
    PC=(rs10 +imm10) #need to ask if rs10 would come or just rs?
    main(PC//4)
    return
def addi(rd, rs, imm):
    global PC,Registers
    rs10,imm10=number_convert(rs,True,len(rs)),number_convert(imm,True,len(imm))
    Registers[rd]=number_convert(rs10+imm10,False)
    PC+=4
    return

# U-Type Instructions -- ask if this is correct or not?
def lui(rd,imm):
    global PC, Registers
    imm+="000000000000"
    Registers[rd]=number_convert((number_convert(imm,True,len(imm))),False)
    PC+=4
    return
def auipc(rd,imm):
    global PC, Registers
    imm+="000000000000"
    Registers[rd]=number_convert((PC+number_convert(imm,True,len(imm))),False)
    PC+=4
    return
    
# S-Type Instructions -- ask if this is correct or not?
def sw(imm,rs2,rs1,):
    global Registers,PC,Data_Memory
    rs110,rs210,imm10=number_convert(rs1,True,len(rs1)),number_convert(rs2,True,len(rs2)),number_convert(imm,True,len(imm))
    Data_Memory[str(rs110+imm10)]=Registers[rs2]
    PC+=4
    return 

Opcode={    # R Type functions -- done -- testing remains
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
    # J Type functions -- done -- testing remains
    "1101111":jal    
    }

def main(given_pc):
    global PC,Opcode,Registers,Data_Memory,instructions,IN,OUT
    