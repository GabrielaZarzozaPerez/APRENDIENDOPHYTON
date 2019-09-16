# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

numero=str("")

# Al colocar True como condicion de while, se forma un 
# ciclo infinito que no se rompera hasta que de forma 
# explicita se utilize la instruccion break.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        # Si el numero es vacio, reporta la situacion y sale.
        print("Vacio. Salida del programa.")
        break
    else:
        # Si se proporciono valor, acumulado = acumulado + numero
        # Se realiza el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
