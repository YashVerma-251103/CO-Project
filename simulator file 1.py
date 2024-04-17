import sys
inFile,outFile=sys.argv[1],sys.argv[2]

# Required Spaces and PC
PC=0
Registers={
    "00000":"00000000000000000000000000000000",
    "00001":"00000000000000000000000000000000",
    "00010":"00000000000000000000000100000000",
    "00011":"00000000000000000000000000000000",
    "00100":"00000000000000000000000000000000",
    "00101":"00000000000000000000000000000000",
    "00110":"00000000000000000000000000000000",
    "00111":"00000000000000000000000000000000",
    "01000":"00000000000000000000000000000000",
    "01001":"00000000000000000000000000000000",
    "01010":"00000000000000000000000000000000",
    "01011":"00000000000000000000000000000000",
    "01100":"00000000000000000000000000000000",
    "01101":"00000000000000000000000000000000",
    "01110":"00000000000000000000000000000000",
    "01111":"00000000000000000000000000000000",
    "10000":"00000000000000000000000000000000",
    "10001":"00000000000000000000000000000000",
    "10010":"00000000000000000000000000000000",
    "10011":"00000000000000000000000000000000",
    "10100":"00000000000000000000000000000000",
    "10101":"00000000000000000000000000000000",
    "10110":"00000000000000000000000000000000",
    "10111":"00000000000000000000000000000000",
    "11000":"00000000000000000000000000000000",
    "11001":"00000000000000000000000000000000",
    "11010":"00000000000000000000000000000000",
    "11011":"00000000000000000000000000000000",
    "11100":"00000000000000000000000000000000",
    "11101":"00000000000000000000000000000000",
    "11110":"00000000000000000000000000000000",
    "11111":"00000000000000000000000000000000"
}
Data_Memory_in_integer={
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

# getting instructions
with open(inFile, 'r') as file:    
    instructions = file.readlines()
# Cleaning the output file
with open(outFile, 'w') as file:
    file.writelines("")
# Removing \n from end of line
for i in range(len(instructions)):
    if instructions[i].strip()=='\n':
        pass
    else:
        instructions[i]=instructions[i].strip()
Total_instructions=len(instructions)

# Utility Functions
def Output_File_Writer(Register=True):
    global PC,Registers
    if Register:
        with open(outFile, 'a') as file:
            file.write(f"0b{Number_change(PC)} ")
            for i in Registers:
                file.write(f"0b{Registers[i]} ")
            file.write("\n")
    else:
        global Data_Memory_in_integer
        with open(outFile, 'a') as file:
            for j in Data_Memory_in_integer:
                file.writelines(f"{(hex(int(j)))[0:2]}000{(hex(int(j)))[2:]}:0b{Data_Memory_in_integer[j]}\n")    
def Number_change(number,into_decimal=False,Bits=0):
    if (into_decimal):
        assert len(number) <= Bits
        n = int(number, 2)
        s = 1 << (Bits - 1)
        return (n & s - 1) - (n & s)
    else:
        Binary_convert=lambda x :''.join(reversed([str((x >> i) & (1)) for i in range(32)]))
        return Binary_convert(number)

# Opperating Functions
def RCall(Instruction):
    global PC
    f3,rd,rs1,rs2=Instruction[17:20],Instruction[20:25],Instruction[12:17],Instruction[7:12]
    PC+=4
    if  ((f3=="000") and (Instruction[0:7]=="0100000")):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)-Number_change(Registers[rs2],True,32))
    elif (f3=="000"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)+Number_change(Registers[rs2],True,32))
    elif (f3=="001"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)<<int(Registers[rs2][27:32],2))
    elif (f3=="010"):
        if (Number_change(Registers[rs1],True,32)<Number_change(Registers[rs2],True,32)):
            Registers[rd]=Number_change(1)
    elif (f3=="011"):
        if (int(Registers[rs1],2)<int(Registers[rs2],2)):
            Registers[rd]=Number_change(1)
    elif (f3=="100"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)^Number_change(Registers[rs2],True,32))
    elif (f3=="101"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)>>int(Registers[rs2][27:32],2))
    elif (f3=="110"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)|Number_change(Registers[rs2],True,32))
    elif (f3=="111"):
        Registers[rd]=Number_change(Number_change(Registers[rs1],True,32)&Number_change(Registers[rs2],True,32))
    Output_File_Writer()
