# Crear un programa que ingrese 3 Notas para cada alumno
# ingresar la cantidad de alumnos de el curso
# Para cada alumno, ingresar
# Calcular promedio para cada alumno
# nombre
# genero
# notas (1, 2, 3)

print("Bienvenido Estudiantes")
print("")

per = int(input("Cuantas personas quiere "))

print("Primer ciclo")
for i in range(per):
   
    print("")
    nombre = input("ingrese nombre: ")
    
    print("")
    genero = input("INGRESE GENEROOO")

    print("")
    nota1 = float(input("ingrese primera nota: "))
    
    print("")
    nota2 = float(input("Ingrese segunda nota: "))
    
    print("")
    nota3 = float(input("Ingrese tercera nota: "))

    def prom(a,b,c):
        prom = (a,b,c)/3
        return prom
    
    