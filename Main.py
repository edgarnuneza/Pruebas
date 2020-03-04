import cv2 as cv
from camara import Camara
from extractorCaracteristicas import ExtractorCaracteristicas
from clasificador import Clasificador

camara = Camara(0)

imagenOriginal, imagenCorregida, imagenEscalaGrises = camara.getImagenes()

cv.imshow('Imagen', imagenOriginal)

caracteristicas = ExtractorCaracteristicas(imagenEscalaGrises)
caracteristicasObjetos = caracteristicas.extraerCaracteristicas()

clasificador = Clasificador()
imagenConObjetosClasficados = clasificador.colocarEtiqueta(imagenCorregida, caracteristicasObjetos)

cv.imshow('Imagen', imagenConObjetosClasficados)

cv.waitKey(0)