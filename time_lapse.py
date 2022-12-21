import os
import time

# Crea un directorio para almacenar las imágenes
if not os.path.exists('imagenes'):
    os.makedirs('imagenes')

i = 0
while True:
    # Toma una fotografía y guarda en el directorio "imagenes" con un nombre enumerado
    os.system('fswebcam -r 1920x1080 --no-banner imagenes/imagen_{}.jpg'.format(i))
    i += 1 # incrementa el contador
    time.sleep(60) # toma una fotografía cada 60 segundos