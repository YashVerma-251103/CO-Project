import sys

def int_to_bin(n,k):
    number = bin(n)[2:]
    number = number.zfill(k)  
    return str(number)

memory_dump = []
memory_address = {}
for i in range(128):
    memory_address[i] = [0,0]
registers = {}
ProgCounter = 0
for i in range(7):
    temp = str(int_to_bin(i,3))
    registers[temp] = 0
registers["111"] = [0,0]

data_list = sys.stdin.readlines()            

for counter in range(len(data_list)):
    data_list[counter]=data_list[counter].rstrip()
    data_list[counter] = data_list[counter].split()


no_of_lines = len(data_list)

data = []
for i in range(no_of_lines):
    data.append(data_list[i][0])

for i in range(no_of_lines):
    memory_dump.append(data[i])

while(True):
    line = data[ProgCounter]
    temp = []
    temp.append(int_to_bin(ProgCounter,7))
    opCode = line[:5:]
    if opCode == "11010": #Halt
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        print(int_to_bin(0,16))
        break
    elif opCode == "00000": #Add
        r1 = line[7:10:]
        r2 = line[10:13]
        r3 = line[13::]
        temp_sum = registers[r2] + registers[r3]
        if (temp_sum > 2**16 - 1 or temp_sum < 0):
            registers[r1] = 0
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
        else:
            registers[r1] = temp_sum
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00001": # Sub
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        temp_diff = registers[r2] - registers[r3]
        if temp_diff > 2**16 - 1 or temp_diff < 0:
            registers[r1] = 0
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
        else:
            registers[r1] = temp_diff
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00110": #Mult
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        temp_prod = registers[r2] * registers[r3]
        if temp_prod > 2**16 - 1 or temp_prod < 0:
            registers[r1] = 0
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
        else:
            registers[r1] = temp_prod
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01010": #Bitwise XOR
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16)
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) ^ int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01011": #Bitwise OR
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16)
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) | int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01100": #Bitwise AND
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:]
        a = int_to_bin(registers[r2],16)
        b = int_to_bin(registers[r3],16)
        c = []
        for i in range(16):
            c.append(0)
        for i in range(16):
            c[i] = str(int(a[0]) & int(b[0]))
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00010": #Move immediate
        r1 = line[6:9]
        imm = line[9::]
        tem = int(imm,2)
        registers[r1] = tem
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01001": #left shift
        r1 = line[6:9]
        imm = line[9::]
        b = int(imm,2)
        a = registers[r1]
        temp_ans = int(a*(2**b))
        if temp_ans > 2**16 - 1 or temp_ans < 0:
            registers[r1] = 0
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
        else:
            registers[r1] = temp_ans
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "01000": #right shift
        r1 = line[6:9]
        imm = line[9::]
        b = int(imm,2)
        a = registers[r1]
        temp_ans = int(a/(2**b))   #edge case not handled here
        if temp_ans > 2**16 - 1 or temp_ans < 0:
            registers[r1] = 0
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
        else:
            registers[r1] = temp_ans
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00011": # Move register
        r1 = line[10:13:]
        r2 = line[13::]
        if r2 == "111":
            registers[r1] = registers[r2][0]
        elif r1 == "111":
            registers[r1][0] = registers[r2]
        else:
            registers[r1] = registers[r2]
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"], 16), end=" ")
        print(int_to_bin(registers["001"], 16), end=" ")
        print(int_to_bin(registers["010"], 16), end=" ")
        print(int_to_bin(registers["011"], 16), end=" ")
        print(int_to_bin(registers["100"], 16), end=" ")
        print(int_to_bin(registers["101"], 16), end=" ")
        print(int_to_bin(registers["110"], 16), end=" ")
        if registers["111"][0] == 0:
            print(int_to_bin(0, 16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0, 16))
        else:
            ans = "0" * 12 + "1" + 3 * "0"
            print(ans)

        ProgCounter += 1
    elif opCode == "00111": #Divide
        r3 = line[10:13:]
        r4 = line[13::]
        a = registers[r3]
        b = registers[r4]
        if (b == 0):
            registers["111"][0] = 4
            registers["111"][1] = ProgCounter
            registers["000"] = 0
            registers["001"] = 0
        else:
            quotient = a//b
            remainder = a%b
            registers["000"] = quotient
            registers["001"] = remainder
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)
        ProgCounter += 1
       
    elif opCode == "01101": #invert
        r1 = line[10:13:]
        r2 = line[13::]
        c = []
        for i in range(16):
            c.append(0)
        a = int_to_bin(registers[r2],16)
        for i in range(16):
            if a[i] == "0":
                c[i] = "1"
            else:
                c[i] = "0"
        ans = ""
        for i in range(16):
            ans += c[i]
        registers[r1] = int(ans,2)
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)
        ProgCounter += 1
    elif opCode == "01110": #Compare
        r1 = line[10:13:]
        r2 = line[13::]
        a = registers[r1]
        b = registers[r2]
        if  a > b:
            registers["111"][0] = 2
            registers["111"][1] = ProgCounter
        elif a == b:
            registers["111"][0] = 1
            registers["111"][1] = ProgCounter
        else:
            registers["111"][0] = 3
            registers["111"][1] = ProgCounter
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        elif registers["111"][0] == 3:
            ans = "0"*13 + "1" + "0"*2
            print(ans)
        elif registers["111"][0] == 2:
            ans = "0" * 14 + "1" + "0"
            print(ans)
        elif registers["111"][0] == 1:
            ans = "0" * 15 + "1"
            print(ans)
        else:
            ans = "0" * 12 + "1" + "0"*3
            print(ans)
        ProgCounter += 1
    elif opCode == "00100": #Load
        r1 = line[6:9:]
        mem = line[9::]
        address = int(mem,2)     #prone to error
        registers[r1] = memory_address[address][0]
       
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)
        ProgCounter += 1
    elif opCode == "00101": #Store
        r1 = line[6:9:]
        mem = line[9::]
        address = int(mem,2)
        memory_address[address][0] = registers[r1]
        memory_address[address][1] = 1
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)
        ProgCounter += 1
    elif opCode == "01111": #Unconditional Jump
        mem = line[9::]
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 0):
            print(int_to_bin(0,16))
        elif registers["111"][1] != ProgCounter:
            registers["111"][0] = 0
            print(int_to_bin(0,16))
        else:
            ans = "0"*12 + "1" + 3*"0"
            print(ans)
        ProgCounter = int(mem,2)
    elif opCode == "11100": #Less than jump
        mem = line[9::]
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 3):
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter = int(mem,2)
        else:
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter+=1
    elif opCode == "11111": #Equal to jump
        mem = line[9::]
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 1):
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter = int(mem,2)
        else:
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter+=1
    elif opCode == "11101": #Greater than jump
        mem = line[9::]
        print(temp[0],end = "        ")
        print(int_to_bin(registers["000"],16),end = " ")
        print(int_to_bin(registers["001"],16),end = " ")
        print(int_to_bin(registers["010"],16),end = " ")
        print(int_to_bin(registers["011"],16),end = " ")
        print(int_to_bin(registers["100"],16),end = " ")
        print(int_to_bin(registers["101"],16),end = " ")
        print(int_to_bin(registers["110"],16),end = " ")
        if (registers["111"][0] == 2):
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter = int(mem,2)
        else:
            if (registers["111"][0] == 0):
                print(int_to_bin(0,16))
            elif registers["111"][1] != ProgCounter:
                registers["111"][0] = 0
                print(int_to_bin(0,16))
            else:
                ans = "0"*12 + "1" + 3*"0"
                print(ans)
            ProgCounter+=1
    else:
        break

for i in memory_address.keys():
    if memory_address[i][1] == 1:
        memory_dump.append(int_to_bin(memory_address[i][0],16))

pussy = len(memory_dump)

for i in range(128 - pussy):
    memory_dump.append("0"*16)

for i in range(128):
    print(memory_dump[i])
