; test.ams -- Practica 1: operacion 5+9*7-10*5-3

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.DATA
sum DWORD ?
suma DWORD 12

.code
main proc
    mov eax,9
    mov ebx,10
    imul eax,7
    imul ebx,5
    mov ecx,5
    add eax,ecx
    sub eax,ebx
    sub eax,3
    add eax,1
    div eax,2
    invoke ExitProcess, 0

main endp
end main