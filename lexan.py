# lexic analysis: diccionarios de palabras reservadas


# Diccionario para mnemónicos de instrucción
MNEMONICS = {
    'MOV': 'MOV',
    'ADD': 'ADD',
    'SUB': 'SUB',
    'MUL': 'MUL',
    'IMUL': 'IMUL',
    'IDIV': 'IDIV',
    'DIV': 'DIV',
    'INC': 'INC',
    'DEC': 'DEC',
    'AND': 'AND',
    'OR': 'OR',
    'XOR': 'XOR',
    'CMP': 'CMP',
    'JMP': 'JMP',
    'CALL': 'CALL',
    'RET': 'RET',
    'PUSH': 'PUSH',
    'POP': 'POP',
}


# Diccionario para directivas
DIRECTIVES = {
    '.SEGMENT': '.SEGMENT',
    '.END': '.END',
    'ENDS': 'ENDS',
    'ENDP': 'ENDP',
    'ORG': 'ORG',
    'DB': 'DB',
    'DW': 'DW',
    'DD': 'DD',
    'DT': 'DT',
    'DQ': 'DQ',
    'INCLUDE': 'INCLUDE',
    'EQU': 'EQU',
    '.DATA': '.DATA',
    '.CODE': '.CODE',
    'BYTE': 'BYTE',
    'WORD': 'WORD',
    'DWORD': 'DWORD',
    '.END': '.END',
    '.PROC': '.PROC',
    'PTR': 'PTR',
    'OFFSET': 'OFFSET',
    'EXTERN': 'EXTERN',
    'PUBLIC': 'PUBLIC',
    '.386':'.386',
    '.STACK':'.STACK',
    '.MODEL':'.MODEL',
    '.CONST':'.CONST',
    'FLAT':'FLAT',
    'STDCALL':'STDCALL',
    '4096':'4096',
}

MACROS_AND_FUNTIONS = {
    'invoke': 'invoke',
    'ExitProcess': 'ExitProcess'
}

# Diccionario para registros
REGISTERS = {
    'EAX': 'EAX',
    'EBX': 'EBX',
    'ECX': 'ECX',
    'EDX': 'EDX',
    'ESI': 'ESI',
    'EDI': 'EDI',
    'ESP': 'ESP',
    'EBP': 'EBP',
    # ... otros registros ...
}

# Diccionario de constantes o literales enteras
INT_CONSTANTS = {
    'hex': 'h',
    'oct1': 'q',
    'oct2': 'o',
    'dec': 'd',
    'bin': 'b',
    'real encoded': 'r',
    'alternative dec': 't',
    'alternative bin': 'y'

}


# Diccionario para etiquetas
LABELS = {
    'loop_start': 'loop_start',
    'data_section': 'data_section',
    'code_section': 'code_section',
    'main': 'main',
    'end':'end',
    'proc':'proc',
    ':': ':',
}



