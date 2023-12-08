Este es un programa analizador de sintaxis y lexico de un archivo .asm (MASM), se ejecuta mediante IDE o consola, aun no cuenta con archivo ejecutable.

Desarrollado con python 3.11.4

Archivo principal: editorTxt.py


Algunas consideraciónes de su funcionamiento:
    Trabaja con diccionarios de palabras reservadas del MASM 
    Emplea expresiones regulares (biblioteca "re")
    Los diccionarios se utilizan en la definicion de expresiones regulares para analisis de la sintaxis y del léxico 

Se han implementado las 3 fases solicitadas para la entrega del proyecto (fases 4 y 5 complementarias aun no desarrolladas):

    Fase 1: CRUD de un archivo .asm
    Fase 2: Identificación del .data y .code (segmento de datos y segmento de codigo)
    Fase 3: Analisis lexico-sintactico 
        Reconoce varias intrucciones como JMP LOOP MOV NEG SUB INC y otras.
        Debido a la amplio lexico de MASM si alguna instruccion no es reconocida debe:
            a) Agregarse o trabajar con los diccionarios en lexan.py
            b) Adaptar lexemean.py para que reconozca el lexema deseado
            c) Adaptar syntan.py para que este contemplada alguna sintaxis especifica del lexema deseado y sea clasificada como correcta




    		Ej
			
			destino:
				MOV ax,bx
				Jmp destino
				
			L1: mov ax,bx
            L2: mov ax,cx

    Fase 4: Direccionamiento de memoria
    Fase 5: Codificacion de instrucciones a codigo máquina


Protip: Para que el icono se pueda ver debe estar una carpeta fuera de donde esta todos estos scripts

Protip: Rama3 y rama "Main" se encuentran con la entrega final.