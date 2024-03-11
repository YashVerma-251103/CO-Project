import sys
input_file= sys.argv[1]
output_file= sys.argv[2]


def imm_convert(decimal_str, num_bits):
    if int(decimal_str)>=-2**(int(num_bits)-1) and int(decimal_str)<=((2**int(num_bits))-1):
        decimal = int(decimal_str)
        num_bits=int(num_bits)
        is_negative = decimal < 0
        abs_decimal = abs(decimal)
        binary = ''
        while abs_decimal > 0:
            binary = str(abs_decimal % 2) + binary
            abs_decimal //= 2
        binary = binary.rjust(num_bits, '0')
        if is_negative:
            inverted_binary = ''.join(['1' if bit == '0' else '0' for bit in binary])
            twos_complement = ''
            carry = 1
            for bit in inverted_binary[::-1]:
                if bit == '0' and carry == 1:
                    twos_complement = '1' + twos_complement
                    carry = 0
                elif bit == '1' and carry == 1:
                    twos_complement = '0' + twos_complement
                else:
                    twos_complement = bit + twos_complement
            binary = twos_complement

        return binary
    else:
        return "imm val out of range"

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
    i1=imm_convert(str(imm),str(12))
    if i1=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1      
    value=str(i1)+reg_codes[rs1]+isa_codes["lw"]["f3"]+reg_codes[rd]+isa_codes["lw"]["opcode"]
    return value
