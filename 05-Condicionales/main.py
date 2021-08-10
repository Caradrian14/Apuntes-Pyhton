#Condicinal
#IF si se cumple est acondicion se ejecutan las instrucciones, si no se ejecutan otras

#Opereadores de comparacion
"""
 == igual
 != diferencte
 < menor que
 > mayor que
 <= menor o igual que
 >= mayor o igual que

 #operadores logicos
 and = i
 or = o
 ! negacon
 not = no

 """
"""
print("******Ejemplo 1******")
#color = "rojo"
color = input("Cual es tu color favorito ")

if color == "rojo": #== operador de exactamente igual a...
    print("el color es rojo")
else:
    print("el color no es rojo")

#Ejemplo 2
print("******Ejemplo 2******")

year = 2020
year = int(input ("En que año estamos? "))
if year <= 2021:
    print (" Estamos de 2021 en abajo!!")
else:
    print("Es un año superior")

#Ejemeplo 3
print ("***************EJEMPLO 3****************")
nombre = "Victor Robles"
ciudad = "Barcelona"
contniente = "Europa"
edad = 15
mayorEdad = 18
if edad >= mayorEdad:
    #instrucciones
    print(f"{nombre} es mayor de edad")
    if contniente != "Europa":
        print(f"{nombre} No es europeo")
    else:
        print(f"{nombre} es europeo y de la ciudad {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")



#Ejemeplo 4
print ("***************EJEMPLO 4****************")

dia = int(input("Introduce el dia de la semana: "))

if dia == 1:
    print("es lunes")
else:
    if dia == 2:
        print("es martes")
    else:
        if dia == 3:
            print("es miercoles")
        else:
            if dia == 4:
                print("es jueves")
            else:
                if dia == 5:
                    print("es viernes")
                else:
                    print("es fin de semana")
                
# este es un codigo complicado, hay otra opcion
if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana")
            
#Ejemeplo 5
print ("***************EJEMPLO 5****************")
edadMin = 18
edadMaxTrabajo = 65
edad = int(input("Tu edad: "))
if edad >= edadMin and edad <= 65:
    print("esta en edad de trabajar")
else:
    print("no est aen edad de trabajar")

#Ejemeplo 6
print ("***************EJEMPLO 6****************")
pais = "españa"
if pais == "mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"en {pais} no hablan en hispano")


#Ejemeplo 7
print ("***************EJEMPLO 7****************")
pais = "colombia"
if not (pais == "mexico" or pais == "españa" or pais == "colombia"):#no cumple la condicion
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"en {pais} SI hablan en hispano")
    """

#Ejemeplo 8
print ("***************EJEMPLO 8****************")
pais = "sacwcawc"
if pais != "mexico" and pais != "españa" and pais != "colombia":#no cumple la condicion
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"en {pais} SI hablan en hispano :)")
