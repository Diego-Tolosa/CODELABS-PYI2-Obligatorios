# importar voz_archivo y voz_comandos
from voz_archivo import grabar_y_reconocer
from voz_comandos import procesar_comando

if __name__ == "__main__":
    texto = grabar_y_reconocer()
    if texto:
        procesar_comando(texto)