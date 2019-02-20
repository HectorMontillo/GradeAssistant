# -*- coding: utf-8 -*-
import wx
import constantes as c
import modelo as m
import bd

class Login(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION, size=c.SIZE,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.IniciarInterfaz()
    
    def IniciarInterfaz(self):
        print("Interfaz inicializada")
        #Panel Principal---------------------------
        panel = wx.Panel(self)

        #Fuentes-------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)

        #Titulo--------------------------------------
        titulo = wx.StaticText(panel, -1, label="Bienvenido a GradeAssistant", pos=(32,32))
        titulo.SetFont(font)
        wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO-96,-1), style=wx.LI_HORIZONTAL)

        #Ingreso de datos---------------------------
        wx.StaticText(panel, -1, label="Usuario", pos=(32, 104))
        self.TFUsuario = wx.TextCtrl(panel, id=wx.ID_ANY, value="cedula", pos=(112, 104), size=(c.ANCHO-176, -1))

        wx.StaticText(panel, -1, label="Contraseña", pos=(32, 136))
        self.TFContrasena = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(112, 136), size=(c.ANCHO-176, -1), style=wx.TE_PASSWORD)

        self.BtnIngresar = wx.Button(panel, label="Ingresar", pos=(c.ANCHO-160, 168), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Ingresar, self.BtnIngresar)
        self.BtnRegistrar = wx.Button(panel, label="Registrarse", pos=(c.ANCHO-272, 168), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Registrar, self.BtnRegistrar)

        #Alertas-------------------------------
        self.MDError = wx.MessageDialog(self,"Default")

        #Frames---------------------------------
        self.IndexFrame = Index(self, -1)




    def Ingresar(self,event):
        Error = ["Usuario o contrasena incorrecta","Debe llenar ambos campos"]
        Usuario = self.TFUsuario.GetValue()
        Contrasena = self.TFContrasena.GetValue()

        if Usuario == "" or Contrasena == "":
            self.MDError.SetMessage(Error[1])
            self.MDError.ShowModal()
        else:
            inicio = bd.Ingresar(Usuario,Contrasena)
            usu = None
            for us in inicio:
                usu = us

            if not inicio:
                #m.text_to_speech(Error[0],'es')
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()
                
            else:
                #m.text_to_speech("Bienvenido a GradeAssistant",'es')
                self.Show(False)
                self.IndexFrame.Show()
                self.IndexFrame.Usuario = usu.Cedula_Usuario
                #print(usu.Cedula_Usuario)
                self.IndexFrame.ActulizarListaGrupos(usu.Cedula_Usuario)


    def Registrar(self,event):
        Error = ["No pudo ser registrado, Este usuario ya existe","Debe llenar ambos campos"]
        Usuario = self.TFUsuario.GetValue()
        Contrasena = self.TFContrasena.GetValue()
        

        if Usuario == "" or Contrasena == "":
            self.MDError.SetMessage(Error[1])
            self.MDError.ShowModal()
        else:
            registro = bd.Registrar(Usuario,Contrasena)
            if registro:
                self.Ingresar(event)
            else:
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()

