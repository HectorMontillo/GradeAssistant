import wx

class Index(wx.Frame):
    def __init__(self, parent, id, ancho, alto):
        wx.Frame.__init__(self, parent, id, title='SETEN Beta 0.1', size=(ancho, alto), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.IniciarInterfaz(ancho,alto)

    def IniciarInterfaz(self, ancho, alto):
        print("Interfaz Inicializada")

        self.resultado = -1
        #Barra de Menues------------------------
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
        #FIN Barra de menues--------------------

        #Barra de estados-----------------------
        #statusbar = wx.StatusBar()
        #self.SetStatusBar(statusbar)
        #FIN Barra de estados-------------------

        #PANEL----------------------------------
        panel = wx.Panel(self)

        #Fuentes--------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(10)
        font2 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font2.SetPointSize(8)
        #titulo---------15------------------------
        titulo = wx.StaticText(panel, -1, label="SETEN : Diagnóstico", pos=(32,32))
        titulo.SetFont(font)
        separator = wx.StaticLine(panel, -1, pos=(32, 56),size=(ancho-64,-1), style=wx.LI_HORIZONTAL)
        ayuda = wx.StaticText(panel, -1, label="Llene todos los campos",
                              pos=(32,72))
        separator2 = wx.StaticLine(panel, -1, pos=(480, 104), size=(-1,alto-168), style=wx.LI_VERTICAL)
        bitLogo = wx.Bitmap('icon.png',wx.BITMAP_TYPE_PNG)
        stcBitLogo = wx.StaticBitmap(panel,-1,bitLogo,(ancho-128,60))

        bitIcon = wx.Bitmap('IconFrame2.png', wx.BITMAP_TYPE_PNG)
        icono = wx.EmptyIcon()
        icono.CopyFromBitmap(bitIcon)
        self.SetIcon(icono)
        #Inputs---------------------------------
        LNombre = wx.StaticText(panel, -1, label="Nombre    :", pos=(32, 104))
        LNombre.SetFont(font2)
        self.TFNombre = wx.TextCtrl(panel, id=wx.ID_ANY, value="Default", pos=(112, 104), size=(352, -1))

        LAltura = wx.StaticText(panel, -1, label="Altura(m) :", pos=(32, 136))
        LAltura.SetFont(font2)
        self.TFAltura = wx.TextCtrl(panel, id=wx.ID_ANY, value="25.0", pos=(112, 136), size=(128, -1))

        LPeso = wx.StaticText(panel, -1, label="Peso(kg) :", pos=(264, 136))
        LPeso.SetFont(font2)
        self.TFPeso = wx.TextCtrl(panel, id=wx.ID_ANY, value="25.0", pos=(336, 136), size=(128, -1))

        LSexo = wx.StaticText(panel, -1, label="Sexo         :", pos=(32, 168))
        LSexo.SetFont(font2)
        self.CBMasculino = wx.CheckBox(panel, -1, label="Hombre", pos=(112, 168))
        self.CBFemenino = wx.CheckBox(panel, -1, label="Mujer", pos=(112, 184))
        self.Bind(wx.EVT_CHECKBOX, self.CBM, self.CBMasculino)
        self.Bind(wx.EVT_CHECKBOX, self.CBF, self.CBFemenino)

        LEdad = wx.StaticText(panel, -1, label="Edad       :", pos=(264, 168))
        LEdad.SetFont(font2)
        self.TFEdad = wx.TextCtrl(panel, id=wx.ID_ANY, value="25", pos=(336, 168), size=(128, -1))

        separator3 = wx.StaticLine(panel, -1, pos=(32, 216), size=(432, -1), style=wx.LI_HORIZONTAL)

        LConsola = wx.StaticText(panel, -1, label="Consola", pos=(32, 232))
        LConsola.SetFont(font2)
        self.TAConsola = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(32, 264), size=(432, 128), style=wx.TE_MULTILINE | wx.TE_RICH)

        BtnDiagnosticar = wx.Button(panel,label="Diagnosticar",pos=(368,408),size=(96,32))
        self.Bind(wx.EVT_BUTTON, self.diagnosticar, BtnDiagnosticar)

        LResumen = wx.StaticText(panel, -1, label="Resumen", pos=(512, 104))
        LResumen.SetFont(font2)
        self.TAResumen = wx.TextCtrl(panel, id=wx.ID_ANY, value="", pos=(512, 136), size=(416, 256),
                                     style=wx.TE_MULTILINE)

        BtnImprimir = wx.Button(panel, label="Imprimir", pos=(832, 408), size=(96, 32))
        BtnTratamiento = wx.Button(panel, label="Tratamiento", pos=(720, 408), size=(96, 32))
        self.Bind(wx.EVT_BUTTON, self.tratamiento, BtnTratamiento)

        self.MsnSintomas = wx.MessageDialog(None, ' ', 'Pregunta', wx.YES_NO)

        #self.frameTrat = Tratamiento(self, -1, ancho - 128, alto)

    def tratamiento(self,event):
        pass
        '''
        
        if self.resultado != -1:
            self.frameTrat.Show(True)
            control.generarTratamiento(self.resultado,self.frameTrat.TATratamieto)
        else:
            self.TAConsola.SetForegroundColour(wx.RED)
            #self.TAConsola.SetValue("")
            self.TAConsola.WriteText("Debe realizar primero un diagnóstico\n")
        '''
    def diagnosticar(self, event):
        #print("Diagn")
        pass
        '''
        try:
            nombre = self.TFNombre.GetValue()
            altura = float(self.TFAltura.GetValue())
            peso = float(self.TFPeso.GetValue())
            edad = int(self.TFEdad.GetValue())
            if (self.CBMasculino.GetValue() == False) and (self.CBFemenino.GetValue() == False):
                self.TAConsola.SetForegroundColour(wx.RED)
                self.TAConsola.WriteText("Debe llenar todos los campos!!\n")
            else:
                self.TAConsola.SetForegroundColour(wx.GREEN)
                self.TAConsola.SetValue("")
                self.TAConsola.WriteText("Realizando diagnóstico!!\n")
                if self.CBFemenino.GetValue() == True:
                    sexo = "Femenino"
                else:
                    sexo = "Masculino"
                self.resultado = control.generarDiagnostico(nombre,altura,peso,edad,sexo,self.TAResumen,self.MsnSintomas)
        except:
            self.TAConsola.SetForegroundColour(wx.RED)
            self.TAConsola.WriteText("Ha ingreado valores invalidos!!\n")
            self.resultado = -1
        '''
    def CBM(self, event):
        pass
        '''
        self.CBFemenino.SetValue(False)
        '''

    def CBF(self, event):
        pass
        '''
        self.CBMasculino.SetValue(False)
        '''
if __name__=="__main__":
    app = wx.App()
    frame = Index(None, -1, 960, 512)
    frame.Show()

    app.MainLoop()
