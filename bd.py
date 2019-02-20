import peewee
from playsound import playsound
db = peewee.SqliteDatabase('Aplicacion.db')

class Usuarios(peewee.Model):
    Cedula_Usuario = peewee.IntegerField(primary_key=True)
    Contrasena = peewee.CharField()
    class Meta:
        database=db
        db_table='usuarios'

class Estudiantes(peewee.Model):
    ID_Estudiante = peewee.IntegerField(primary_key =True)
    Nombre = peewee.CharField()
    class Meta:
        database=db
        db_table = 'estudiantes'

class Grupos(peewee.Model):
    ID_Grupo = peewee.IntegerField(primary_key =True)
    Nombre = peewee.CharField()
    Materia = peewee.CharField()
    Cedula_Usuario = peewee.ForeignKeyField(Usuarios, backref='cedula_usuario')
    class Meta:
        database=db
        db_table = 'grupos'

class GrupoEstudiante(peewee.Model):
    ID_GrupoEstudiante = peewee.IntegerField(primary_key =True)
    ID_Estudiante = peewee.ForeignKeyField(Estudiantes, backref='id_estudiante')
    ID_Grupo = peewee.ForeignKeyField(Grupos, backref='id_grupo')
    class Meta:
        database=db
        db_table = 'grupo_estudiantes'

class Asistencias(peewee.Model):
    ID_Asistencia = peewee.IntegerField(primary_key =True)
    Dia = peewee.IntegerField()
    ID_Grupo = peewee.ForeignKeyField(Grupos, backref='id_grupo')
    class Meta:
        database=db
        db_table = 'asistencias'

class AsistenciasEstudiantes(peewee.Model):
    ID_AsistenciaEstudiante = peewee.IntegerField(primary_key =True)
    Valor = peewee.BooleanField(null=True)
    ID_Estudiante = peewee.ForeignKeyField(Estudiantes, backref='id_estudiante')
    ID_Asistencia = peewee.ForeignKeyField(Asistencias, backref='id_asistencia')
    class Meta:
        database=db
        db_table = 'asistencias_estudiantes'


class Calificaciones(peewee.Model):
    ID_Calificaion = peewee.IntegerField(primary_key =True)
    Nombre = peewee.CharField()
    ID_Grupo = peewee.ForeignKeyField(Grupos, backref='id_grupo')
    class Meta:
        database=db
        db_table = 'calificaciones'

class CalificacionesEstudiantes(peewee.Model):
    ID_CalificaionEstudiante = peewee.IntegerField(primary_key =True)
    Valor = peewee.FloatField()
    ID_Estudiante = peewee.ForeignKeyField(Estudiantes,backref='id_estudiante')
    ID_Calificaion = peewee.ForeignKeyField(Calificaciones,backref='id_calificacion')
    class Meta:
        database=db
        db_table = 'calificaciones_estudiantes'


db.create_tables([Usuarios, Estudiantes, Grupos, GrupoEstudiante, Asistencias, Calificaciones, AsistenciasEstudiantes, CalificacionesEstudiantes])

def Registrar(Usuario,Contrasena):
    try:
        Usuarios.create(Cedula_Usuario=Usuario,Contrasena = Contrasena)
        return 1
    except:
        print("An exception occurred")
        return 0

def Ingresar(Usuario, Contrasena):
    return Usuarios.select().where(Usuarios.Cedula_Usuario == Usuario, Usuarios.Contrasena == Contrasena)

#FUNCT 0
def CrearGrupo(Nombre,Materia,Usuario):
    Grupos.create(Nombre = Nombre,Materia = Materia,Cedula_Usuario= Usuario)
#FUNCT 1
def CrearNota(Nombre,Grupo):
    Calificaciones.create(Nombre = Nombre, ID_Grupo = Grupo)
    cali = Calificaciones.select().where(Calificaciones.Nombre == Nombre, Calificaciones.ID_Grupo == Grupo)
    est = Estudiantes.select()
    for e in est:
        for c in cali:
            CalificacionesEstudiantes.create(ID_Estudiante = e.ID_Estudiante,ID_Calificaion = c.ID_Calificaion, Valor= 0.0)
