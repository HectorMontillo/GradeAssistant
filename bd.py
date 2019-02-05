from peewee import *

database = SqliteDatabase('DATABASE')

class BaseModel(Model):
    class Meta:
        database = database

class Usuarios(BaseModel):
    Cedula_Usuario = IntegerField(primary_key =True)
    Contrasena = CharField()

class Grupos(BaseModel):
    ID_Grupo = IntegerField(primary_key =True)
    Nombre = CharField()
    Materia = CharField()
    Cedula_Usuario = ForeignKeyField(Usuarios, backref='cedula_usuario')

class Estudiantes(BaseModel):
    ID_Estudiante = IntegerField(primary_key =True)
    Nombre = CharField()

class GrupoEstudiante(BaseModel):
    ID_GrupoEstudiante = IntegerField(primary_key =True)
    ID_Estudiante = ForeignKeyField(Estudiantes, backref='id_estudiante')
    ID_Grupo = ForeignKeyField(Grupos, backref='id_grupo')

class Asistencias(BaseModel):
    ID_Asistencia = IntegerField(primary_key =True)
    Dia = IntegerField()
    Valor = BooleanField()
    ID_Estudiante = ForeignKeyField(Estudiantes, backref='id_estudiante')

class Calificaciones(BaseModel):
    ID_Calificaion = IntegerField(primary_key =True)
    Nombre = CharField()
    Valor = FloatField()
    ID_Estudiante = ForeignKeyField(Estudiantes,backref='id_estudiante')

def InizialarBD():
    #database.connect()
    database.create_tables([Usuarios, Grupos, Estudiantes, GrupoEstudiante, Asistencias, Calificaciones])


if __name__=="__main__":
    InizialarBD()
    #database.connect()
    Saulo = Usuarios(Cedula_Usuario=123,Contrasena='123')
    Saulo.save()
    #Angel = Usuarios.create(124,123)

    query = Usuarios.select()
    for i in query:
        print(i)

