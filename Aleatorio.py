# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

# Para utilizarse un modulo en un programa, primero debe 
# importarse, usando la instruccion import
import random

# Se define una variable float, y se le asigna un valor. 
numero1=float(10.5)

# En python, uuna funcion es un conjunto de instrucciones que 
# procesan una tarea especifica, como una unidad de ejecucion.
# Se declara con def. todo el codigo posicionado a la derecha 
# de la definicion, forma parte de la funcion 
def miFuncion():
    # Se convierte en float el numero aleatorio generado por 
    # random.randrange() (solo si esta disponible si se importa 
    # el modulo random)
    numero2=float(random.randrange(1,10)) 
    # Se utilizan meta sustituciones para mostrar resultados.
    mensaje="La suma de {} y {} es {}" 
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la funcion definida en el codigo 
miFuncion()