class Index(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_I, size=c.SIZE_I,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Usuario = None
        self.Estudiantes = None
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        print("Index")
        #Menu Bar---------------------------------
        menubar = wx.MenuBar()
        file = wx.Menu()
        view = wx.Menu()
        help = wx.Menu()
        about = wx.Menu()

        file.Append(-1,"&Salir\tCTRL+Q","Salir de la Aplicacion")
        view.Append(-1,"&Mostrar barra de estados\tCTRL+M", "Ocualtar Barra de estados")
        help.Append(-1,"&Sitio Web\tCTRL+H", "Ir a sitio web")
        about.Append(-1, "&Informacion del Producto\tCTRL+I")

        menubar.Append(file,"Archivos")
        menubar.Append(view, "Ver")
        menubar.Append(help, "Ayuda")
        menubar.Append(about, "Acerca de")

        self.SetMenuBar(menubar)
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        titulo = wx.StaticText(panel, -1, label="GradeAssistant", pos=(32,32))
        titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_I-96,-1), style=wx.LI_HORIZONTAL)
        #Listado de Grupos-------------------------------
        self.LBListaGrupos = wx.ListBox(panel, pos = (32,88),size = (c.ANCHO_I-96,340), style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.AbrirGrupo, self.LBListaGrupos)
        #Botones----------------------------------------
        self.BtnCrearGrupo = wx.Button(panel, label="CrearGrupo", pos=(c.ANCHO_I-160,c.ALTO_I-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.CrearGrupo, self.BtnCrearGrupo)

        self.BtnVoz = wx.Button(panel, label="Comando voz", pos=(c.ANCHO_I-160,16), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Voz, self.BtnVoz)
        '''
        self.BtnRegistrar = wx.Button(panel, label="Registrarse", pos=(c.ANCHO-272, 168), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Registrar, self.BtnRegistrar)
        '''
        #Frames--------------------------------------------
        self.CrearGrupoFrame = CrearGrupo(self,-1)
        self.VistaGrupo = VistaGrupo(self,-1)

    def Voz(self,event):
        tspeech.recognize(7)
        
    def Close(self,event):
        self.Show(False)
        MainFrame.Show()
    
    def CrearGrupo(self,event):
        self.CrearGrupoFrame.Show()

    def ActulizarListaGrupos(self,Usuario):
        '''
        Grupos = bd.ListarGrupos(Usuario)
        i = 0
        n = self.LBListaGrupos.GetCount()
        while(i<n or i<len(Grupos)):
            if len(Grupos)>i:
                self.LBListaGrupos.SetString(i,Grupos[i])
            else:
                self.LBListaGrupos.SetString(i,"")
            i+=1
        '''
        Grupos = bd.ListarGrupos(Usuario)
        self.LBListaGrupos.Clear()
        self.LBListaGrupos.AppendItems(Grupos)

    def AbrirGrupo(self, event):
        label = self.LBListaGrupos.GetStringSelection()
        self.VistaGrupo.titulo.SetLabel(label)
        self.VistaGrupo.LabelGrupo = label
        self.VistaGrupo.Grupo = int(label.split()[0])
        self.VistaGrupo.ActulizarListaEstudiantes()
        self.VistaGrupo.Show()

class VistaGrupo(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_VG, size=c.SIZE_VG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.LabelGrupo = ""
        self.Grupo = 0
        self.IniciarInterfaz()  

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        self.titulo = wx.StaticText(panel, -1, label="", pos=(32,32))
        self.titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_VG-96,-1), style=wx.LI_HORIZONTAL)
        #Lista estudiantes------------------------------
        self.LBListaEstdiantes = wx.ListBox(panel, pos = (32,88),size = (c.ANCHO_VG-96,340), style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.AbrirEstdiante, self.LBListaEstdiantes)
        #Botones----------------------------------------
        self.BtnAgregarEstudiante = wx.Button(panel, label="Agregar Estudiante", pos=(c.ANCHO_VG-192,c.ALTO_VG-128), size=(128, 32))
        self.Bind(wx.EVT_BUTTON, self.AgregarEstudiante, self.BtnAgregarEstudiante)

        self.BtnAgregarNota= wx.Button(panel, label="Agregar Nota", pos=(32,c.ALTO_VG-128), size=(128, 32))
        self.Bind(wx.EVT_BUTTON, self.AgregarNota, self.BtnAgregarNota)

        self.BtnAgregarAsistencia= wx.Button(panel, label="Agregar Asistencia", pos=(168,c.ALTO_VG-128), size=(128, 32))
        self.Bind(wx.EVT_BUTTON, self.AgregarAsistencia, self.BtnAgregarAsistencia)
        #Frames---------------------------------
        self.FrameCrearNota = CrearNota(self,-1)
        self.FrameCrearAsistencia = CrearAsistencia(self,-1)
        self.FrameAgregarEstudiante = AgregarEstudiante(self,-1)
        self.FrameVerEstudiante = VerEstudiante(self,-1)


    def Close(self,event):
        self.Show(False)
        MainFrame.IndexFrame.Show()
    
    def AbrirEstdiante(self,event):

        est = self.LBListaEstdiantes.GetStringSelection()
        self.FrameVerEstudiante.titulo.SetLabel(est)
        self.FrameVerEstudiante.Estudiante = int(est.split()[0])
        self.FrameVerEstudiante.Grupo = self.Grupo
        self.FrameVerEstudiante.ActulizarListaCalificaciones()
        self.FrameVerEstudiante.ActulizarListaAsistencias()
        self.FrameVerEstudiante.Show()
        
    
    def AgregarEstudiante(self,event):
        self.FrameAgregarEstudiante.Grupo = self.Grupo
        self.FrameAgregarEstudiante.Show()
    
    def AgregarNota(self,event):
        self.FrameCrearNota.Grupo = self.Grupo
        self.FrameCrearNota.Show()
        
    def AgregarAsistencia(self,event):
        self.FrameCrearAsistencia.Grupo = self.Grupo
        self.FrameCrearAsistencia.Show()
    
    def ActulizarListaEstudiantes(self):
        Estudiantes = bd.ListarEstudiantes(self.Grupo)
        self.LBListaEstdiantes.Clear()
        self.LBListaEstdiantes.AppendItems(Estudiantes)

