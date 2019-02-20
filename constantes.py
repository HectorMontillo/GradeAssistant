#!/usr/bin/python
# -*- coding: utf-8 -*-

#Logeo
ANCHO = 500
ALTO = 300
SIZE = (ANCHO,ALTO)
CAPTION = "GradeAssistant: Login"

#Index
ANCHO_I = 700
ALTO_I = 600
SIZE_I =(ANCHO_I,ALTO_I)
CAPTION_I = "GradeAssistant: Index"

#CrearGrupo
ANCHO_CG = 500
ALTO_CG = 300
SIZE_CG = (ANCHO_CG,ALTO_CG)
CAPTION_CG = "GradeAssistant: Crear Grupo"

#VistaGrupo
ANCHO_VG = 700
ALTO_VG = 600
SIZE_VG = (ANCHO_VG,ALTO_VG)
CAPTION_VG = "GradeAssistant: Grupo"

#Diccionarios de palabras y preguntas

words = [
    "grupo",
    "bando",
    "facción",
    "tribu",
    "legión",
    "familia",
    "comunidad",
    "equipo",
    "cuadrilla",
    "pandilla",
    "banda",
    "conjunto",
    "asosiación",
    "orden",
    "colectividad",
    "estudiante",
    "bachiller",
    "graduado",
    "licenciado",
    "docto",
    "experto",
    "entendido",
    "alúmno",
    "discípulo",
    "pupilo",
    "educando",
    "escolar",
    "colegial",

    "calificación",
    "nota",
    "puntuación",
    "evaluación",
    "apreciación",
    "valoración",
    "aptitud",
    "capacidad",
    "valor",
    "habilidad",
    "asistencia",
    "precencia",
    "comparecencia",
    "concurrencia",
    "concurso",
    "falta",

    "crear",
    "agregar",
    "asignar",
    "concebir",
    "establecer",
    "guardar",
    "instaurar",
    "formar",
    "elaborar",
    "inventar",
    "producir",
    "hacer",
    "dar",

    "uno",
    "un",
    "una",
    "el",
    "la",
    "unos",
    "unas",
    "los",
    "las",

    "para",
    "por",
    "con",
    "en",

    "llamado",
    "nombrado",
    "etiquetado",
    "citado",
    "mencionado",
    "denominado",
    "nominado",
    "proclamado",
    "designado",
    "ascendido",
    "colocado",

    "cédula",
    "identificacion",
    "id",
    "papel",
    "ficha",
    "documento",
    "tarjeta",
    "identidad",
    "tarjeta identidad",
    "cc",
    "ti",
    "credencial",
    "carné",

    "materia",
    "asignaruta",
    "disciplina",
    "tópico",
    "disciplina",

]
tokens = {
    "S":[
        "VI ART TABLA CN VALOR CART CM VALOR",
        "VI TABLA CN VALOR CON CM VALOR"
    ],
    "VALOR":[
        "#none"
    ],
    "CART":[
        "CON ART",
        "ART",
        "CON"
    ],
    "TABLA":{
        "GRU":[
            "grupo",
            "bando",
            "facción",
            "tribu",
            "legión",
            "familia",
            "comunidad",
            "equipo",
            "cuadrilla",
            "pandilla",
            "banda",
            "conjunto",
            "asosiación",
            "orden",
            "colectividad"
        ],
        "EST":[
            "estudiante",
            "bachiller",
            "graduado",
            "licenciado",
            "docto",
            "experto",
            "entendido",
            "alúmno",
            "discípulo",
            "pupilo",
            "educando",
            "escolar",
            "colegial"
        ],
        "CAL":[
            "calificación",
            "nota",
            "puntuación",
            "evaluación",
            "apreciación",
            "valoración",
            "aptitud",
            "capacidad",
            "valor",
            "habilidad"
        ],
        "ASI":[
            "asistencia",
            "precencia",
            "comparecencia",
            "concurrencia",
            "concurso",
            "falta"
        ]
    },
    "VI":[
        "crear",
        "agregar",
        "asignar",
        "concebir",
        "establecer",
        "guardar",
        "instaurar",
        "formar",
        "elaborar",
        "inventar",
        "producir",
        "hacer",
        "dar"
    ],
    "ART":[
        "uno",
        "un",
        "una",
        "el",
        "la",
        "unos",
        "unas",
        "los",
        "las"
    ],
    "CON":[
        "para",
        "por",
        "con",
        "en"
    ],
    "CN":[
        "llamado",
        "nombrado",
        "etiquetado",
        "citado",
        "mencionado",
        "denominado",
        "nominado",
        "proclamado",
        "designado",
        "ascendido",
        "colocado"
    ],
    "CID":[
        "cédula",
        "identificacion",
        "id",
        "papel",
        "ficha",
        "documento",
        "tarjeta",
        "identidad",
        "tarjeta identidad",
        "cc",
        "ti",
        "credencial",
        "carné",
    ],
    "CM":[
        "materia",
        "asignaruta",
        "disciplina",
        "tópico",
        "disciplina",
    ]

}
#------------------------------------------------
#Agregar prural a los tokens de tipo CampoMateria
for cm in list(tokens["CM"]):
    word = cm+"s"
    tokens["CM"].append(word)
    words.append(word)
#------------------------------------------------
#Agregar femenino a los tokens del tipo CampoNombre
for cn in list(tokens["CN"]):
    word = cn[:len(cn)-1]+"a"
    tokens["CN"].append(word)
    words.append(word)
#------------------------------------------------
#Agregar plural a los tokens del tipo CampoNombre
for cn in list(tokens["CN"]):
    word = cm+"s"
    tokens["CN"].append(word)
    words.append(word)

#Funcion que genera archivo fcfg para la gramatica, a partir del diccionario tokens
def FCFG_Generador():
    f = open("gramatica.fcfg", 'w',encoding='utf-8')
    gramatica = "% start S\n" 
    for t in tokens:
        gramatica += t+" -> "
        for i in tokens[t]:
            if i.islower():
                gramatica += "'"+i+"' | "
            else:
                gramatica += i+" | "
        gramatica = gramatica[:-2] + "\n"
        if isinstance(tokens[t],dict):
            for i in tokens[t]:
                gramatica += i+" -> "
                for j in tokens[t][i]:
                    gramatica += "'"+j+"' | "
                gramatica = gramatica[:-2] + "\n"
    f.write(gramatica)
    f.close()

#se genera el archivo gramatica.fcfg y se abre como lectura
FCFG_Generador()
filegrammar = open("gramatica.fcfg","r")

'''
from nltk import CFG
from nltk.parse import RecursiveDescentParser


f = open("gramatica.fcfg","r")
grammar = CFG.fromstring(f.read())
f.close()
rd = RecursiveDescentParser(grammar)
#print(grammar._productions)
sentence1 = 'crear un grupo llamado #none para materia #none'.split()
for t in rd.parse(sentence1):
    print(t.productions()[0].rhs())
    #print(t.remove('S'))
    #print("fila : "+str(t))

'''