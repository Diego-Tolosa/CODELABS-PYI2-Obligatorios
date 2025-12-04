import random

def procesar_comando(texto: str):
    cmd = texto.lower()

    if "hola" in cmd:
        print("¡Hola, bienvenido al curso!")
    elif "abrir google" in cmd:
        import webbrowser
        webbrowser.open("https://www.google.com")
    elif "hora" in cmd:
        from datetime import datetime
        print("Hora actual:", datetime.now().strftime("%H:%M"))
    elif "pide lo que quiera mami" in cmd:
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=G9hcTFynsgQ&ab_channel=COLORS")
    elif "traductor" in cmd:
        import webbrowser
        webbrowser.open("https://translate.google.com/?hl=es")
    elif "clima" in cmd:
        import webbrowser
        webbrowser.open("https://wttr.in/bogota?format=3")
    elif "chiste" in cmd:
        chistes = [
            "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!",
            "¿Cómo organizan una fiesta los gatos? ¡Hacen un miau-sical!",
            "¿Por qué la computadora fue al médico? Porque tenía un virus."
        ]
        print("Aqui va un chiste:", random.choice(chistes))
    else:
        print("Comando no reconocido.")