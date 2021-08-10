# for, es una estrcutura iterativa que se repite x veces
#for variable in elemento_interable, como lista, datos...
contador = 0
resultado = 0
for contador in range(1,11):
    print(" voy por el " + str(contador))
    resultado += contador

print(f"El resultado es {resultado}")

#ejemplo tablas de multiplicar
print("****************EJEMPLO**************")
numero_usuario = int(input(" De que numero quieres la tabla: "))
if numero_usuario < 1:
    numero_usuario = 1

print(f"#### Tabla de multiplicar del numero usuario {numero_usuario} ####")
for numero_tabla in range(1, 11):#aqui se define una variable
    
    if numero_usuario == 45:
        print("numero prohibido")
        break#rompe el codigo
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("tabla finalizada")
