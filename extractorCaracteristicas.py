import cv2 as cv
import numpy as np
from math import sqrt, atan2, sin, cos, pi

class ExtractorCaracteristicas:

    def __init__(self, imagen):
        self.__imagen = imagen

    def extraerCaracteristicas(self):
        self.__binarizar()
        self.__listaCaracteristicasObjetos = list()

        self.contornos, hierarchy = cv.findContours(self.__imagenBinarizada, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        print(len(self.contornos))
        for contorno in self.contornos:
            perimetro = cv.arcLength(contorno, True)
            area = cv.contourArea(contorno)

            if area > 200:
                boundingRect = cv.boundingRect(contorno)
                diametroExterno = sqrt(4 * area / 3.1416)
                rect_area = boundingRect[2] * boundingRect[3]
                extent = area / rect_area

                if len(contorno) > 5:
                    minEllipse = cv.fitEllipse(contorno)
                #minEllipse = cv.fitEllipse(contorno)

                angulo, centro = self.__getOrientation(contorno)
                self.__listaCaracteristicasObjetos.append((centro, area, perimetro, diametroExterno, extent))

        return self.__listaCaracteristicasObjetos

    def __binarizar(self):
        umbral, self.__imagenBinarizada = cv.threshold(self.__imagen, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY_INV)
        cv.imshow("imagenB", self.__imagenBinarizada)

    def __getOrientation(self, puntos):
        sz = len(puntos)
        data_pts = np.empty((sz, 2), dtype=np.float64)

        for i in range(data_pts.shape[0]):
            data_pts[i, 0] = puntos[i, 0, 0]
            data_pts[i, 1] = puntos[i, 0, 1]

        # Perform PCA analysis
        mean = np.empty((0))
        mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
        # Store the center of the object
        cntr = (int(mean[0, 0]), int(mean[0, 1]))

        cv.circle(self.__imagen, cntr, 3, (255, 0, 255), 2)
        p1 = (cntr[0] + 0.02 * eigenvectors[0, 0] * eigenvalues[0, 0],
              cntr[1] + 0.02 * eigenvectors[0, 1] * eigenvalues[0, 0])
        p2 = (cntr[0] - 0.02 * eigenvectors[1, 0] * eigenvalues[1, 0],
              cntr[1] - 0.02 * eigenvectors[1, 1] * eigenvalues[1, 0])
        #self.drawAxis(self.__imagen, cntr, p1, (0, 255, 0), 1)
        #self.drawAxis(self.__imagen, cntr, p2, (255, 255, 0), 5)
        angle = atan2(eigenvectors[0, 1], eigenvectors[0, 0])  # orientation in radians

        return angle, cntr

    def drawAxis(self, imagen, p_, q_, colour, scale):
        p = list(p_)
        q = list(q_)

        angle = atan2(p[1] - q[1], p[0] - q[0])
        hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))

        q[0] = p[0] - scale * hypotenuse * cos(angle)
        q[1] = p[1] - scale * hypotenuse * sin(angle)
        cv.line(imagen, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)

        p[0] = q[0] + 9 * cos(angle + pi / 4)
        p[1] = q[1] + 9 * sin(angle + pi / 4)
        cv.line(imagen, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)

        p[0] = q[0] + 9 * cos(angle - pi / 4)
        p[1] = q[1] + 9 * sin(angle - pi / 4)
        cv.line(imagen, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv.LINE_AA)