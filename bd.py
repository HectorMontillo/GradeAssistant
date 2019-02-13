import peewee

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
    Valor = peewee.BooleanField()
    ID_Estudiante = peewee.ForeignKeyField(Estudiantes, backref='id_estudiante')
    class Meta:
        database=db
        db_table = 'asistencias'

class Calificaciones(peewee.Model):
    ID_Calificaion = peewee.IntegerField(primary_key =True)
    Nombre = peewee.CharField()
    Valor = peewee.FloatField()
    ID_Estudiante = peewee.ForeignKeyField(Estudiantes,backref='id_estudiante')
    class Meta:
        database=db
        db_table = 'calificaciones'


db.create_tables([Usuarios, Estudiantes, Grupos, GrupoEstudiante, Asistencias, Calificaciones])

def Registrar(Usuario,Contrasena):
    try:
        Usuarios.create(Cedula_Usuario=Usuario,Contrasena = Contrasena)
        return 1
    except:
        print("An exception occurred")
        return 0

def Ingresar(Usuario, Contrasena):
    return Usuarios.select().where(Usuarios.Cedula_Usuario == Usuario, Usuarios.Contrasena == Contrasena)

def CrearGrupo(Nombre,Materia,Usuario):
    Grupos.create(Nombre = Nombre,Materia = Materia,Cedula_Usuario= Usuario)

def ListarGrupos(Usuario):
    grupos = Grupos.select().where(Grupos.Cedula_Usuario == Usuario)
    gruposre =[]
    for i in grupos:
        gruposre.append(i.Nombre+" : "+i.Materia)
    return gruposre

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
