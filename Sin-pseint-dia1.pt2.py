# condicional SI
# debe ingresar 2 usuarios
# debe ingresar su nombre y el color de la alianza

# COntador de el color AZUL
cont_azul = 0
cont_green = 0
cont_yellow = 0

print(" BIENVENIDO A ANIVERSARIO INSUCO ")
print("")

# INGRESE DE USUARIO

# CAPTA EL NOMBRE DE USUARIO

nombre1 = input("¿CUAL ES TU NOMBRE? ")

print ("seleccione el color de su alianza preferita ")
print ("1 si es rojo")
print ("2 si es verde")
print ("3 si es amarillo")
color1 = input("")

if color1 == "1":
    cont_azul = cont_azul + 1
else: color1 == "2"
cont_green = cont_green + 1
if color1 == "3":
    cont_yellow = cont_yellow + 1
    
#Usuario 2

nombre2 = input("Cual es tu nombre? ")

print ("seleccione el color de su alianza preferita ")
print ("1 si es rojo")
print ("2 si es verde")
print ("3 si es amarillo")
color2 = input("")

if color2 == "1":
    cont_azul = cont_azul + 1
else: color2 == "2"
cont_green = cont_green + 1
if color2 == "3":
    cont_yellow = cont_yellow + 1
        
#USUARIO 3

nombre3 = input("¿CUAL ES TU NOMBRE? ")

print ("seleccione el color de su alianza preferita ")
print ("1 si es rojo")
print ("2 si es verde")
print ("3 si es amarillo")
color3 = input("")

if color3 == "1":
    cont_azul = cont_azul + 1
else: color3 == "2"
cont_green = cont_green + 1
if color3 == "3":
    cont_yellow = cont_yellow + 1
    
#USUARIO 4

nombre4 = input("¿CUAL ES TU NOMBRE? ")

print ("seleccione el color de su alianza preferita ")
print ("1 si es rojo")
print ("2 si es verde")
print ("3 si es amarillo")
color4 = input("")

if color4 == "1":
    cont_azul = cont_azul + 1
else: color4 == "2"
cont_green = cont_green + 1
if color4 == "3":
    cont_yellow = cont_yellow + 1

#USUARIO 5

nombre5 = input("¿CUAL ES TU NOMBRE? ")

print ("seleccione el color de su alianza preferita ")
print ("1 si es rojo")
print ("2 si es verde")
print ("3 si es amarillo")
color5 = input("")

if color5 == "1":
    cont_azul = cont_azul + 1
else: color5 == "2"
cont_green = cont_green + 1
if color5 == "3":
    cont_yellow = cont_yellow + 1
        
print("EL COLOR AZUL TIENE ", cont_azul)
print("EL COLOR VERDE TIENE ", cont_green)
print("EL COLOR AMARILLO TIENE", cont_yellow)