def addi(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    if i1=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1   
    value=str(i1)+reg_codes[rs1]+isa_codes["addi"]["f3"]+reg_codes[rd]+isa_codes["addi"]["opcode"]
    return value
def sltiu(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    if i1=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1   
    value=str(i1)+reg_codes[rs1]+isa_codes["sltiu"]["f3"]+reg_codes[rd]+isa_codes["sltiu"]["opcode"]
    return value
def jalr(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    if i1=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1   
    value=str(i1)+reg_codes[rs1]+isa_codes["jalr"]["f3"]+reg_codes[rd]+isa_codes["jalr"]["opcode"]
    return value

# S - type Functions
def sw(imm,rs2,rs1): # configure imms   ||   imm1 --> 11:5   ||  imm2 --> 4:0 
    si=imm_convert(str(imm),str(12))
    if si=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1   
    s1=si[0:7:1]  #s1[6::-1] was used earlier but was giving reversed results
    s2=si[7:12:1] #s2[11:6:-1] was used earlier but was giving reversed results
    value=s1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sw"]["f3"]+s2+isa_codes["sw"]["opcode"]
    return value

# U - type
def lui(imm,rd): #configure imm  ||  31:12
    ui=imm_convert(str(imm),str(32))
    if ui=="imm val out of range": 
        Flags["immediate"]["Flag"]=True
        return -1
    u1=ui[0:20:1]
    value=u1+reg_codes[rd]+isa_codes["lui"]["opcode"]
    return value
def auipc(imm,rd): #configure imm  ||  31:12
    ui=imm_convert(str(imm),str(32))
    if ui=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    u1=ui[0:20:1] 
    value=u1+reg_codes[rd]+isa_codes["auipc"]["opcode"]
    return value

# B - type      # configure imms   ||   imm1 --> 12|10:5   ||  imm2 --> 4:1|11
def beq(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["beq"]["f3"]+b2+isa_codes["beq"]["opcode"]
    return value
def bne(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bne"]["f3"]+b2+isa_codes["bne"]["opcode"]
    return value
def blt(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["blt"]["f3"]+b2+isa_codes["blt"]["opcode"]
    return value 
def bge(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bge"]["f3"]+b2+isa_codes["bge"]["opcode"]
    return value
def bltu(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bltu"]["f3"]+b2+isa_codes["bltu"]["opcode"]
    return value
def bgeu(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    if bi=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    b1=bi[-12]+bi[-11:-5:1]
    b2=bi[-5:-1:1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bgeu"]["f3"]+b2+isa_codes["bgeu"]["opcode"]
    return value

# J - type     #configure imm  ||  20|10:1|11|19:12
def jal(imm,rd):
    #imm=ans[19]+ans[9:0:-1]+ans[10]+ans[18:10:-1]
    ji=imm_convert(str(imm),str(20))  
    if ji=="imm val out of range":
        Flags["immediate"]["Flag"]=True
        return -1
    j1=ji[-20]+ji[9:19:1]+ji[-11]+ji[-12:-20:-1] #ji[-1:-11:-1] was used earlier but was giving wrong result
    value=j1+reg_codes[rd]+isa_codes["jal"]["opcode"]
    return value

# Bonus - Type #       ||    still need to build these out
def mul(rs1,rs2,rd):
    value=isa_codes["mul"]["f7"]+reg_codes[rs2]+reg_codes[rs1]+isa_codes["mul"]["f3"]+reg_codes[rd]+isa_codes["mul"]["opcode"]
    return value
def rst():
    value=isa_codes["rst"]["f7"]+"00000000000000"+isa_codes["rst"]["opcode"]
    return value
def halt():
    value=isa_codes["halt"]["f7"]+"00000000000000"+isa_codes["halt"]["opcode"]
    return value
def rvrs(rs,rd):
    value=isa_codes["rvrs"]["f7"]+"11111"+reg_codes[rs]+isa_codes["rvrs"]["f3"]+reg_codes[rd]+isa_codes["rvrs"]["opcode"]
    return value

reg_codes = { 
             "zero" : "00000" ,   # x0   
               "ra" : "00001" ,   # x1
               "sp" : "00010" ,   # x2
               "gp" : "00011" ,   # x3
               "tp" : "00100" ,   # x4
               "t0" : "00101" ,   # x5
               "t1" : "00110" ,   # x6
               "t2" : "00111" ,   # x7
               "s0" : "01000" ,   # x8
               "fp" : "01000" ,   # x8
               "s1" : "01001" ,   # x9
               "a0" : "01010" ,   # x10
               "a1" : "01011" ,   # x11
               "a2" : "01100" ,   # x12
               "a3" : "01101" ,   # x13
               "a4" : "01110" ,   # x14
               "a5" : "01111" ,   # x15
               "a6" : "10000" ,   # x16
               "a7" : "10001" ,   # x17
               "s2" : "10010" ,   # x18
               "s3" : "10011" ,   # x19
               "s4" : "10100" ,   # x20
               "s5" : "10101" ,   # x21
               "s6" : "10110" ,   # x22
               "s7" : "10111" ,   # x23
               "s8" : "11000" ,   # x24
               "s9" : "11001" ,   # x25
              "s10" : "11010" ,   # x26
              "s11" : "11011" ,   # x27
               "t3" : "11100" ,   # x28
               "t4" : "11101" ,   # x29
               "t5" : "11110" ,   # x30
               "t6" : "11111" ,   # x31
}

isa_codes={
    # r type
      "add":{"opcode":"0110011","type":"r","f3":"000","f7":"0000000","function":add},
      "sub":{"opcode":"0110011","type":"r","f3":"000","f7":"0100000","function":sub},
      "sll":{"opcode":"0110011","type":"r","f3":"001","f7":"0000000","function":sll},
      "slt":{"opcode":"0110011","type":"r","f3":"010","f7":"0000000","function":slt},
     "sltu":{"opcode":"0110011","type":"r","f3":"011","f7":"0000000","function":sltu},
      "xor":{"opcode":"0110011","type":"r","f3":"100","f7":"0000000","function":xor},
      "srl":{"opcode":"0110011","type":"r","f3":"101","f7":"0000000","function":srl},
       "or":{"opcode":"0110011","type":"r","f3":"110","f7":"0000000","function":OR},
      "and":{"opcode":"0110011","type":"r","f3":"111","f7":"0000000","function":AND},
    # i
       "lw":{"opcode":"0000011","type":"i","f3":"010","function":lw},
     "addi":{"opcode":"0010011","type":"i","f3":"000","function":addi},
    "sltiu":{"opcode":"0010011","type":"i","f3":"011","function":sltiu},
     "jalr":{"opcode":"1100111","type":"i","f3":"000","function":jalr},
    #  s 
       "sw":{"opcode":"0100011","type":"s","f3":"010","function":sw},
    # b
      "beq":{"opcode":"1100011","type":"b","f3":"000","function":beq},
      "bne":{"opcode":"1100011","type":"b","f3":"001","function":bne},
      "blt":{"opcode":"1100011","type":"b","f3":"100","function":blt},
      "bge":{"opcode":"1100011","type":"b","f3":"101","function":bge},
     "bltu":{"opcode":"1100011","type":"b","f3":"110","function":bltu},
     "bgeu":{"opcode":"1100011","type":"b","f3":"111","function":bgeu},
    # u
      "lui":{"opcode":"0110111","type":"u","function":lui},
    "auipc":{"opcode":"0010111","type":"u","function":auipc},
    # J
      "jal":{"opcode":"1101111","type":"j","function":jal},
    # bonus -- configure -- special cases
     "mul":{"Opcode":"0000000","type":"bonus","f7":"0000000","f3":"000","function":mul},
     "rst":{"Opcode":"0101010","type":"bonus","f7":"0000000","f3":"000","function":rst},
    "halt":{"Opcode":"1010101","type":"bonus","f7":"0000000","f3":"000","function":halt},
    "rvrs":{"Opcode":"1111111","type":"bonus","f7":"1111111","f3":"111","function":rvrs}
}
        
#List of Regiters and ISAs
ISAs=list(isa_codes.keys())
registers=list(reg_codes.keys())

#For Errors
Flags={
    "reg":{"Flag":False,"Name":[],"Line":[]},
    "instruction":{"Flag":False,"Value":[],"Line":[]},
    "immediate":{"Flag":False,"Value":[],"Line":[]},
    "label":{"Flag":False,"Value":[],"Line":[]}
}

# file import of assembly code
with open(input_file,"r") as f:
    data=f.readlines()
        
input_instruction = []
Output_instruction = []
counter=0
labels={"Present":False,"Labels":[],"line":[]} # Lable counter
Virtual_Halts=[]

for instruction in data: #Gives me everthing required in a list
    if instruction in ["\n",""]:
        continue
    instruct=instruction.rstrip()
    instruct=instruct.lstrip()
    if ":" in instruct:
        index_=instruct.index(":")
        if ("beq zero,zero,0\n" == instruct[index_+1:]):
            Virtual_Halts.append(counter)
    else:
        if ("beq zero,zero,0\n" == instruct):
                    Virtual_Halts.append(counter)
    input_instruction.append(instruct.split())
    if input_instruction[0][-1]==":": #Should remove all labels and not their position
        if " " in input_instruction[0]:
            Flags["label"]["Flag"]=True
            Flags["label"]["Value"]=input_instruction[0]
            Flags["label"]["Line"]=counter
        labels["Present"]=True
        labels["Labels"].append(input_instruction[0])
        labels["line"].append(counter) #Just not sure about the way to note it. here although i have used Positon rather than indexing think of lines.
        input_instruction.pop(0)
    counter+=4

#Converting the main program
counter=0
for instruction in input_instruction:
    opperation=instruction[0]
    #if opperation in isa_codes.keys(): #if a valid opperation
    if opperation in ISAs: #if a valid opperation
        op_type=isa_codes[opperation]["type"]
        if op_type=="r": #for all r type instructions
            rd,rs1,rs2=instruction[-1].split(",")
            if rd not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rd)
                Flags["reg"]["Line"].append(counter)
            if rs1 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs1)
                Flags["reg"]["Line"].append(counter)
            if rs2 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs2)
                Flags["reg"]["Line"].append(counter)
            if Flags["reg"]["Flag"]==False:
                Binary_Format=isa_codes[opperation]["function"](rs1,rs2,rd)
                Output_instruction.append(Binary_Format)
        elif op_type=="i": #for all i type instructions
            if opperation != "lw":
                rd,rs,imm=instruction[-1].split(",")
            else:
                rd,imm_rs=instruction[-1].split(",")
                imm,rs=imm_rs.split("(")
                rs=rs[:-1]
            if rd not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rd)
                Flags["reg"]["Line"].append(counter)
            if rs not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs)
                Flags["reg"]["Line"].append(counter)
            if Flags["reg"]["Flag"]==False:
                Binary_Format=isa_codes[opperation]["function"](imm,rs,rd)
                if Binary_Format==-1: #imm error toh nahi hai 
                    Flags["immediate"]["Flag"]=True
                    Flags["immediate"]["Line"].append(counter)
                    Flags["immediate"]["Value"].append(imm)
                    continue
                else:
                    Output_instruction.append(Binary_Format)
        elif op_type=="s": #Should work fine ig
            rs2,imm_rs1=instruction[-1].split(",")            
            imm,rs1=imm_rs1.split("(")
            rs1=rs1[:-1]
            if rs2 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs2)
                Flags["reg"]["Line"].append(counter)
            if rs1 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs1)
                Flags["reg"]["Line"].append(counter)
            if Flags["reg"]["Flag"]==False:             
                Binary_Format=isa_codes[opperation]["function"](imm,rs2,rs1)
                if Binary_Format==-1: #imm error toh nahi hai 
                    Flags["immediate"]["Flag"]=True
                    Flags["immediate"]["Line"].append(counter)
                    Flags["immediate"]["Value"].append(imm)
                    continue
                else:
                    Output_instruction.append(Binary_Format)
        elif op_type=="b": #for all b type instructions
            rs1,rs2,imm=instruction[-1].split(",")
            if imm in labels["Labels"]:
                index_of_label=labels["line"].index(imm)
                if (counter>index_of_label):
                    imm=counter-index_of_label                                    
                elif (counter<index_of_label):
                    imm=counter+index_of_label               
                else:
                    Flags["label"]["Flag"]=True
                    Flags["label"]["Line"].append(counter)
                    Flags["label"]["Value"].append(imm)
            if rs2 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs2)
                Flags["reg"]["Line"].append(counter)
            if rs1 not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rs1)
                Flags["reg"]["Line"].append(counter)
            if (Flags["reg"]["Flag"]==False) and (Flags["label"]["Flag"]==False):
                Binary_Format=isa_codes[opperation]["function"](rs1,rs2,imm)
                if Binary_Format==-1:
                    Flags["immediate"]["Flag"]=True
                    Flags["immediate"]["Line"].append(counter)
                    Flags["immediate"]["Value"].append(imm)
                    continue
                else:                    
                    Output_instruction.append(Binary_Format)
        elif op_type=="u": #for all u type instructions
            rd,imm=instruction[-1].split(",")
            if rd not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rd)
                Flags["reg"]["Line"].append(counter)
            if Flags["reg"]["Flag"]==False:
                Binary_Format=isa_codes[opperation]["function"](imm,rd)
                if Binary_Format==-1:
                    Flags["immediate"]["Flag"]=True
                    Flags["immediate"]["Line"].append(counter)
                    Flags["immediate"]["Value"].append(imm)
                    continue    
                else:                
                    Output_instruction.append(Binary_Format)
        elif op_type=="j": #for all j type instructions
            rd,imm=instruction[-1].split(",")
            if imm in labels["Labels"]:
                index_of_label=labels["line"].index(imm)
                if (counter>index_of_label):
                    imm=counter-index_of_label                                
                elif (counter<index_of_label):
                    imm=counter+index_of_label                  
                else:
                    Flags["label"]["Flag"]=True
                    Flags["label"]["Line"].append(counter)
                    Flags["label"]["Value"].append(imm)            
            if rd not in registers:
                Flags["reg"]["Flag"]=True
                Flags["reg"]["Name"].append(rd)
                Flags["reg"]["Line"].append(counter)
                continue
            if (Flags["reg"]["Flag"]==False) and (Flags["label"]["Flag"]==False):
                Binary_Format=isa_codes[opperation]["function"](imm,rd)
                if Binary_Format==-1:
                    Flags["immediate"]["Flag"]=True
                    Flags["immediate"]["Line"].append(counter)
                    Flags["immediate"]["Value"].append(imm)
                    continue
                else:
                    Output_instruction.append(Binary_Format)
        elif op_type=="bonus": #Still left
            if opperation == "halt":
                Binary_Format=halt()
                Output_instruction.append(Binary_Format)
                continue
            elif opperation == "rst":
                Binary_Format=rst()
                Output_instruction.append(Binary_Format)
                continue
            elif opperation == "rvrs": #rvrs rd,rs
                rd,rs=instruction[-1].split(",")
                if rd not in registers:
                    Flags["reg"]["Flag"]=True
                    Flags["reg"]["Name"].append(rd)
                    Flags["reg"]["Line"].append(counter)
                if rs not in registers:
                    Flags["reg"]["Flag"]=True
                    Flags["reg"]["Name"].append(rs)
                    Flags["reg"]["Line"].append(counter)
                if Flags["reg"]["Flag"]==False:
                    Binary_Format=isa_codes[opperation]["function"](rs,rd)
                    Output_instruction.append(Binary_Format)
            elif opperation == "mul":
                rs1,rs2,rd=instruction[-1].split(",")
                if rd not in registers:
                    Flags["reg"]["Flag"]=True
                    Flags["reg"]["Name"].append(rd)
                    Flags["reg"]["Line"].append(counter)
                if rs1 not in registers:
                    Flags["reg"]["Flag"]=True
                    Flags["reg"]["Name"].append(rs1)
                    Flags["reg"]["Line"].append(counter)
                if rs2 not in registers:
                    Flags["reg"]["Flag"]=True
                    Flags["reg"]["Name"].append(rs2)
                    Flags["reg"]["Line"].append(counter)
                if Flags["reg"]["Flag"]==False:
                    Binary_Format=isa_codes[opperation]["function"](rs1,rs2,rd)
                    Output_instruction.append(Binary_Format)
                
                                                
    else: #give error of invalid opperation
       Flags["instruction"]["Flag"]=True
       Flags["instruction"]["Value"].append(opperation)
       Flags["instruction"]["Line"].append(counter)
    counter+=4

