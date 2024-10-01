# codigo Mientras :D

# creacion de la funcion PROMEDIO
# A B C son parametros
def promedio(a,b,c):
    prom = (a+b+c)/3
    return  prom
   #Hola          
print("Hola mundo")
print("")

# Hay formas de escribir
# forma 1
print("ingrese primer numero")
num1 = int(input(""))

print("")

# forma 2
num2 = int(input("ingrese segundo numero "))

print("")

print("ingrese tercer numero")
num3 = int(input(""))

print("")

print("El promedio, es: ", promedio(num1, num2, num3))

print("")
print("parte 2")

n1 = 15
n2 = 30
n3 = 70

print("la nota fue de ", promedio(n1,n2,n3))

nota1 = float(input("Ingrese primera nota: "))
nota2 = int(input("ingrese segunda nota: "))
nota3 = int(input("ingrese tercera nota: ")) 
print("EL PROMEDIO DE NOTAS ES ", promedio(nota1,nota2,nota3))

def maximum(a,b,c):
    mayor = max(a,b,c)
    return mayor

print("la mejor nota fue ", maximum(nota1, nota2, nota3))