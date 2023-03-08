#programa para hallar el punto de corte en el eje x de una funcion lineal

print("---------------------------------")
print("---------puntos de corte---------")
print("---------------------------------")

# input

a = int(input("insterte un numero: "))
b = int(input("inserte un numero: "))

#processing

if( a != 0):
    x = -b / a
    #output
    print(str("el punto de corte en el eje x es: "  +str(x)))

else:
    #output
    print(str("es una funcion constante"))

