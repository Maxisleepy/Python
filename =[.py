# Calcular de el prom 3 EDADES
# Calcular el prom de 3 notas 
# (Una por alumno)
# CALCULAR 3 mesadas

# definicion de promedio
def prom(a,b,c):
    prom = (a + b + c)/3
    return prom

# Calcular edad
def validar_edad():
    edad = 0 # fuera del rango, inicialmente..
    while ((edad <= 10) or (edad >= 25)):
        edad = int(input("ingrese edad "))
        if edad <= 10:
            print("La edad es muy baja para estar en el rango")
        if edad > 25:
            print("La edad es muy alta para estar en el rango")
    return edad

#calcular nota
def validar_nota():
    nota = 0 # fuera del rango, inicialmente..
    while ((nota <= 0) or (nota >= 7)):
        nota = float(input("ingrese nota "))
        if nota <= 0:
            print("La nota es muy baja para estar en el rango")
        if nota > 7:
            print("La nota es muy alta para estar en el rango")
    return nota

# Calcular plata
def validar_plata():
    mesada = 0 # fuera del rango, inicialmente..
    while ((mesada <= 1000) or (mesada >= 10000)):
        mesada = int(input("ingrese mesada "))
        if mesada <= 1000:
            print("La mesada es muy baja para estar en el rango")
        if mesada > 10000:
            print("La mesada es muy alta para estar en el rango")
    return mesada

# Valida genero
def validar_gen():
    generos = ("masculino", "femenino", "otro")
    while True:
        genero = input("Introduce genero (masculino, femenino, otro) ") .strip().lower()
        if genero in generos:
            print("genero", genero, "Validado")
            return genero
    else:
        print("")



# Valida especialidad
def validar_especialidad():
    especialidades = ("programacion", "administracion", "contabilidad", "segundo", "primero")
    while True:
        especialidad = input("""Introduce especialidad 
(programacion, administracion, contabilidad, primero, segundo) 
""") .strip().lower()
        if especialidad in especialidades:
            print("especialidad", especialidad, "Valida")
            return especialidad
    else:
        print("")


print("BIENVENIDO A SEPTIEMBRE")
print("tiki tiki ti")
print("")

especialidad = [0, 0, 0]
genero = [0, 0, 0]
mesada = [0, 0, 0]
nombre = [0, 0, 0]
nota = [0, 0, 0]
edad = [0, 0, 0]

for i in range(0, 3, 1):
    print("DATOS DEL ALUMNO ", i+1)

    nombre[i] = input("ingrese nombre ")
    print("")
    edad[i] = validar_edad()
    print("")
    genero[i] = validar_gen()
    print("")
    especialidad[i] = validar_especialidad()
    print("")
    nota[i] = validar_nota()
    print("")
    mesada[i] = validar_plata()
    print("")



# ALUMNO 1
print("Ingrese su nombre!")
nombre = input("")
print("")
genero = validar_gen()
print("")
especialidad = validar_especialidad()
print("")
edad = validar_edad()
print("edad es ", edad)
print("")
nota = validar_nota()
print("")
mesada = validar_plata()
print("")

#************************************************************************


# ALUMNO 2
print("alum 2")
print("Ingrese su nombre!")
nombre2 = input("")
print("")
genero2 = validar_gen()
print("")
especialidad2 = validar_especialidad()
print("")
edad2 = validar_edad()
print("edad es ", edad2)
print("")
nota2 = validar_nota()
print("")
mesada2 = validar_plata()
print("")
# *********************************************************


#alumno 3
print("alum 3")
print("Ingrese su nombre!")
nombre3 = input("")
print("")
genero3 = validar_gen()
print("")
especialidad3 = validar_especialidad()
print("")
edad3 = validar_edad()
print("edad es ", edad3)
print("")
nota3 = validar_nota()
print("")
mesada3 = validar_plata()
print("")

# Calculars

print("El promedio de nota es de ", prom(nota,nota2,nota3))
print("El promedio de edad es de ", prom(edad,edad2,edad3))
print("El promedio de mesadas es de ", prom(mesada,mesada2,mesada3))
