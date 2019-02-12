# -*- coding: utf-8 -*-
import wx
import constantes as c
import modelo as m

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
        self.BtnRegistrar = wx.Button(panel, label="Registrarse", pos=(c.ANCHO-272, 168), size=(96, 32))

        #self.BtnPrueba = wx.Button(self.Panel, label="Prueba", pos=(32, 32), size=(96, 32))
        #self.Bind(wx.EVT_BUTTON, self.tratamiento, self.BtnPrueba)

  




if __name__=="__main__":
    app = wx.App()
    frame = Login(None, -1)
    frame.Show()

    app.MainLoop()