class VerEstudiante(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_VG, size=c.SIZE_VG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Grupo = 0
        self.Estudiante = 0
        self.IniciarInterfaz()  

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        self.titulo = wx.StaticText(panel, -1, label="", pos=(32,32))
        self.titulo.SetFont(font)
        wx.StaticText(panel, -1, label="Calificaciones", pos=(32,88))
        wx.StaticText(panel, -1, label="Asistencias", pos=(364,88))
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_VG-96,-1), style=wx.LI_HORIZONTAL)
        #Lista estudiantes------------------------------
        self.LBListaCalificaiones = wx.ListBox(panel, pos = (32,120),size = (276,340), style = wx.LB_SINGLE)
        #self.Bind(wx.EVT_LISTBOX_DCLICK, self.AbrirEstdiante, self.LBListaEstdiantes)
        self.LBListaAsistencias = wx.ListBox(panel, pos = (364,120),size = (276,340), style = wx.LB_SINGLE)
        #self.Bind(wx.EVT_LISTBOX_DCLICK, self.AbrirEstdiante, self.LBListaEstdiantes)


    def Close(self,event):
        self.Show(False)   

    def ActulizarListaCalificaciones(self):
        calificaciones = bd.ListarCalificaciones(self.Grupo,self.Estudiante)
        self.LBListaCalificaiones.Clear()
        self.LBListaCalificaiones.AppendItems(calificaciones)  

    def ActulizarListaAsistencias(self):
        asistencias = bd.ListarAsistencias(self.Grupo,self.Estudiante)
        self.LBListaAsistencias.Clear()
        self.LBListaAsistencias.AppendItems(asistencias) 

    

