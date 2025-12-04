# Preguntas de Repaso

## 1 ¿Qué librerías se usaron en el laboratorio para grabar y reconocer voz?

**R//** Se usaron principalmente:

* **Sounddevice:** Para grabar el audio desde el micrófono.
* **Scipy.io.wavfil.write:** Para guardar el audio en formato **WAV**.
* **Speech_recognition:** Para convertir el audio a texto usando un servicio de reconocimiento de voz (Google Speech Recognition en este caso).

## 2. ¿Por qué decidimos no usar PyAudio en esta práctica?

**R//** **PyAudio** es otra librería popular para captura de audio, pero:

* Puede presentar problemas de instalación en algunos sistemas (especialmente Windows).
* Requiere dependencias nativas y compilación adicional.
* `sounddevice` es más ligero, fácil de instalar y suficiente para grabaciones simples.

## 3. ¿Qué rol cumple la función `recognize_google` en el código?

**R//** Es el método de **`SpeechRecognition`** que envía el audio a los servidores de Google para su procesamiento.

* Convierte la onda sonora en **texto** usando el modelo de reconocimiento de voz de Google.
* Recibe comor argumento el audio capturado (**`data`**) y el idioma (**`es-ES`** para español de España).

## 4. ¿Qué ocurre si `SpeechRecognition` no entiende lo que dijiste?

**R//** Si no puede reconocer palabras claras, lanza la excepción:

* **`sr.UnknownValueError`**, que manejamos con un mensaje: **`No se entendió el audio.`**

* En este caso, el sistema no procesa ningún comando.

## 5. ¿Cómo se guardó temporalmente el archivo `WAV` en el código?

**R//** Se utilizó **`tempfile.mktemp(suffix="-wav")`** para generar una ruta de archivo temporal.

* Luego se guardó el audio usando **`write(tmp_wav, SRATE, audio)`**.
* Finalmente, se eliminó con **`os.remove(tmp_wav)`** para no dejar archivos residuales.

## 6. ¿Qué diferencia hay entre `voz_archivo.py` y `voz_comandos.py`?

**R//** **`voz_archivo.py:`** Se encarga de **grabar la voz y convertirla en texto** (captura + reconocimiento).

* **`voz_comandos.py:`** Se encarga de **interpretar el texto** y ejecutar las acciones correspondientes (abrir páginas, contar chistes, mostrar hora, etc.).

## 7. Menciona un comando que implementaste y explica cómo funciona

**R//** Uno de los comandos que implementamos fue el de abrir **`Youtube`** en una canción especifica.

* Lo que hiciemos fue que la entrada fuese el nombre de la canción en este caso **`pide lo que quiera mami`** y utilizando la libreria `import webbroser` usamos **`webbrowser.open`** para colocar la url de la canción en youtube y de esta manera se abra esta en el navegador.

## 8. ¿Qué posibles aplicaciones reales tiene un sistema de voz como este?

**R//** **Asistentes virtuales** (como Alexa, Google Assistant).

* Sistemas de **domótica** (controlar luces, música, etc. con la voz).
* **Lectura y dictado** de mensajes o documentos.
* **Comandos rápidos** en aplicaciones sin necesidad de teclado.
* Herramientas de **accesibilidad** para personas con discapacidad.

## 9. ¿Cómo manejarías el error de conexión con el servicio de reconocimiento?

**R//** Capturando la excepción **`sr.RequestError`**, que ya tenemos en el código.

* Mostrar un mensaje claro: **`"No se pudo conectar al servicio de reconocimiento."`**
* Implementar **reintentos automáticos** o usar un sistema de reconocimiento **offline (como Vosk)** si no hay conexión.

## 10. ¿Qué mejoras propondrías para la próxima versión de este asistente de voz?

**R//** **Soporte offline** para reconocimiento sin internet (Vosk, Whisper).

* **Respuesta hablada (text-to-speech)** para que lea las respuestas.
* **Comandos dinámicos y configurables** por el usuario.
* **Integración con APIs externas** (clima real, noticias, agenda personal).
* **Mejor manejo de errores y feedback en tiempo real**.
* **Posibilidad de ejecutarse continuamente en segundo plano** escuchando palabras clave ("Hey asistente").

## Imagenes de la ejecucion del programa

![Ejecucion del programa](/codelab1/ReconocimientoDeVoz/imgs/ReconocimientoVoz.png)

![Ejecucion del programa](/codelab1/ReconocimientoDeVoz/imgs/ReconocimientoVoz1.png)