def JCall(Instruction):
    global PC
    rd,imm=Instruction[20:25],(Instruction[0]+Instruction[12:20]+Instruction[11]+Instruction[1:11]+"0")
    imm10=Number_change(imm,True,len(imm))
    Registers[rd]=Number_change(PC+4)
    PC=Number_change((Number_change(PC+imm10)[0:-1]+"0"),True,32)
    Output_File_Writer()
    driver(PC//4)
def BCall(Instruction):
    global PC
    f3,rs1,rs2,imm=Instruction[17:20],Instruction[12:17],Instruction[7:12],(Instruction[0]+Instruction[24]+Instruction[1:7]+Instruction[20:24]+"0")
    imm10=Number_change(imm,True,len(imm))
    if ((f3=="000") and (Number_change(Registers[rs1],True,32)==Number_change(Registers[rs2],True,32))):
        PC=PC+imm10
    elif ((f3=="001") and (Number_change(Registers[rs1],True,32)!=Number_change(Registers[rs2],True,32))): 
        PC=PC+imm10
    elif ((f3=="100") and (Number_change(Registers[rs1],True,32)<Number_change(Registers[rs2],True,32))):
        PC=PC+imm10
    elif ((f3=="101") and (Number_change(Registers[rs1],True,32)>=Number_change(Registers[rs2],True,32))):
        PC=PC+imm10
    elif ((f3=="110") and (int(Registers[rs1],2)<int(Registers[rs2],2))):
        PC=PC+imm10
    elif ((f3=="111") and (int(Registers[rs1],2)>=int(Registers[rs2],2))):
        PC=PC+imm10
    else:
        PC+=4
    Output_File_Writer()
    driver(PC//4)
def UCall(Instruction,opperation):
    global PC
    rd = Instruction[20:25]
    PC+=4 
    if opperation == '0010111':
        imm = Number_change((Number_change(Instruction[0:20],True,len(Instruction[0:20])) << 12) + (PC-4))
    else:
        imm = Number_change((Number_change(Instruction[0:20],True,len(Instruction[0:20])) << 12))
    Registers[rd] = imm
    Output_File_Writer()
def ICall(Instruction , opperation):
    global PC
    f3,rd,rs,imm=Instruction[17:20],Instruction[20:25],Instruction[12:17],Instruction[0:12]
    imm10 = Number_change(imm,True,len(imm))
    rs10=Number_change(Registers[rs],True,32)
    PC+=4
    if (f3=="000" and opperation=="1100111"): 
        Registers[rd]=Number_change(PC)
        PC=Number_change(((Number_change(rs10 + imm10))[0:-1]+"0"),True,32)
        Output_File_Writer()
        driver(PC//4)
    else:
        if (f3 == "000"  and opperation=="0010011"): 
            Registers[rd] = Number_change(imm10 + rs10)
        elif (f3=="010"):
            Registers[rd] = Data_Memory_in_integer[str(imm10 + rs10)]
        elif (f3=="011"):
            if (int(Registers[rs] , 2) < int(imm , 2)):
                Registers[rd] = Number_change(1)
        Output_File_Writer()
def SCall(Instruction):
    global PC
    PC += 4
    imm,rs1,rs2=(Instruction[0:7]+Instruction[20:25]),Instruction[12:17],Instruction[7:12]
    imm_val=Number_change(imm,True,len(imm))
    base =Number_change(Registers[rs1],True,len(Registers[rs1])) 
    Data_Memory_in_integer[str(base+imm_val)] = Registers[rs2]
    Output_File_Writer()

# Main Driver
def driver(start):
    global PC
    for x in range(start,Total_instructions):
        if instructions[x]=="00000000000000000000000001100011": 
            Output_File_Writer()
            Output_File_Writer(False)
            exit()
        Opcode=instructions[x][25:len(instructions[x])]
        if Opcode=="0110011": 
            RCall(instructions[x])
        elif Opcode=="1101111": 
            JCall(instructions[x])
        elif Opcode=="1100011": 
            BCall(instructions[x])
        elif Opcode=="0110111": 
            UCall(instructions[x],"0110111")
        elif Opcode=="0010111": 
            UCall(instructions[x],"0010111")
        elif Opcode=="0000011":
            ICall(instructions[x],"0000011")
        elif Opcode=="0010011": 
            ICall(instructions[x],"0010011")
        elif Opcode=="1100111": 
            ICall(instructions[x],"1100111")
        elif Opcode=="0100011":
            SCall(instructions[x],"0100011")

# Start
driver(0)
