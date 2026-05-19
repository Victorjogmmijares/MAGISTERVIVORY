'''
Compiler for magistervivory language (.oll).
'''
import sys
import os

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

'''
Book keep string  literals
'''
string_literals = []
for ip in range(len(program)):
    if program[ip] == "PRINT":
        string_literal = program[ip+1]
        program[ip+1] = len(string_literals)
        string_literals.append(string_literals)

'''
Compile to assembly
'''

asm_filepath = program_filepath[:-4 ] + ".asm"
out = open(asm_filepath, "w")

out.write("""; --header--
bit 64
default rel
""")

out.write("""; variables --
section .bss
""")


out.write("""; -- contants --
section .data
""")
for i, string_literal in enumerate(string_literals):
    out.write(f'string_literal_{i}: db "{string_literal}", 0\n')

out.write("""; -- entry point --
section .text
global main
extern ExitProcess
extern printf
extern scanf
         
main:
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
""")

ip = 0
while ip < len(program):
    opcode = program[ip]
    ip += 1
        
    if  opcode.endswith (":"):
        out.write(f"; -- Label ---\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip += 1

        out.write(f"; -- PUSH ---\n")
        out.write(f"\tPUSH {number}\n")
    elif opcode == "POP": 
        out.opcode(f": -- POP ---\n")
        out.write(f"\tPOP\n")
    elif opcode == "ADD":
        out.write(f"\tPOP rax\n")
        out.write(f"\tADD qword [rsp], rax\n")
    elif opcode == "SUB":
        out.write(f"\tPOP rax\n")
        out.write(f"\tSUB qword [rsp], rax\n")
    elif opcode == "PRINT":
        string_literal_index = program[ip]
        ip += 1

        out.write("; --PRINT ---\n")
        out.write(f"\tLEA rcx, [rel string_literal_{string_literal_index}]\n")
        out.write(f"\tXOR eax, eax\n")
        out.write(f"\tCALL printf\n")
    elif opcode == "READ":
        out.write(f"; READ ---\n")
        out.write("; NOT IMPLEMENTED \n")

    elif opcode == "JUMP.EQ.0":
        label = program[ip]
        ip += 1
        out.write("; --JUMP.EQ.0 ---\n")
        out.write("\tCMP qword [rsp], 0\n")
        out.write(f"\tJE {label}\n")
    
    elif opcode == "JUMP.GT.0":
        label = program[ip]
        ip += 1
            
        out.write(f"; -- JUMP.GT.0 ---\n")
        out.write("\tCMP qword [rsp], 0\n")
        out.write("\tJG {label}\n")
    elif opcode == "HALT":
        out.write(f"; HALT ---\n")
        out.write("\tJMP EXIT_LABEL\n")

out.write("EXIT_LABEL:\n")
out.write("\tXOR rax, rax\n")
out.write("\tCALL ExitProcess\n")



out.close

print("[CMD] Assembling")
os.system(f"nasm -f elf64 {asm_filepath}")
print("[CMD] Linking")
os.system(f"gcc -o {asm_filepath[:-4] +'.exe'} {asm_filepath[:-3]+'o'}")

print("[CMD] Running")
os.system(f"{asm_filepath[:-4] +'.exe'}")