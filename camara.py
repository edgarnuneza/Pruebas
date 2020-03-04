import cv2 as cv

class Camara:

    def __init__(self, numeroCamara):
        self.__captura = cv.VideoCapture(numeroCamara)

    def __tomarImagen(self):
        if self.__captura.isOpened():
            isImageCapture, self.__imagenOriginal = self.__captura.read()
        else:
            print("No se puede abrir la camara")

    def tomarImagenCorregida(self):
        self.__tomarImagen()
        self.__imagenCorregida = self.__imagenOriginal.copy()
        self.ajustarBrillo()
        self.ajustarConstraste()

        return self.__imagenCorregida

    def getImagenCorregidaEscalaGrises(self):
        return cv.cvtColor(self.__imagenCorregida, cv.COLOR_BGR2GRAY)

    def getImagenes(self):
        self.tomarImagenCorregida()
        return self.__imagenOriginal, self.__imagenCorregida, self.getImagenCorregidaEscalaGrises()

    def ajustarBrillo(self):
        self.__imagenCorregida[:, :, 0] = cv.add(self.__imagenOriginal[:, :, 0], -175)  # Canal azul
        self.__imagenCorregida[:, :, 1] = cv.add(self.__imagenOriginal[:, :, 1], -180)  # Canal  verde
        self.__imagenCorregida[:, :, 2] = cv.add(self.__imagenOriginal[:, :, 2], -150)  # Canal rojo

    def ajustarConstraste(self):
        self.__imagenCorregida = cv.convertScaleAbs(self.__imagenOriginal, self.__imagenCorregida, 4, 0)