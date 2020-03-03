import cv2 as cv

class Camara:

    def __init__(self, numeroCamara):
        self.__captura = cv.VideoCapture(numeroCamara)

    def __tomarImagen(self):
        if self.__captura.isOpened():
            isImageCapture, self.imagenOriginal = self.__captura.read()

        print("No se puede abrir la camara")
        return None

    def tomarImagenCorregida(self):
        self.__tomarImagen()
        self.imagenCorregida = self.imagenOriginal.copy()
        self.ajustarBrillo()
        self.ajustarConstraste()

        return self.imagenCorregida

    def getImagenCorregidaEscalaGrises(self):
        return cv.cvtColor(self.imagenCorregida, cv.COLOR_BGR2GRAY)

    def getImagenes(self):
        self.tomarImagenCorregida()
        return self.imagenOriginal, self.imagenCorregida, self.getImagenCorregidaEscalaGrises()

    def ajustarBrillo(self):
        self.imagenCorregida[:, :, 0] = cv.add(self.imagenOriginal[:, :, 0], -175)  # Canal azul
        self.imagenCorregida[:, :, 1] = cv.add(self.imagenOriginal[:, :, 1], -180)  # Canal  verde
        self.imagenCorregida[:, :, 2] = cv.add(self.imagenOriginal[:, :, 2], -150)  # Canal rojo

    def ajustarConstraste(self):
        self.imagenCorregida = cv.convertScaleAbs(self.imagenOriginal, self.imagenCorregida, 4, 0)