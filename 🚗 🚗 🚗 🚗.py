# realizar un programa que de solucion a lo sgte
# Ingresar 5 ALUMNOS (nombre, apellido, nota, etc)
# Calcular el promedio de todos los alumnos (notas)
# Calcular el promedio total de el curso
# Calcular el mejor promedio

def promedio_alumnos(a, b, c, d, e):
    # Variable local

    prom = 0
    prom = (a + b + c + d + e)/5
    return prom

def promedio_Notas(a, b, c, p1, p2, p3):

    prom = 0
    prom = (a * p1 + b * p2 + c * p3)/100
    return prom

# Nota 1 vale el 20%
# Nota 2 vale 30%
# Nota 3 vale 50%

notas = [0,0,0]
alumnos = [0,0,0,0,0]

#ponderado
pon = [20,30,50]

print("Bienvenido a INSUCO")
print("")

for a in range(0,5,1):

    print(f"ALUMNO {a+1}")
    alumnos[a] = (input("Ingrese nombre del alumno: "))
    # Nota variable ingresada
    notas[0] = float(input("Ingrese su primera nota: "))
    notas[1] = float(input("Ingrese su segunda nota: "))
    notas[2] = float(input("Ingrese su tercera nota: "))

    prom = promedio_Notas(notas[0], notas[1], notas[2], pon[0], pon[1], pon[2])
    print (" El promedio de notas del alumno es de", prom)
    print("")



