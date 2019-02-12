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

            if not inicio:
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()
            else:
                self.Show(False)
                self.IndexFrame.Show()


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
                self.Show(False)
                self.IndexFrame.Show()
                
            else:
                self.MDError.SetMessage(Error[0])
                self.MDError.ShowModal()

class Index(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title=c.CAPTION_I, size=c.SIZE_I,
                style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.Bind(wx.EVT_CLOSE,self.Close)
        self.IniciarInterfaz()

    def IniciarInterfaz(self):
        print("Index")
        
    def Close(self,event):
        self.Show(False)
        MainFrame.Show()
        


  




if __name__=="__main__":
    app = wx.App()
    MainFrame = Login(None, -1)
    MainFrame.Show()

    app.MainLoop()
