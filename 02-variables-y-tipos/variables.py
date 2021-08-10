#variables son contenedores de informacion.Pueden modificarse

texto = "Master en Python"
print(texto)
#se puede cambiar una variable, hay que tener cuidado
texto2 = "con Victor Robles"

print (texto + " " + texto2)

numero = 4
numDecimal = 6.7

print(numero)
print(numDecimal)
#al reasignar numero se cambia la vriable, es importante esto
numero = 10
numDecimal = 5.5
print(numero)
print(numDecimal)
print("---------------------------------------------")
#concatenacion
nombre = "Victor"
apellido = "Robles"
web = "VictorRoblesweb.es"

#esto no es concatenacion, solo devuelve el resultado en espacios.
print (nombre, apellido, web)
print(nombre + " " + apellido + ", su web es:" + web)
#otra forma de hacerlo, metodo mas sencillo y limpio, las demas son validas
print(f"{nombre} {apellido} - {web}")
#la f se puede usar para concatenar en calquier variable.
#metodo format, otra manera
print(" hola me llamo {} {}, y mi web es : {}".format(nombre, apellido, web))

