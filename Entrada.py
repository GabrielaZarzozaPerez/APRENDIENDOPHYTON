# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

entrada=input()
print(type(entrada))
# La variable booleana contiene el resultado de verificar 
# Si lo capturado es digito, y si no se encuentra un punto 
# en lo capturado, lo que indicaria se que trata de un 
# numero con decimales, es decir, float. Si find retorna -1
# quiere decir que lo buscado, en este caso con punto decimal
# no se encontro. Si esEntero es True, lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if(esEntero):
    # Lineas que se ejecutaran si la condicion es verdera (true)
    print("Dato entero. ¡Muy bien!")
else:
    # Las lineas que se ejecutaran si la condicion es falsa (false)
    print("Dato que no es entero. Intentar nuevamente")
