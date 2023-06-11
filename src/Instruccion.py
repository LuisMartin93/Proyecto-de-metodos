class Instruccion:
    def __init__(self):
        self.saludo = """
        Hola, bienvenido a la calculadora de integrales por medio del método de rectangulos.
        A continuación verá las instrucciones de uso y posteriormente se le solicitaran ciertos datos 
        para calcular su integral.
        Gracias!"""

        self.instruccion = """
        Favor de ingresar numeros enteros en el valor de la 'n', el fix y los limites de la integral; 
        en el caso de los limites, estos pueden ser negativos, pero la 'n' y el fix no.
        A la hora de escribir su funcion, perfectamente puede escribir valores decimales o negativos.
         
                                ***Intrucciones de uso al ingresar la función***
                                
        Para sumar use '+', restar '-', multiplicar '*' y para dividir use '/'
         
        Para calcular el coseno de 'x' escriba:
        cos(x)
         
        Para calcular el seno de 'x' escriba
        sin(x)
         
        Para utilizar 'e' elevado a cualquier potencia, escriba:
        exp(m)
        siendo 'm' cualquier numero al cual desea elevar la base 'e', incluyendo la variable 'x'
        O si lo prefiere, solo escriba 'E' para tenerlo a la exponente 1.
         
        Para utilizar un logaritmo base 'a' de un numero 'b' por favor escriba:
        log(a,b)
        ***Nota: si quiere utilizar el logaritmo natural, favor de poner 'log(exp(1),b)'
         
        Para utilizar raices cuadradas favor de escribir lo siguiente:
        sqrt(m)
        siendo 'm' cualquier numero que desee, incluyendo la variable 'x'
         
        Para elevar una expresión 'a' a la potencia 'b' favor de escribir:
        a**b
         
        Para utilizar la constante pi, favor de escribir 'pi' a la hora de escribir la funcion.
         
        Y por ultimo, recuerde utilizar parentesis para mayor precision y para que se respete mejor 
        la jerarquía de operaciones."""

    def saludar(self):
        print(self.saludo)

    def mostrar_instruccio(self):
        print(self.instruccion)
