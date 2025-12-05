# import cv2, dlib, time

# detector = dlib.get_frontal_face_detector()
# cap = cv2.VideoCapture('./video/video_rostros.mp4')  # sube tu video corto

# prev = time.time(); frames=0
# while True:
#     ok, frame = cap.read()
#     if not ok: break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     rects = detector(gray, 0)  # 0 = sin upsampling
#     for r in rects:
#         x,y,w,h = r.left(), r.top(), r.width(), r.height()
#         cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
#     frames += 1
#     if frames % 10 == 0:
#         now = time.time(); fps = 10/(now-prev); prev=now
#         cv2.putText(frame, f"FPS: {fps:.1f}", (10,30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
#     # Mostrar frame en notebook (en local usa imshow)
#     _, buf = cv2.imencode('.jpg', frame)
#     # en Colab podrías guardar frames si quieres
# cap.release()


import cv2
import dlib
import time
import numpy as np

# Cargar el detector HOG de dlib
detector = dlib.get_frontal_face_detector()

# Abrir el video
cap = cv2.VideoCapture(r'C:\SemestreActual\ProyectoIntegrador2\CODELABS-PYI2\dlib-HGOenVideo\video\video_rostros.mp4')  # usa ruta absoluta si falla

if not cap.isOpened():
    print("❌ No se pudo abrir el video")
    exit()

prev = time.time()
frames = 0

while True:
    ok, frame = cap.read()
    if not ok or frame is None:
        print("❌ Frame vacío o fin del video")
        break

    # Convertir a RGB (dlib acepta RGB o escala de grises)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = np.ascontiguousarray(rgb, dtype=np.uint8)

    # Detección de rostros
    rects = detector(rgb, 0)

    for r in rects:
        x, y, w, h = r.left(), r.top(), r.width(), r.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # FPS cada 10 frames
    frames += 1
    if frames % 10 == 0:
        now = time.time()
        fps = 10 / (now - prev)
        prev = now
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar frame
    cv2.imshow("Video con Detección - dlib HOG", frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



# Para WebCam (local)
# cap = cv2.VideoCapture(0)
# while True:
#     ok, frame = cap.read()
#     if not ok: break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     rects = detector(gray, 0)
#     for r in rects:
#         x,y,w,h = r.left(), r.top(), r.width(), r.height()
#         cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
#     cv2.imshow("dlib HOG", frame)
#     if cv2.waitKey(1) & 0xFF==27: break
# cap.release(); cv2.destroyAllWindows()