if ((Flags["reg"]["Flag"]==False) and (Flags["immediate"]["Flag"]==False) and (Flags["instruction"]["Flag"]==False) and (Flags["label"]["Flag"]==False)):
    # creating a binary code text file
    with open(output_file,"w") as f:
        #f.writelines(Output_instruction)
        for i in range(len(Output_instruction)):
            f.write(Output_instruction[i])
            if i<(len(Output_instruction)-1):
                f.write("\n")
else: #return all errors
    if (Flags["instruction"]["Flag"]==False):
        for i in range(len(Flags["instruction"]["Value"])):
            value,line = Flags["instruction"]["Value"][i],Flags["instruction"]["Line"][i]
            print(f"Instruction '{value}' in line {(line//4)+1} is not a valid Instruction.")
    if (Flags["reg"]["Flag"]):
        for i in range(len(Flags["reg"]["Name"])):
            name,line = Flags["reg"]["Name"][i] , Flags["reg"]["Line"][i]
            print(f"Register '{name}' in line {(line//4)+1} is not a valid Register.")
    if (Flags["immediate"]["Flag"]):
        for i in range(len(Flags["immediate"]["Values"])):
            value,line = Flags["immediate"]["Values"][i] , Flags["immediate"]["Line"][i]
            print(f"Immediate '{value}' in line {(line//4)+1} is not a valid immediate.")
    if (Flags["label"]["Flag"]):
        for i in range(len(Flags["label"]["Value"])):
            value,line = Flags["label"]["Value"][i],Flags["label"]["Line"][i]
            print(f"Invalid Usage of Label '{value}' in line {(line//4)+1}.")