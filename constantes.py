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
querys = [
    ["VI","ART","TABLA","CN","VALOR","CON","CM","VALOR"],
    ["VI","TABLA","CN","VALOR","CON","CM","VALOR"]
]
tokens = {
    "TABLA":{
        "grupo":[
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
        "estudiante":[
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
        "calificación":[
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
        "asistencia":[
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
        "hacer"
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
        "con"
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
for cm in list(tokens["CM"]):
    tokens["CM"].append(cm+"s")
for cn in list(tokens["CN"]):
    tokens["CN"].append(cn[:len(cn)-1]+"a")
for cn in list(tokens["CN"]):
    tokens["CN"].append(cn+"s")
for c in list(tokens["CON"]):
    for a in list(tokens["ART"]):
        tokens["CON"].append(c+" "+a)

print(tokens["CM"])

