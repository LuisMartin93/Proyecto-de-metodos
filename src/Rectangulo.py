from sympy import *
from tabulate import tabulate


class Rectangulo:
    def __init__(self):
        self.__n = 0
        self.__fix = 0
        self.__l_superior = 0
        self.__l_inferior = 0
        self.__h = 0
        self.__sumatoria = 0
        self.__x = symbols('x')
        self.__funcion = ""
        self.__f = ""
        self.__area = 0
        self.__lista_principal = []
        self.__lista_reciclada = []

    def set_valores(self):
        self.__n = int(input("Ingrese el valor n para calcular la integral: "))
        self.__fix = int(input("Ingrese el fix que desea: "))
        self.__l_superior = int(input("Ingrese el limite superior de la integral: "))
        self.__l_inferior = int(input("Ingrese el limite inferior de la integral: "))
        self.__funcion = input("Ingrese la función a integrar: ")

    def calcular_h(self):
        self.__h = (self.__l_superior - self.__l_inferior) / self.__n

    def interpretar_funcion(self):
        self.__f = sympify(self.__funcion)

    def calcular_integral(self):
        print("Vamos a calcular la integral de la función '{}' por el metodo de rectangulos".format(self.__f))
        print("\t\t***Tabulación***")
        for i in range(0, self.__n):
            self.__sumatoria = self.__f.subs(self.__x, i * self.__h + self.__l_inferior) + self.__sumatoria
            self.__lista_reciclada.append(i)
            self.__lista_reciclada.append("{:.{}f}".format(i * self.__h + self.__l_inferior, self.__fix))
            self.__lista_reciclada.append(
                "{:.{}f}".format(self.__f.subs(self.__x, i * self.__h + self.__l_inferior), self.__fix))
            self.__lista_principal.append(self.__lista_reciclada.copy())
            self.__lista_reciclada.clear()
        print(tabulate(self.__lista_principal, ["Iteración", "Valor de 'x'", "valor de 'f(x)'"], tablefmt="grid"))
        self.__lista_principal.clear()
        print(
            "Por ultimo vamor a multiplicar la 'h' por el valor total de la sumatoria de las 'f(x)', para calcular la integral")
        print("{} * {} = Integral de la funcion".format(self.__h, self.__sumatoria))
        self.__area = self.__h * self.__sumatoria

    def get_integral(self):
        print("La integral calculada por el metodo es: {:.{}f}".format(self.__area, self.__fix))
        print("La integral analitica para esta funcion es: {}".format(
            integrate(self.__f, (self.__x, self.__l_inferior, self.__l_superior))))
        self.__n = 0
        self.__fix = 0
        self.__l_superior = 0
        self.__l_inferior = 0
        self.__h = 0
        self.__sumatoria = 0
        self.__x = symbols('x')
        self.__funcion = ""
        self.__f = ""
        self.__area = 0
