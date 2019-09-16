# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

for i in range (1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    # print sin argumentos es un salto de linea
    print()
    # Dentro de un for, se pone otro for
    for j in range (1,11):
        # Aqui i contiene el numero de base de la tabla 
        # y j el elemento de la tabla.
        salida="{} * {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Al concluir con las iteraciones indicadas
        # se ejecuta este codigo, que es un salto de 
        # linea .
        print()
