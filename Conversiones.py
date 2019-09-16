# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

# Se declara una variable str, con una cadena de digitos
numero="1234"
# Se muestra el tipo que tiene la variable. La salida de type()
# no es un str es un dato type.
print(type(numero))
# Se convierte la cadena a su equivalencia int.
numero=int(numero)
# Se muestra como el tipo a cambiado aunque se usa la misma 
# variable 
print(type(numero))
# Se declara un str con neta sustitucion (posiciones donde iran
# los valores proporcionados usando format.
salida="El numero utilizado es{}"
# Se muestra el resultado. La neta sustitucion hara que donde esta 
# {} se colque el valor del numero.
print(salida.format(numero))
