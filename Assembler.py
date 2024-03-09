import sys
def imm_convert(s,r):
    if int(s)>=-2**(int(r)-1) and int(s)<=((2**int(r))-1):  #2's complement range
        if 1==1:
            if s[0]=="-":
                if_negative=True
                s=s[1:]
                n=int(s)
                a=[]
                s=""
                while(n>0):
                    b=n%2
                    a.append(b)
                    n=n//2
                a.reverse()
                for i in a:
                    s=s+str(i)
                d=int(r)-len(s)
                s=d*"0"+s   # r bit binary number of given string
                for i in s[::-1]:
                    if i=="1":                
                        d1=s[0:s.index(i)]  
                        d2=s[s.index(i): ]  # copying the number untill first 1
                        f=""
                        for j in d1[::-1]:  # and reversing the 0 to 1 and vice versa for the numbers following
                            if j=="0":
                                f=f+"1"
                            else:
                                f=f+"0"
                        s=f+d2
                        break
                return s
                #return s[0]+s[10:]+s[9]+s[1:9] #according to the imm[20|10:1|11|19:12] 
            elif s[0]!="-":
                if_negative=False
                n=int(s)
                a=[]
                s=""
                while(n>0):
                    b=n%2
                    a.append(b)
                    n=n//2
                a.reverse()
                for i in a:
                    s=s+str(i)
                d=int(r)-len(s)
                s=d*"0"+s      # r bit binary number of given string
                return s
                #return s[0]+s[10:]+s[9]+s[1:9] #according to the imm[20|10:1|11|19:12]
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
    value=i1+reg_codes[rs1]+isa_codes["lw"]["f3"]+reg_codes[rd]+isa_codes["lw"]["opcode"]
    return value