#FUNCT 2
def CrearAsistencia(Dia,Grupo):
    Asistencias.create(Dia = Dia, ID_Grupo = Grupo)
    asis = Asistencias.select().where(Asistencias.Dia == Dia, Asistencias.ID_Grupo == Grupo)
    est = Estudiantes.select()
    for e in est:
        for a in asis:
            AsistenciasEstudiantes.create(ID_Estudiante = e.ID_Estudiante,ID_Asistencia = a.ID_Asistencia)
#FUNCT 3
def AgregarEstudiante(Nombre,ID_Estudiante,ID_Grupo):
    est = Estudiantes.select().where(Estudiantes.ID_Estudiante == ID_Estudiante)
    cal = Calificaciones.select()
    asis = Asistencias.select()
    if not est:
        Estudiantes.create(ID_Estudiante = ID_Estudiante, Nombre = Nombre)
        for i in cal:
            CalificacionesEstudiantes.create(ID_Estudiante = ID_Estudiante,ID_Calificaion = i.ID_Calificaion, Valor= 0.0)
        for i in asis:
            AsistenciasEstudiantes.create(ID_Estudiante = ID_Estudiante,ID_Asistencia = i.ID_Asistencia)
    GrupoEstudiante.create(ID_Estudiante = ID_Estudiante, ID_Grupo = ID_Grupo)
    

#FUNCT 4
def ListarGrupos(Usuario):
    grupos = Grupos.select().where(Grupos.Cedula_Usuario == Usuario)
    gruposre =[]
    for i in grupos:
        gruposre.append(str(i.ID_Grupo)+" "+i.Nombre+" : "+i.Materia)
    return gruposre

#FUNCT 5
def ListarEstudiantes(Grupo):
    ests = GrupoEstudiante.select().join(Estudiantes).where(GrupoEstudiante.ID_Grupo == Grupo).order_by(Estudiantes.Nombre)
    nombreestudiantes =[]
    for i in ests:
        nombreestudiantes.append(str(i.ID_Estudiante)+" "+i.ID_Estudiante.Nombre)
    return nombreestudiantes

#FUNCT 6
def ListarCalificaciones(ID_Grupo,ID_Estudiante):
    cal = CalificacionesEstudiantes.select().join(Calificaciones).where(Calificaciones.ID_Calificaion == CalificacionesEstudiantes.ID_Calificaion,
                CalificacionesEstudiantes.ID_Estudiante == ID_Estudiante,Calificaciones.ID_Grupo == ID_Grupo)
    calre =[]
    for i in cal:
       calre.append(i.ID_Calificaion.Nombre + ": "+str(i.Valor))
    return calre

#FUNCT 7
def ListarAsistencias(ID_Grupo,ID_Estudiante):
    asis = AsistenciasEstudiantes.select().join(Asistencias).where(Asistencias.ID_Asistencia == AsistenciasEstudiantes.ID_Asistencia,
                AsistenciasEstudiantes.ID_Estudiante == ID_Estudiante,Asistencias.ID_Grupo == ID_Grupo)
    asisre =[]
    for i in asis:
       asisre.append("Clase: "+str(i.ID_Asistencia.Dia)+ ": "+str(i.Valor))
    return asisre

listfunct =[["VI","CN","CM",3],["VI","TABLA","CN",3],[50],["VI","CN","CID",3]]

def DoQuery(select, params,Usuario):
    if select == 0:
        CrearGrupo(params["CN"],params["CM"],Usuario)
        playsound("bienvenida.mp3")
    elif select == 1:
        pass

if __name__=="__main__":
    #usuario1 = Usuarios.create(Cedula_Usuario=1234567890,Contrasena = 'qwerty')
    #Saulo.save()
    #Angel = Usuarios.create(124,123)

    '''
    query = Usuarios.select()
    for i in query:
        print(i)
    print("Finalizo")
    '''
    #CrearGrupo("Grupo 2","Inteligencia Artificial",147852369)
    print(ListarCalificaciones(1,111))