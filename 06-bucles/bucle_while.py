#While 
"""escrutura de control que repite la ejecucion de una serie de 
instrucciones tantas veces como sea necesario, hasta dejar 
de cumplirse la instruccion

while condicion:
    bloque de instrccion
    actualizacion de contador ( se recomienda tener)

contador = 1
while contador <=100:
    print(f"Estoy contando el numero: {contador}")
    contador = contador + 1
print("----------------------")
contador = 1
muestrame = str(0)
while contador <=100:
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1
print(muestrame)
"""
#ejemplo
print("*********************Ejemeplo***********************")
numero_usuario = int(input("De que numero quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
print(f"***El usuario ha elegido la tabla {numero_usuario}***")
contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
print("tabla terminada")
