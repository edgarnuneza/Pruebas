import cv2 as cv
from objeto import Objeto

class Clasificador:

    def __init__(self):
        self.listaObjetosDefinidos = list()
        self.listaObjetosDefinidos.append(Objeto("Conector", (1600, 200), (170, 15), (44, 5), (0.65, 0.2)))
        self.listaObjetosDefinidos.append(Objeto("Bateria", (2800, 500), (375, 125), (60, 5), (0.53, 0.3)))
        self.listaObjetosDefinidos.append(Objeto("Vasito", (14500, 1500), (570, 80), (130, 10), (0.64, 0.4)))
        self.listaObjetosDefinidos.append(Objeto("Lata", (4100, 1600), (750, 230), (65, 25), (0.6, 0.2)))

    def colocarEtiqueta(self, imagen, area, perimetro, diametroEquivalente, extent, puntoCentral):
        for objeto in self.listaObjetosDefinidos:
            objeto.calcularUmbral(area, perimetro, diametroEquivalente, extent)
            if objeto.isObjeto():
                cv.putText(imagen, objeto.nombre, puntoCentral, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 180), 1)

        return imagen