import speech_recognition as sr

from datetime import date

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe la voz tomada desde el microfono.

    Retorna un diccionario con las siguientes tres claves:

    "success":          Un Booleano que indica si la respuesta de la API fue satisfactoria.
    "error":            Contiene el mesaje de error, este es None si no ocurrió ningun error.
    "transcription":    Contiene el texto transcrito, este es None si no pudo ser transcrito.
    """

    # Toma el audio desde el microfono en un intervalo de 5 segundos, teniendo en cuenta el ruido de ambiente
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,phrase_time_limit=5)
        print("Reconociendo")

    # Diccionario que es retornado como respuesta
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    #Se utiliza la API de google para pasar de la voz tomada desde el microfono a texto
    print("Reconociendo")
    try:
        response["transcription"] = recognizer.recognize_google(audio, language='es-CO')
    except sr.RequestError:
        # La API no responde
        response["success"] = False
        response["error"] = "API no disponible"
    except sr.UnknownValueError:
        # No se logro reconocer la que se dijo
        response["error"] = "Imposible reconocer lo que quiere decir"

    return response



if __name__=="__main__":
    
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
