import sys

def add(r1,r2,r3):
    val = isa_codes["add"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def sub(r1,r2,r3):
    val = isa_codes["sub"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def mov(r1,r2,flg):
    if flg:
        val =  isa_codes["movr"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    else:
        val =  isa_codes["movi"]["opcode"]+"0"+reg_codes[r1]
        r2 = str(bin(int(r2[1:]))).lstrip("0b")
        if (len(r2) != 7):
            for i in range (0,7-len(r2),1):
                val +="0"
        val += r2
    return val

def ld(r1,mem_add):
    alpha = ""
    if len(mem_add) !=7:
        for i in range(7-len(mem_add)):
            alpha+="0"
    mem_add = alpha+mem_add
    val = isa_codes["ld"]["opcode"]+"0"+reg_codes[r1]+mem_add
    return val

def st(r1,mem_add):
    alpha = ""
    if len(mem_add) !=7:
        for i in range(7-len(mem_add)):
            alpha+="0"
    mem_add = alpha+mem_add
    val = isa_codes["st"]["opcode"]+"0"+reg_codes[r1]+mem_add
    return val

def rs(r1,r2):
    val = isa_codes["rs"]["opcode"]+"0"+reg_codes[r1]
    r2 = str(bin(int(r2[1:]))).lstrip("0b")
    if (len(r2) != 7):
        for i in range (0,7-len(r2),1):
            val += "0"
    val += r2

def ls(r1,r2):
    val = isa_codes["ls"]["opcode"]+"0"+reg_codes[r1]
    r2 = str(bin(int(r2[1:]))).lstrip("0b")
    if (len(r2) != 7):
        for i in range (0,7-len(r2),1):
            val += "0"
    val += r2

def mul(r1,r2,r3):
    val = isa_codes["mul"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def div(r1,r2):
    val = isa_codes["div"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def xor(r1,r2,r3):
    val = isa_codes["xor"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def or_(r1,r2,r3):
    val = isa_codes["or"]["opcode"]+"00"+reg_codes[r1]+reg_codes[r2]+reg_codes[r3]
    return val

def and_(e1,e2,e3):
    val = isa_codes["and"]["opcode"]+"00"+reg_codes[e1]+reg_codes[e2]+reg_codes[e3]
    return val

def not_(r1,r2):
    val = isa_codes["not"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def cmp(r1,r2):
    val = isa_codes["cmp"]["opcode"]+"00000"+reg_codes[r1]+reg_codes[r2]
    return val

def hlt():
    val = isa_codes["hlt"]["opcode"]+"00000000000"
    return val

def jmp(r1):
    val = isa_codes["jmp"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def jlt(r1):
    val = isa_codes["jlt"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def jgt(r1):
    val = isa_codes["jgt"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val
def je(r1):
    val = isa_codes["je"]["opcode"]+"0000"
    r = label_checker[r1]
    if (len(r) != 7):
        for i in range (0,7-len(r),1):
            val += "0"
    val += r
    return val

def variable_starting(no_of_var,lines):
    if sum(lines) != int((no_of_var)*(no_of_var+1)/2):
        return False
    else:
        return True

def correct_usage_of_halt(input_instruction):
    occurence_of_halt = input_instruction.count("hlt")
    if occurence_of_halt == 1:
        index_of_halt = input_instruction.index("hlt")
    last_index = len(input_instruction) - 1

    if occurence_of_halt == 1 and index_of_halt == last_index:
        return True
    elif occurence_of_halt == 0:
        return "Error: Halt function is absent"
    elif occurence_of_halt == 1 and index_of_halt < last_index:
        return "Error: Lines of code present after the halt function"
    else:
        return "Error: Multiple halt functions are present"

def valid_immediate(immediate):
    flag = True
    for i in range(1,len(immediate)):
        if immediate[i].isdigit() == False:
            flag = "is not a valid immediate"
            break
    try:
        if int(immediate[1::]) < 0 or int(immediate[1::]) >127:
            return " can't be represented as a 7 bit binary number"
        return flag
    except:
        return flag

def valid_memory(memory):
    if len(memory) != 7:
        return "does not have a valid memory length"
    else:
        flag = True
        for i in range(len(memory)):
            if memory[i] != "1" and memory[i] != "0":
                flag = "is not a valid memory address"
                break
        return flag
reg_codes = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
isa_codes = {
        "add" : {"opcode" : "00000", "type" : "a"},
        "sub" : {"opcode" : "00001", "type" : "a"},
        "movi" : {"opcode" : "00010", "type" : "b"},
        "movr" : {"opcode" : "00011", "type" : "c"},
        "ld" : {"opcode" : "00100", "type" : "d"},
        "st" : {"opcode" : "00101", "type" : "d"},
        "mul" : {"opcode" : "00110", "type" : "a"},
        "div" : {"opcode" : "00111", "type" : "c"},
        "rs" : {"opcode" : "01000", "type" : "b"},
        "ls" : {"opcode" : "01001", "type" : "b"},
        "xor" : {"opcode" : "01010", "type" : "a"},
        "or" : {"opcode" : "01011", "type" : "a"},
        "and" : {"opcode" : "01100", "type" : "a"},
        "not" : {"opcode" : "01101", "type" : "c"},
        "cmp" : {"opcode" : "01110", "type" : "c"},
        "jmp" : {"opcode" : "01111", "type" : "e"},
        "jlt" : {"opcode" : "11100", "type" : "e"},
        "jgt" : {"opcode" : "11101", "type" : "e"},
        "je" : {"opcode" : "11111", "type" : "e"},
        "hlt" : {"opcode" : "11010", "type" : "f"}}

list_of_instructions = list(isa_codes.keys())

list_of_registers = list(reg_codes.keys())

       
data = sys.stdin.readlines()
data_1 = data.copy()

for counter in range(len(data)):
    data[counter]=data[counter].rstrip()
    data[counter] = data[counter].split()

no_of_lines = len(data)
list_of_variables = []                              
line_when_variable_added = []                      
for counter in range(len(data)):
    if data[counter][0] == "var":
        list_of_variables.append(data[counter][1])
        line_when_variable_added.append(counter+1)
no_of_variables = len(list_of_variables)

input_labels = []                                  
jump_to_labels = []                                      
input_register = []
input_memory = []
input_instruction = []
immediates = []

for counter in range(len(data)):  
    try:                                                                                            
        if data[counter][0][len(data[counter][0])-1] == ":":                                        
            input_labels.append(data[counter][0][0:len(data[counter][0])-1:])                        
            input_instruction.append(data[counter][1])                                              
            if data[counter][1] == "mov"or data[counter][1] == "movi" or data[counter][1] == "movr":
                if data[counter][3] in list_of_registers:
                    input_register.append(data[counter][2])
                    input_register.append(data[counter][3])
                else:
                    input_register.append(data[counter][2])
                    immediates.append(data[counter][3][1::])
            elif isa_codes[data[counter][1]]["type"] == "a":                                                                  
                input_register.append(data[counter][2])
                input_register.append(data[counter][3])
                input_register.append(data[counter][4])
            elif isa_codes[data[counter][1]]["type"] == "b":
                input_register.append(data[counter][2])
                immediates.append(data[counter][3][1::])
            elif isa_codes[data[counter][1]]["type"] == "c":
                input_register.append(data[counter][2])
                input_register.append(data[counter][3])
            elif isa_codes[data[counter][1]]["type"] == "d":
                input_register.append(data[counter][2])
                input_memory.append(data[counter][3])
            elif isa_codes[data[counter][1]]["type"] == "e":
                jump_to_labels.append(data[counter][2])
            else:
                continue
        else:
            input_instruction.append(data[counter][0])
            if data[counter][0] == "mov" or data[counter][0] == "movi" or data[counter][0] == "movr" :
                if data[counter][2] in list_of_registers:
                    input_register.append(data[counter][1])
                    input_register.append(data[counter][2])
                else:
                    input_register.append(data[counter][1])
                    immediates.append(data[counter][2][1::])
            elif isa_codes[data[counter][0]]["type"] == "a":
                    input_register.append(data[counter][1])
                    input_register.append(data[counter][2])
                    input_register.append(data[counter][3])
            elif isa_codes[data[counter][0]]["type"] == "b":
                input_register.append(data[counter][1])
                immediates.append(data[counter][2][1::])
            elif isa_codes[data[counter][0]]["type"] == "c":
                input_register.append(data[counter][1])
                input_register.append(data[counter][2])
            elif isa_codes[data[counter][0]]["type"] == "d":
                input_register.append(data[counter][1])
                input_memory.append(data[counter][2])
            elif isa_codes[data[counter][0]]["type"] == "e":
                jump_to_labels.append(data[counter][1])
            else:
                continue
    except:
            continue

if variable_starting(no_of_variables,line_when_variable_added) == False:
    print("Error: Variables must be declared at the beginning")

if correct_usage_of_halt(input_instruction) != True:
    print(correct_usage_of_halt(input_instruction))

pussy = 1

for i in range(no_of_lines):
    base = 0
    if data[i][0][len(data[i][0])-1] == ":":
        base += 1
    instruct = data[i][base]
    if instruct == "mov":
        if data[i][base+2][0] == "$":
            instruct = "movi"
        else:
            instruct = "movr"
    if instruct == "var":
        continue
    elif instruct not in list_of_instructions:
        print(f"Error in Line-{i+1}: {instruct} is not defined")
        pussy = 0
    else:
        typ = isa_codes[instruct]["type"]
        if typ == "a":
            nos = len(data[i]) - base
            if nos != 4:
                print(f"Error in Line-{i+1}: Invalid number of registers")
                pussy = 0
            else:
                if data[i][base+1] not in list_of_registers:
                    print(f"Error in Line-{i+1}: {data[i][base+1]} is not a valid register")
                    pussy = 0
                if data[i][base+2] not in list_of_registers:
                    print(f"Error in Line-{i+1}: {data[i][base+2]} is not a valid register")
                    pussy = 0
                if data[i][base+3] not in list_of_registers:
                    print(f"Error in Line-{i+1}: {data[i][base+3]} is not a valid register")
                    pussy = 0
        elif typ == "b":
            nos = len(data[i]) - base
            if nos != 3:
                print(f"Error in Line-{i+1}: Invalid number of arguments")
                pussy = 0
            else:
                if data[i][base+1] not in list_of_registers:
                    print(f"Error in Line-{i+1}: {data[i][base+1]} is not a valid register")
                    pussy = 0
                if data[i][base+2][0] != "$":
                    print(f"Error in Line-{i+1}: {data[i][base+2][0]} is not a valid immediate")
                    pussy = 0
                else:
                    if valid_immediate(data[i][base+2]) != True:
                        print(f"Error in Line-{i+1}: {data[i][base+2]} {valid_immediate(data[i][base+2])}")
                        pussy = 0
        elif typ == "c":
            nos = len(data[i]) - base
            if nos != 3:
                print(f"Error in Line-{i+1}: Invalid number of arguments")
                pussy = 0
            else:
                if instruct == "movr":
                    if data[i][base+1] not in list_of_registers:
                        print(f"Error in Line-{i+1}: {data[i][base+1]} is not a valid register")
                        pussy = 0
                    if data[i][base+2] not in list_of_registers and data[i][base+2] != "FLAGS":
                        print(f"Error in Line-{i+1}: {data[i][base+2]} is not a valid register")
                        pussy = 0
                else:
                    if data[i][base+1] not in list_of_registers:
                        print(f"Error in Line-{i+1}: {data[i][base+1]} is not a valid register")
                        pussy = 0
                    if data[i][base+2] not in list_of_registers:
                        print(f"Error in Line-{i+1}: {data[i][base+2]} is not a valid register")
                        pussy = 0
        elif typ == "d":
            nos = len(data[i]) - base
            if nos != 3:
                print(f"Error in Line-{i+1}: Invalid number of arguments")
                pussy = 0
            else:
                if data[i][base+1] not in list_of_registers:
                    print(f"Error in Line-{i+1}:{data[i][base+1]} is not a valid register ")
                    pussy = 0
                if data[i][base + 2] not in list_of_variables and valid_memory(data[i][base + 2]) != True:
                    print(f"Error in Line-{i+1}: {data[i][base+2]} is not a valid variable name or memory location")
                    pussy = 0
        elif typ == "e":
            nos = len(data[i]) - base
            if nos != 2:
                print(f"Error in Line-{i+1}: Invalid number of arguments")
                pussy = 0
            else:
                if data[i][base+1] not in input_labels and valid_memory(data[i][base + 1]) != True :
                    print(f"Error in Line-{i+1}: {data[i][base+1]} is not a valid address")
                    pussy = 0
        elif typ == "f":
            nos = len(data[i]) - base
            if nos != 1:
                print(f"Error in Line-{i+1}: Invalid number of arguments")
                pussy = 0

if pussy == 1:
   
    m= []
    for i in range(0,127) :
        x = str(bin(i)).lstrip("0b")
        m.append(x)

    label_checker = {}        
    var_name = {}              
    count_counter = var_count = count_empty = 0

    for i in data_1:
        if i != "\n":
            final_list = [x for x in i.split()]
            if final_list[0][-1] == ":":
                final_list = final_list[1:]
            if final_list != []:
                if final_list[0] == "var":
                    var_count += 1
            else:
                count_empty += 1
        else:
            count_empty += 1

    length = len(data_1) - var_count - count_empty

    for i in data_1:
        if i == "\n":
            continue
        else:
            final_list = [x for x in i.split()]
            if final_list[0] == "var" :
                var_name[final_list[1]] = m[count_counter + length]  
            if final_list[0][-1] == ":" :
                label_checker[final_list[0][0:-1]] = m[count_counter - var_count]
                final_list = final_list[1:]
            if final_list != []:
                count_counter += 1

    test = []
    for i in data_1:
        flag = True
        val = ""
        if i == "\n":
            flag = False
            pass
        else:
            final_list = [x for x in i.split()]
            if final_list[0] == "var":
                flag = False
                pass
            if final_list[0][-1] == ":" :
                final_list = final_list[1:]
            if final_list == []:
                flag = False
                pass
            elif final_list[0] == "add":
                val = add(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "sub":
                val = sub(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "mov":
                t = True
                if final_list[2][0] == "$":
                    t = False
                val = mov(final_list[1],final_list[2],t)
            elif final_list[0] == "ld":
                temp=var_name[final_list[2]]
                val = ld(final_list[1],temp)
            elif final_list[0] == "st":
                temp=var_name[final_list[2]]
                val = st(final_list[1],temp)
            elif final_list[0] == "mul":
                val = mul(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "div":
                val = div(final_list[1],final_list[2])
            elif final_list[0] == "rs":
                val = rs(final_list[1],final_list[2])
            elif final_list[0] == "ls":
                val = ls(final_list[1],final_list[2])
            elif final_list[0] == "xor":
                val = xor(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "or":
                val = or_(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "and":
                val = and_(final_list[1],final_list[2],final_list[3])
            elif final_list[0] == "not":
                val = not_(final_list[1],final_list[2])
            elif final_list[0] == "cmp":
                val = cmp(final_list[1],final_list[2])
            elif final_list[0] == "jmp":
                val = jmp(final_list[1])
            elif final_list[0] == "jlt":
                val = jlt(final_list[1])
            elif final_list[0] == "jgt":
                val = jgt(final_list[1])
            elif final_list[0] == "je":
                val = je(final_list[1])
            elif final_list[0] == "hlt":
                val = hlt()
        if flag == True:
            print(val)
