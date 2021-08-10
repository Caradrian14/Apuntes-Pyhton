#al crear variables no poner caracteres extraños 
mi_texto = "Hola"
mi_texto2 = "Mundo"
#para mostarr comillas en variables
mi_texto2 = "\"Mundo\"" #el caracter \ salta el caracter posterior
mi_texto2 = "'Mundo'"
# - no sirven para crear variables
texto_unido = mi_texto + " " + mi_texto2 + mi_texto + " \n " + mi_texto2#\n es como enter, un punto y aparte
print(texto_unido)
texto_unido = mi_texto + " " + mi_texto2 + mi_texto + " \t " + mi_texto2#\t es como tabular
print(texto_unido)
texto_unido = mi_texto + " " + mi_texto2 + mi_texto + " \r " + mi_texto2#\r borrar lo que hay despues
print(texto_unido)