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
                text = text.replace(t,"#none")
        return text
    
    def Parser(self,fixtext):
        sentence = fixtext.split()
        for t in self.rd.parse(sentence):
            return t.productions()[0].rhs()
                
        
    def Text_To_Peewee(self,text,Usuario):
        parse = self.Parser(self.Fixer(text))
        count = 0
        select = None
        textlist = text.split()
        params = dict()
        for i in bd.listfunct:
            #print(i)
            for tag in parse:
                tagstr = str(tag)
                if tagstr in i:
                    params[tagstr] = textlist[parse.index(tag)+1]
                    count+=1
            if count == i[-1]:
                select = bd.listfunct.index(i)
                break
            count=0
        bd.DoQuery(select,params,Usuario)
                
    

    def Peewee_To_Text(self):
        pass

class Text_To_Speech():
    def __init__(self):
        pass
    def Play(self,file):
        playsound(file)
    
    def Saludo(self):
        playsound('bienvenida.mp3')


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
    obj =NLP()
    obj.Text_To_Peewee('crear un grupo llamado matemáticas para la materia matemáticas')