class AgregarEstudiante(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Crear Nota", size=c.SIZE_CG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Grupo = None
        #self.Parent = parent
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        self.titulo = wx.StaticText(panel, -1, label="Agregar un Estudiante", pos=(32,32))
        self.titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_CG-104,-1), style=wx.LI_HORIZONTAL)
        #Campos de Texto---------------------------------
        wx.StaticText(panel, -1, label="Nombre del Estudiante", pos=(32, 88))
        self.TFNombre = wx.TextCtrl(panel, id=wx.ID_ANY, value="default", pos=(182, 88), size=(c.ANCHO_CG-256, -1))
        wx.StaticText(panel, -1, label="Id Estudiante: ", pos=(32, 120))
        self.TFID = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(128, 120), size=(c.ANCHO_CG-256, -1))
        #Botones-----------------------------------------
        self.BtnCrear = wx.Button(panel, label="Agregar Estudiante", pos=(c.ANCHO_CG-160,c.ALTO_CG-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Crear, self.BtnCrear)
        
    def Close(self,event):
        self.Show(False)
    
    def Crear(self,event):
        nombre = self.TFNombre.GetValue()
        id_estudiante = int(self.TFID.GetValue())
        bd.AgregarEstudiante(nombre,id_estudiante,self.Grupo)
        self.Parent.ActulizarListaEstudiantes()
        self.Show(False)

class CrearNota(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Crear Nota", size=c.SIZE_CG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Grupo = None
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        self.titulo = wx.StaticText(panel, -1, label="Crear una calificación", pos=(32,32))
        self.titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_CG-104,-1), style=wx.LI_HORIZONTAL)
        #Campos de Texto---------------------------------
        wx.StaticText(panel, -1, label="Nombre de la Calificaión", pos=(32, 88))
        self.TFNombre = wx.TextCtrl(panel, id=wx.ID_ANY, value="default", pos=(182, 88), size=(c.ANCHO_CG-256, -1))
        #Botones-----------------------------------------
        self.BtnCrear = wx.Button(panel, label="Crear Nota", pos=(c.ANCHO_CG-160,c.ALTO_CG-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Crear, self.BtnCrear)
        
    def Close(self,event):
        self.Show(False)
    
    def Crear(self,event):
        nombre = self.TFNombre.GetValue()
        bd.CrearNota(nombre,self.Grupo)
        self.Show(False)

class CrearAsistencia(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Crear Asistencia", size=c.SIZE_CG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Grupo = None
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        self.titulo = wx.StaticText(panel, -1, label="Crear una Asistencia", pos=(32,32))
        self.titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_CG-104,-1), style=wx.LI_HORIZONTAL)
        #Campos de Texto---------------------------------
        wx.StaticText(panel, -1, label="Dia de la Asistencia", pos=(32, 88))
        self.TFNombre = wx.TextCtrl(panel, id=wx.ID_ANY, value="default", pos=(182, 88), size=(c.ANCHO_CG-256, -1))
        #Botones-----------------------------------------
        self.BtnCrear = wx.Button(panel, label="Crear Asistencia", pos=(c.ANCHO_CG-160,c.ALTO_CG-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Crear, self.BtnCrear)
        
    def Close(self,event):
        self.Show(False)
    
    def Crear(self,event):
        dia = int(self.TFNombre.GetValue())
        bd.CrearAsistencia(dia,self.Grupo)
        self.Show(False)

class CrearGrupo(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_CG, size=c.SIZE_CG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.IniciarInterfaz()
    

    def IniciarInterfaz(self):
        #Panel------------------------------------------
        panel = wx.Panel(self)
        #Fuentes----------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #Titulo-----------------------------------------
        titulo = wx.StaticText(panel, -1, label="Crear un grupo", pos=(32,32))
        titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(c.ANCHO_CG-96,-1), style=wx.LI_HORIZONTAL)
        #Campos de Texto---------------------------------
        wx.StaticText(panel, -1, label="Nombre Grupo: ", pos=(32, 88))
        self.TFNombreGrupo = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(128, 88), size=(c.ANCHO_CG-192, -1))

        wx.StaticText(panel, -1, label="Materia: ", pos=(32, 120))
        self.TFMateria = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(128, 120), size=(c.ANCHO_CG-192, -1))
        #Botones-----------------------------------------
        self.BtnCrearGrupo = wx.Button(panel, label="CrearGrupo", pos=(c.ANCHO_CG-160,c.ALTO_CG-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.CrearGrupo, self.BtnCrearGrupo)

    def Close(self,event):
        self.Show(False)
        MainFrame.IndexFrame.Show()

    def CrearGrupo(self,event):
        Nombre = self.TFNombreGrupo.GetValue()
        Materia = self.TFMateria.GetValue()
        Usuario = MainFrame.IndexFrame.Usuario
        bd.CrearGrupo(Nombre,Materia,Usuario)
        MainFrame.IndexFrame.ActulizarListaGrupos(Usuario)
        self.Show(False)



  



if __name__=="__main__":
    tspeech = m.Recognizer_From_Mic()
    app = wx.App()
    MainFrame = Login(None, -1)
    MainFrame.Show()

    app.MainLoop()
