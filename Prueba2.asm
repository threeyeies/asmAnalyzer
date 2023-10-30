; test.ams -- Practica 1: operacion 5+9*7-10*5-3

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.DATA
sum DWORD ?
suma DWORD +12d
cadena DWORD 'Esto es una cadena con comillas simples'
cadena2 DWORD "Esto es una cadena con comillas dobles"
cadena3 DWORD "Hola"
cadena4 DWORD 'Mundo'
var1 DWORD -3
rvar1 DD +1.2
rvar2 DQ -3.2


.code
main proc
destino:
    mov eax,9h
    mov ebx,10b
    imul eax,7q
    imul ebx,5o
    mov ecx,5r
    add eax,ecx
    sub eax,ebx
    sub eax,3t
    add eax,1y
    div eax,2
    invoke ExitProcess, 0

main endp
end main
