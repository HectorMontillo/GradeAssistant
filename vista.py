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
                print(str(us.Cedula_Usuario)+" "+str(us.Contrasena))
                usu = us

            if not inicio:
                m.text_to_speech(Error[0],'es')
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()
                
            else:
                m.text_to_speech("Bienvenido a GradeAssistant",'es')
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
                '''
                self.Show(False)
                self.IndexFrame.Show()
                '''
            else:
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()

class Index(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_I, size=c.SIZE_I,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.Bind(wx.EVT_CLOSE,self.Close)
        self.Usuario = None
        self.Grupos = ["" for i in range(100)]
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
        self.LBListaGrupos = wx.ListBox(panel, pos = (32,88),choices=self.Grupos,size = (c.ANCHO_I-96,340), style = wx.LB_SINGLE)
        #Botones----------------------------------------
        self.BtnCrearGrupo = wx.Button(panel, label="CrearGrupo", pos=(c.ANCHO_I-160,c.ALTO_I-128), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.CrearGrupo, self.BtnCrearGrupo)
        '''
        self.BtnRegistrar = wx.Button(panel, label="Registrarse", pos=(c.ANCHO-272, 168), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.Registrar, self.BtnRegistrar)
        '''
        #Frames--------------------------------------------
        self.CrearGrupoFrame = CrearGrupo(self,-1)

    def Close(self,event):
        self.Show(False)
        MainFrame.Show()
    
    def CrearGrupo(self,event):
        self.CrearGrupoFrame.Show()

    def ActulizarListaGrupos(self,Usuario):
        Grupos = bd.ListarGrupos(Usuario)
        i = 0
        n = self.LBListaGrupos.GetCount()
        while(i<n or i<len(Grupos)):
            if len(Grupos)>i:
                self.LBListaGrupos.SetString(i,Grupos[i])
            else:
                self.LBListaGrupos.SetString(i,"")
            i+=1

        

    
class CrearGrupo(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_CG, size=c.SIZE_CG,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_CLOSE,self.Close)
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        print("Creando Grupo")
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
    app = wx.App()
    MainFrame = Login(None, -1)
    MainFrame.Show()

    app.MainLoop()
