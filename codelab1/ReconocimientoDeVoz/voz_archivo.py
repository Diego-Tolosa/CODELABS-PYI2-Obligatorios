import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile, os

SRATE = 16000 # tasa de muestreo
DUR = 5 # segundos

def grabar_y_reconocer():
    print("Grabando... habla ahora!")
    audio = sd.rec(int(DUR*SRATE), samplerate=SRATE, channels=1, dtype='int16')
    sd.wait() # espera a que termine la grabacion
    print("Listo, procesando...!")

    # Guarda a WAV temporal
    tmp_wav = tempfile.mktemp(suffix=".wav")
    write(tmp_wav, SRATE, audio)

    # Reconoce con SpeechRecognition
    r = sr.Recognizer()
    with sr.AudioFile(tmp_wav) as source:
        data = r.record(source)  # lee el archivo de audio completo
        
    try:
        texto = r.recognize_google(data, language="es-ES")
        print("Dijiste:", texto)
    except sr.UnknownValueError:
        print("No se entendió el audio.")
    except sr.RequestError as e:
        print("Error:", e)
    finally:
        if os.path.exists(tmp_wav):
            os.remove(tmp_wav)
    
    return texto
