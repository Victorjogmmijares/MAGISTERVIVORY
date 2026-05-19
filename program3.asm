; --header--
bit 64
default rel
; variables --
section .bss
; -- contants --
section .data
string_literal_0: db "[[...], [...], [...], [...]]", 0
string_literal_1: db "[[...], [...], [...], [...]]", 0
string_literal_2: db "[[...], [...], [...], [...]]", 0
string_literal_3: db "[[...], [...], [...], [...]]", 0
; -- entry point --
section .text
global main
extern ExitProcess
extern printf
extern scanf
         
main:
	PUSH rbp
	MOV rbp, rsp
	SUB rsp, 32
; READ ---
; NOT IMPLEMENTED 
; --JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L2
; -- JUMP.GT.0 ---
	CMP qword [rsp], 0
	JG {label}
; --PRINT ---
	LEA rcx, [rel string_literal_0]
	XOR eax, eax
	CALL printf
; HALT ---
	JMP EXIT_LABEL
; -- Label ---
LO:
; -- PUSH ---
	PUSH 3
	POP rax
	SUB qword [rsp], rax
; --JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L1
; --PRINT ---
	LEA rcx, [rel string_literal_1]
	XOR eax, eax
	CALL printf
; HALT ---
	JMP EXIT_LABEL
; -- Label ---
L1:
; --PRINT ---
	LEA rcx, [rel string_literal_2]
	XOR eax, eax
	CALL printf
; HALT ---
	JMP EXIT_LABEL
; -- Label ---
L2:
; --PRINT ---
	LEA rcx, [rel string_literal_3]
	XOR eax, eax
	CALL printf
; HALT ---
	JMP EXIT_LABEL
EXIT_LABEL:
	XOR rax, rax
	CALL ExitProcess
