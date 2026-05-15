'''
Compiler for magistervivory language (.oll).
'''
import sys

# read arguments
program_filepath = sys.argv[1]

print("[CMD] Parsing")
################################
#      TOKENIZED PROGRAM       
################################

# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip() 
            for line in program_file.readlines()]

program = []
for line in program_lines:
    part = line.split(" ")
    opcode = part[0]
    

    # check for empty line
    if opcode == "":
        continue

    # store opcode token
    program.append(opcode)

    # handle each  opcode
    if opcode == "PUSH":
        # expecting  a number
        number = int(part[1])
        program.append(number)
    elif opcode == "PRINT":
        # excpecting string literal
        string_literal = ''.join(part[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0": 
        # read label  
        label = part[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        # read label 
        label_name = part[1]
        program.append(label)

# print(program)
print(program)