def addi(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    value=i1+reg_codes[rs1]+isa_codes["addi"]["f3"]+reg_codes[rd]+isa_codes["addi"]["opcode"]
    return value
def sltiu(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    value=i1+reg_codes[rs1]+isa_codes["sltiu"]["f3"]+reg_codes[rd]+isa_codes["sltiu"]["opcode"]
    return value
def jalr(imm,rs1,rd): #configure imm
    i1=imm_convert(str(imm),str(12))
    value=i1+reg_codes[rs1]+isa_codes["jalr"]["f3"]+reg_codes[rd]+isa_codes["jalr"]["opcode"]
    return value

# S - type Functions
#same problem like B type
def sw(imm,rs2,rs1): # configure imms   ||   imm1 --> 11:5   ||  imm2 --> 4:0 
    si=imm_convert(str(imm),str(12))
    s1=si[-6::-1]
    s2=si[-1:-6:-1]
    value=s1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["sw"]["f3"]+s2+isa_codes["sw"]["opcode"]
    return value

# U - type
def lui(imm,rd): #configure imm  ||  31:12
    ui=imm_convert(str(imm),str(31))
    u1=ui[-12::-1]
    value=u1+reg_codes[rd]+isa_codes["lui"]["opcode"]
    return value
def auipc(imm,rd): #configure imm  ||  31:12
    ui=imm_convert(str(imm),str(31))
    u1=ui[-12::-1] 
    value=u1+reg_codes[rd]+isa_codes["auipc"]["opcode"]
    return value

# B - type      # configure imms   ||   imm1 --> 12|10:5   ||  imm2 --> 4:1|11
def beq(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["beq"]["f3"]+b2+isa_codes["beq"]["opcode"]
    return value
def bne(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bne"]["f3"]+b2+isa_codes["bne"]["opcode"]
    return value
def blt(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["blt"]["f3"]+b2+isa_codes["blt"]["opcode"]
    return  
def bge(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bge"]["f3"]+b2+isa_codes["bge"]["opcode"]
    return value
def bltu(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bltu"]["f3"]+b2+isa_codes["bltu"]["opcode"]
    return value
def bgeu(rs1,rs2,imm):
    bi=imm_convert(str(imm),str(12))
    b1=bi[-12]+bi[-5:-11:-1]
    b2=bi[-1:-5:-1]+bi[-11]
    value=b1+reg_codes[rs2]+reg_codes[rs1]+isa_codes["bgeu"]["f3"]+b2+isa_codes["bgeu"]["opcode"]
    return value

# J - type     #configure imm  ||  20|10:1|11|19:12
def jal(imm,rd):
    #imm=ans[19]+ans[9:0:-1]+ans[10]+ans[18:10:-1]
    ji=imm_convert(str(imm),str(20))  
    j1=ji[-20]+ji[-1:-11:-1]+ji[-11]+ji[-12:-20:-1]
    value=j1+reg_codes[rd]+isa_codes["jal"]["opcode"]
    return value

# Bonus - Type #       ||    still need to build these out
def mul():
    pass
def rst():
    pass
def halt():
    pass
def rvrs():
    pass

#function to create an integer into binary
    

reg_codes = { 
             "zero" : "00000",   # x0   
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
     "mul":{},
     "rst":{},
    "halt":{},
    "rvrs":{}
}

# instructions=list(isa_codes.keys())
# registers=list(reg_codes.keys())




# no_of_variables = len(list_of_variables)
# input_labels = []                                  
# jump_to_labels = []                                      
# input_register = []
# input_memory = []
# immediates = []



# file import of assembly code
with open("Assembly Program.txt","r") as f:
    data=f.readlines()


input_instruction = []
Output_instruction = []
counter=0

for instruction in data: #Gives me everthing required in a list
    instruct=instruction.rstrip()
    input_instruction[counter]=instruct.split()
    counter+=1

counter=1
for instruction in input_instruction:
    opperation=instruction[0]
    if opperation in isa_codes.keys(): #if a valid opperation
        op_type=isa_codes[opperation]["type"]
        if op_type=="r": #for all r type instructions
            rd,rs1,rs2=instruction[-1].split(",")
            Binary_Format=isa_codes[opperation]["function"](rs1,rs2,rd)
            Output_instruction.append(Binary_Format)
        elif op_type=="i": #for all i type instructions
            rd,rs,imm=instruction[-1].split(",")
            Binary_Format=isa_codes[opperation]["function"](imm,rs,rd)
            Output_instruction.append(Binary_Format)
        elif op_type=="s": #Should work fine ig
            rs2,imm_rs1=instruction[-1].split(",")
            imm,rs1=imm_rs1.split("(")
            rs1=rs1[:-2]
            Binary_Format=isa_codes[opperation]["function"](imm,rs2,rs1)
            Output_instruction.append(Binary_Format)
        elif op_type=="b": #for all b type instructions
            rs1,rs2,imm=instruction[-1].split(",")
            Binary_Format=isa_codes[opperation]["function"](rs1,rs2,imm)
            Output_instruction.append(Binary_Format)
        elif op_type=="u": #for all u type instructions
            rd,imm=instruction[-1].split(",")
            Binary_Format=isa_codes[opperation]["function"](imm,rd)
            Output_instruction.append(Binary_Format)
        elif op_type=="j": #for all j type instructions
            rd,imm=instruction[-1].split(",")
            Binary_Format=isa_codes[opperation]["function"](imm,rd)
            Output_instruction.append(Binary_Format)
        #bonus still left
    else: #give error of invalid opperation
        print(f"Invlid Instruction in line {counter}.")
        exit()
        
# creating a binary code text file
with open("Avengers Assembled.txt","w") as f:
    f.writelines(Output_instruction)



# #for I type
# ii=imm_convert(str(imm),str(12))
# i1=ii

# #for S type
# si=imm_convert(str(imm),str(12))
# s1=si[-6::-1]
# s2=si[-1:-6:-1]

# #for B type
# bi=imm_convert(str(imm),str(12))
# b1=bi[-12]+bi[-5:-11:-1]
# b2=bi[-1:-5:-1]+bi[-11]

# #for U type
# ui=imm_convert(str(imm),str(31))
# u1=ui[-12::-1]
        
# #for J type
# ji=imm_convert(str(imm),str(20))  
# j1=ji[-20]+ji[-1:-11:-1]+ji[-11]+ji[-12:-20:-1]

