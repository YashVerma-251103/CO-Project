import sys
import numpy
#IF=sys.argv[1] #Input File
#OUT=sys.argv[2] #Output File\
IF=r"C:\Users\davsv\Dropbox\PC (2)\Desktop\s_test1.txt"
OUT=r"C:\Users\davsv\Dropbox\PC (2)\Desktop\out1.txt"
with open(IF,"r") as file: #Reading input file
    instructions=file.readlines()
total_instructions=len(instructions)
Registers={"00000":"00000000000000000000000000000000","00001":"00000000000000000000000000000000","00010":"00000000000000000000000000000000","00011":"00000000000000000000000000000000","00100":"00000000000000000000000000000000","00101":"00000000000000000000000000000000","00110":"00000000000000000000000000000000","00111":"00000000000000000000000000000000","01000":"00000000000000000000000000000000","01000":"00000000000000000000000000000000","01001":"00000000000000000000000000000000","01010":"00000000000000000000000000000000","01011":"00000000000000000000000000000000","01100":"00000000000000000000000000000000","01101":"00000000000000000000000000000000","01110":"00000000000000000000000000000000","01111":"00000000000000000000000000000000","10000":"00000000000000000000000000000000","10001":"00000000000000000000000000000000","10010":"00000000000000000000000000000000","10011":"00000000000000000000000000000000","10100":"00000000000000000000000000000000","10101":"00000000000000000000000000000000","10110":"00000000000000000000000000000000","10111":"00000000000000000000000000000000","11000":"00000000000000000000000000000000","11001":"00000000000000000000000000000000","11010":"00000000000000000000000000000000","11011":"00000000000000000000000000000000","11100":"00000000000000000000000000000000","11101":"00000000000000000000000000000000","11110":"00000000000000000000000000000000","11111":"00000000000000000000000000000000"}
Data_Memory={"65536":"00000000000000000000000000000000","65540":"00000000000000000000000000000000","65544":"00000000000000000000000000000000","65548":"00000000000000000000000000000000","65552":"00000000000000000000000000000000","65556":"00000000000000000000000000000000","65560":"00000000000000000000000000000000","65564":"00000000000000000000000000000000","65568":"00000000000000000000000000000000","65572":"00000000000000000000000000000000","65576":"00000000000000000000000000000000","65580":"00000000000000000000000000000000","65584":"00000000000000000000000000000000","65588":"00000000000000000000000000000000","65592":"00000000000000000000000000000000","65596":"00000000000000000000000000000000","65600":"00000000000000000000000000000000","65604":"00000000000000000000000000000000","65608":"00000000000000000000000000000000","65612":"00000000000000000000000000000000","65616":"00000000000000000000000000000000","65620":"00000000000000000000000000000000","65624":"00000000000000000000000000000000","65628":"00000000000000000000000000000000","65632":"00000000000000000000000000000000","65636":"00000000000000000000000000000000","65640":"00000000000000000000000000000000","65644":"00000000000000000000000000000000","65648":"00000000000000000000000000000000","65652":"00000000000000000000000000000000","65656":"00000000000000000000000000000000","65660":"00000000000000000000000000000000"}
Data_Memory_hex_Location=["0x00010000","0x00010004","0x00010008","0x0001000c","0x00010010","0x00010014","0x00010018","0x0001001c","0x00010020","0x00010024","0x00010028","0x0001002c","0x00010030","0x00010034","0x00010038","0x0001003c","0x00010040","0x00010044","0x00010048","0x0001004c","0x00010050","0x00010054","0x00010058","0x0001005c","0x00010060","0x00010064","0x00010068","0x0001006c","0x00010070","0x00010074","0x00010078","0x0001007c"]
PC=0
def number_convert(number,Binary_to_integer_conversion=False,bits=0): 
    if (Binary_to_integer_conversion):
        assert len(number)<=bits
        n=int(number,2)
        s=1<<(bits-1)
        return ((n & s - 1) - (n & s))
    else:
        Binary_number=numpy.binary_repr(number, width=32)
        return Binary_number

