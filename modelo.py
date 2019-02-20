import speech_recognition as sr
import bd 
import constantes as c
from nltk import word_tokenize
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from playsound import playsound


class Recognizer_From_Mic():
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize_speech_from_mic(self, time_limit):
        """Transcribe la voz tomada desde el microfono.

        Retorna un diccionario con las siguientes tres claves:

        "success":          Un Booleano que indica si la respuesta de la API fue satisfactoria.
        "error":            Contiene el mesaje de error, este es None si no ocurrió ningun error.
        "transcription":    Contiene el texto transcrito, este es None si no pudo ser transcrito.
        """

        # Toma el audio desde el microfono en un intervalo de 5 segundos, teniendo en cuenta el ruido de ambiente
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source,phrase_time_limit=time_limit)

        # Diccionario que es retornado como respuesta
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        #Se utiliza la API de google para pasar de la voz tomada desde el microfono a texto
        print("Reconociendo")
        try:
            response["transcription"] = self.r.recognize_google(audio, language='es-CO')
        except sr.RequestError:
            # La API no responde
            response["success"] = False
            response["error"] = "API no disponible"
        except sr.UnknownValueError:
            # No se logro reconocer la que se dijo
            response["error"] = "Imposible reconocer lo que quiere decir"

        return response
    
    def recognize_infinite(self,time_limit):
        while(True):
            print("Say Something!")
            prueba = self.recognize_speech_from_mic(time_limit)
            if prueba["success"]:
                if prueba["error"]:
                    return prueba["error"]
                else:
                    return prueba["transcription"]
            else:
                return "I dont understand" 
    
    def recognize(self,time_limit):
        print("Say Something!")
        prueba = self.recognize_speech_from_mic(time_limit)
        if prueba["success"]:
            if prueba["error"]:
                    return prueba["error"]
            else:
                return prueba["transcription"]
        else:
            return "I dont understand"

class NLP():
    def __init__(self):
        self.Dict = c.tokens
        self.grammar = CFG.fromstring(c.filegrammar.read())
        self.rd = RecursiveDescentParser(self.grammar)


    def Fixer(self,text):
        tokens = word_tokenize(text)
        for t in tokens:
            if t not in c.words:
                text = text.replace(t,"#NONE")
        return text
    
    def Parser(self,fixtext):
        sentence = fixtext.split()
        nonterminals = []
        i=0
        for t in self.rd.parse(sentence):
            while(i < len(t.productions())):
                #print(t.productions())
                nont = str(t.productions()[i].lhs())
                if nont != "TABLA" and nont != "CART":
                    nonterminals.append(str(t.productions()[i].lhs()))
                i+=1
        k=0
        listnone = []
        while(k<len(sentence)):
            if sentence[k]=="#NONE":
                y = k
                while(y < len(sentence) and sentence[y]== "#NONE"):
                    y+=1
                listnone.append(y-k)
                k=y
                
            else:
                k+=1
    

        contador = 0
        x=0
        while(contador<len(listnone) and x < len(nonterminals)):
            if nonterminals[x] == "VALOR":
                for i in range(listnone[contador]):
                    nonterminals.insert(x,"VALOR")
                    x+=1
                contador+=1
            x+=1
        
                 
        return nonterminals
                
        
    def Text_To_Peewee(self,text,Usuario):

        fix = self.Fixer(text)
        parse = self.Parser(fix)
        print(fix)
        print(parse)

        count = 0
        select = None

        textlist = text.split()
        textlistfix = fix.split()
        params = dict()

        print("Obtenida del usuario :"+text)
        print("Obtenida del fixer :"+fix)
        print("Obtenida de la gramatica :"+str(parse))
        if parse:
            for i in bd.listfunct:
                for tag in parse:
                    tagstr = str(tag)
                    #if tagstr == "CART" or tagstr == "TABLA":
                    #    textlistfix.insert(parse.index(tag)-1,"none")
                    if tagstr in i:
                        if tagstr == "CN" or tagstr == "CM":
                            params[tagstr] = ""
                            ind = parse.index(tag)-1
                            print(ind)
                            while(ind < len(textlist) and (textlistfix[ind] == "#NONE" or parse[ind+2] == "GRU" or parse[ind+2] == "ART")):
                                print(str(ind)+ ": "+textlist[ind])
                                params[tagstr]+=(textlist[ind]+" ")
                                ind+=1
                        count+=1
                print("count",count)
                if count == i[-1]:

                    select = bd.listfunct.index(i)
                    break
                count=0
            print(params,select)
            bd.DoQuery(select,params,Usuario)
        else:
            playsound("audios/errorpeticion.mp3")

        
                
    

    def Peewee_To_Text(self):
        pass

class Text_To_Speech():
    def __init__(self):
        pass
    def Play(self,file):
        playsound(file)
    
    def Saludo(self):
        playsound('audios/bienvenida.mp3')

    def GrupoCreado(self):
        playsound('audios/grupocreado.mp3')

    def EstudianteCreado(self):
        playsound('audios/estudiantecreado.mp3')

    def CalificacionCreada(self):
        playsound('audios/calificacioncreado.mp3')

    def AsistenciaCreada(self):
        playsound('audios/asistenciacreado.mp3')


if __name__=="__main__":
    '''
    r = sr.Recognizer()
    mic = sr.Microphone()

    while(True):
        print("Say Something!")
        prueba = recognize_speech_from_mic(r,mic)
        if prueba["success"]:
            if prueba["error"]:
                print(prueba["error"])
            else:
                print("You said: "+prueba["transcription"])
        else:
            print("I dont understand")
    
    obj = Recognizer_From_Mic()
    obj.recognize(7)
    '''
    obj = NLP()
    #parse = obj.Parser(obj.Fixer('quiero crear un grupo llamado grupos 1 para la materia matemáticas 4'))
    #print(parse)
    #parse = obj.Text_To_Peewee('me gustaria crear un grupo llamado  los dioses del olimpo para la materia algebra lineal 5',123)
    parse = obj.Text_To_Peewee('me gustaría crear un grupo llamado grupo uno para la materia matemáticas',123)