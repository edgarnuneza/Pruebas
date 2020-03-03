import cv2 as cv
from camara import Camara

cam = Camara(1)
imagenOriginal, imagenCorregida, imagenEscalaGrises = cam.getImagenes()
cv.imshow("Imagen", imagenOriginal)
cv.imshow("Imagen Gris", imagenEscalaGrises)
cv.imshow("Imagen corregida", imagenCorregida)

cv.waitKey(0)

