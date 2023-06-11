import Rectangulo
import Instruccion


class Calculadora:
    def __init__(self):
        self.instruccion = Instruccion.Instruccion()
        self.integral = Rectangulo.Rectangulo()
        self.condicional = True
        self.opc = ""

    def mostrar_instruccion(self):
        self.instruccion.mostrar_instruccio()

    def saludar(self):
        self.instruccion.saludar()

    def pedir_valor(self):
        self.integral.set_valores()
        self.integral.calcular_h()
        self.integral.interpretar_funcion()
        self.integral.calcular_integral()
        self.integral.get_integral()

    def menu(self):
        while self.condicional:
            self.opc = int(
                input("\nPor favor seleccione una opcion: \n1)Ver instrucciones \n2)Calcular integral \n3)Salir\n"))
            if self.opc == 1:
                self.mostrar_instruccion()

            elif self.opc == 2:
                self.pedir_valor()

            elif self.opc == 3:
                self.condicional = False

            else:
                print("Favor de selecionar una opción válida!")

    def tabular(self):
        pass