def output_file_updator(Write_Register_Value=True):
    global Registers,Data_Memory,PC,OUT,Data_Memory_hex_Location
    with open(OUT, 'a') as file:
        if(Write_Register_Value):
            file.write("0b"+number_convert(PC,False)+" ")
            for i in Registers.keys():
                file.write("0b"+Registers[i]+" ")
            file.write("\n")
        else:
            keys=list(Data_Memory.keys())
            for i in range(0,len(Data_Memory_hex_Location)):
                location,value=Data_Memory_hex_Location[i],Data_Memory[keys[i]]
                file.write(location+":0b"+value+"\n")
def add(rs1,rs2,rd): #trunkation left!!
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1+n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("add")
    return
def sub(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1-n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("sub")
    return
def sll(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=int(Registers[rs2][-5:],2)
    s=n1<<n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("sll")
    return
def slt(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    if(n1<n2):
        s=1
        Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("slt")
    return
def sltu(rs1,rs2,rd):
    global Registers,PC
    n1=int(Registers[rs1],2)
    n2=int(Registers[rs2],2)
    if(n1<n2):
        s=1
        Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("sltu")
    return
def xor(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1^n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("xor")
    return
def srl(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=int(Registers[rs2][-5:],2)
    s=n1>>n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("srl")
    return
def OR(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1|n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("OR")
    return
def AND(rs1,rs2,rd):
    global Registers,PC
    n1=number_convert(Registers[rs1],True,32)
    n2=number_convert(Registers[rs2],True,32)
    s=n1&n2
    Registers[rd]=number_convert(s)
    PC+=4
    output_file_updator()
    print("AND")
    return
def beq(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1],True,32), number_convert(Registers[rs2],True,32)
    print("beq")
    if (n1==n2):
        imm10=number_convert(imm,True,32)
        PC+=imm10
        main(PC//4)
        return
    PC+=4
    return
def bne(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1],True,32), number_convert(Registers[rs2],True,32)
    print("bne")
    if (n1!=n2):
        imm10=number_convert(imm,True,32)
        PC+=imm10
        main(PC//4)
        return
    PC+=4
    return
def blt(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1], True ,32) , number_convert(Registers[rs2] , True ,32)
    print("blt")
    if ((n1<n2)):
        imm10=number_convert(imm,True,32)
        PC+=imm10
        main(PC//4)
        return
    PC+=4
    return
def bge(rs1, rs2, imm):
    global PC, Registers
    n1,n2=number_convert(Registers[rs1], True ,32) , number_convert(Registers[rs2], True ,32)
    print("bge")
    if(n1>=n2):
        imm10=number_convert(imm,True,32)
        PC+=(imm10)
        main(PC//4)
        return
    PC+=4
    return
def bltu(rs1, rs2, imm):
    global PC, Registers
    n1,n2=int(Registers[rs1],2),int(Registers[rs2],2)
    print("bltu")
    if(n1 < n2):
        imm10=number_convert(imm,True,32)
        PC += imm10
        main(PC//4)
        return
    PC+=4
    return
def bgeu(rs1, rs2, imm):
    global PC,Registers
    n1,n2=int(Registers[rs1],2),int(Registers[rs2],2)
    print("bgeu")
    if(n1 >= n2):
        imm10=number_convert(imm,True,32)
        PC+=imm10
        main(PC//4)
        return
    PC+=4
    return
def jal(rd, imm):
    global PC, Registers
    print("jal")
    imm+="0"
    imm10=number_convert(imm,True,len(imm))
    Registers[rd]=number_convert(imm10 + 4, False)
    PC=PC +imm10
    main(PC//4)
    return
def lw(rd, rs, imm):
    global PC, Registers,Data_Memory
    print("lw")
    PC+=4
    imm10=number_convert(imm,True,len(imm))
    rs10=number_convert(rs,True,len(rs))
    Registers[rd]=Data_Memory[imm10+rs10]
    output_file_updator()
    return
def sltiu(rd, rs, imm):
    global PC,Registers
    print("sltiu")
    rs10,imm10=int(rs,2),int(imm,2)
    if(rs10<imm10):
        Registers[rd]=number_convert(1,False)
        PC+=4
    output_file_updator()
    return
def jalr(rd, rs, imm):
    global PC,Registers
    print("jalr")
    Registers[rd]=number_convert(PC+4,False)
    rs10,imm10=number_convert(rs,True,len(rs))+ number_convert(imm, True, len(imm))
    PC=(rs10 +imm10)
    main(PC//4)
    return
def addi(rd, rs, imm):
    global PC,Registers
    print("addi")
    rs10,imm10=number_convert(rs,True,len(rs)),number_convert(imm,True,len(imm))
    Registers[rd]=number_convert(rs10+imm10,False)
    PC+=4
    output_file_updator()
    return
def lui(rd,imm): # Check for this
    global PC, Registers
    print("lui")
    imm+="000000000000"
    Registers[rd]=imm
    PC+=4
    output_file_updator()
    return
def auipc(rd,imm):
    global PC, Registers
    print("auipc")
    imm+="000000000000"
    Registers[rd]=number_convert((PC+number_convert(imm,True,len(imm))),False)
    PC+=4
    output_file_updator()
    return
def sw(rs1,rs2,imm):
    global Registers,PC,Data_Memory
    print("sw")
    rs110,rs210,imm10=number_convert(rs1,True,len(rs1)),number_convert(rs2,True,len(rs2)),number_convert(imm,True,len(imm))
    Data_Memory[str(rs110+imm10)]=Registers[rs2]
    PC+=4
    return 
Opcode={"0110011":{"000":{"0000000":add,"0100000":sub},"001":sll,"010":slt,"011":sltu,"100":xor,"101":srl,"110":OR,"111":AND},"0000011":lw,"0010011":{"000":addi,"011":sltiu},"1100111":jalr,"0100011":sw,"1100011":{"000":beq,"001":bne,"100":blt,"101":bge,"110":bltu,"111":bgeu,},"0110111":lui,"0010111":auipc,"1101111":jal}
def main(given_pc):
    global PC,Opcode,Registers,Data_Memory,instructions,IF,OUT,total_instructions
    print("main")
    for i in range(given_pc,total_instructions):
        instruction=instructions[i].rstrip()
        if instruction=="00000000000000000000000001100011":
            PC+=4
            output_file_updator()
            output_file_updator(False)
            exit()
        current_opcode=instruction[-7:]
        if current_opcode=="0110011": # R-type
            f3,f7=instruction[-15:-12],instruction[-32:-25]
            rd,rs1,rs2=instruction[-12:-7],instruction[-20:-15],instruction[-25:-20]
            if f3 == "000":
                Opcode[current_opcode][f3][f7](rs1,rs2,rd)
            else:
                Opcode[current_opcode][f3](rs1,rs2,rd)
        elif current_opcode=="1100011": # B-type
            f3=instruction[-15:-12]
            rs1,rs2=instruction[-20:-15],instruction[-25:-20]
            imm=instruction[0]+instruction[24]+instruction[1:7]+instruction[20:24]+"0"
            Opcode[current_opcode][f3](rs1,rs2,imm)
        elif current_opcode=="0100011": # S-type
            rs1,rs2=instruction[-20:-15],instruction[-25:-20]
            imm=instruction[0:7]+instruction[20:25]
            Opcode[current_opcode](rs1,rs2,imm)
        elif current_opcode in ["0010011","1100111","1100111"]:
            imm=instruction[0:12]
            rd,rs=instruction[-12:-7],instruction[-20:-15]
            if current_opcode=="0010011":
                f3=instruction[-15:-12]
                Opcode[current_opcode][f3](rd,rs,imm)
            else:
                Opcode[current_opcode](rd,rs,imm)
        elif current_opcode in ["0110111","0010111"]:
            rd,imm=instruction[-12:-7],(instruction[-32:-12]+"000000000000")
            Opcode[current_opcode](rd,imm)
        elif current_opcode=="1101111":
            imm=(instruction[0]+instruction[12:20]+instruction[11]+instruction[1:11]+"0")
            rd=instruction[-12:-7]
            Opcode[current_opcode](rd,imm)
main(0)
