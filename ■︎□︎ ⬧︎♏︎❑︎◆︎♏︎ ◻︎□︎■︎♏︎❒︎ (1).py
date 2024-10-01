# Array o arreglos
# Validaciones
# Rango numerico (ejemplo: Edad, notas, sueldo, etc)
# Opciones (generos, Alianzas)
# Try except para controlar ERROR

# Ingresar ♋︎ ♌︎ ♍︎ ♎︎ ♏︎ Personajes para un show en la pampilla (♋︎ ♌︎ ♍︎ ♎︎ ♏︎ ingresado por teclado)
# Ingresar personaje por lo siguiente

# Nombre
# Apellido
# Apodo
# Sueldo (el rango entre.. $1.000.000 y $17.000.000)
# Horario (5 opciones, 17 de sept, 18 de sept, 19 de sept y 20 de sept)
# Calcular promedio y nom completo (FUNCIONES)
# Mostrar el artista que mas se le paga

def val_sueldo():
    sueldo = 0
    while((sueldo < 1000000) or (sueldo > 17000000)):
        try:
            sueldo = int(input("Ingrese sueldo del artista "))
            if sueldo < 1000000:
                print("Como se atreven a pagarle menos")
            if sueldo > 17000000:
                print(" le pagan mucho, reintente ")
        except ValueError:
            print(" WAOS ")
    return sueldo

def promedio(a,b,c):
    prom = (a, b, c)/3
    return prom

def validar_dia():
        dias = ("1", "2", "3", "4")
        while True:
            dia = input("""¿Que dia estara perfomando? 
                        
1) 17.09
2) 18.09
3) 19.09
4) 20.09

(porfavor escribir el numero (e.g: 1) ): """).strip().lower()
            if dia in dias:
                print("")
                print(" Perfecto ")
                return dia
                
            else: 
                print("")
                print(" Que ")
                print("")

def diascompletos(sia):
    if dia == "1":
        fecha = "17.09"
    if dia == "2":
        fecha = "18.09"
    if dia == "3":
        fecha = "19.09"
    if dia == "4":
        fecha = "20.09"
    return fecha
    
def maximo(a,b,c):
    mayor = max(a,b,c)
    return mayor

def validar_positivo():
    z = 0
    while((z < 1) or (z > 10002)):
        try:
            z = int(input("Cuantos cantantes quiere que performen?: "))
            if (z < 1):
                print("Se restan?")
            if (z > 100):
                print("help")
        except ValueError:
            print("UHHHHH...")

# Arreglos
nombre = []
apellido = []
apodo = []
dia = []
sueldo = []
edad = []


usuario = input("Ingrese su nombre: ")

print("")
print("")

print(f" Bienvenido {usuario} ")
print("")

z = int(input("Cuantos cantantes quiere que performen?: "))
print("")


for s in range(0,z,1):
    print(" Cantante ", s + 1)
    nombre.append(input("ingrese nombre "))
    apellido.append(input("Ingrese apellido "))
    apodo.append(input("Ingrese apodo "))
    sueldo.append(val_sueldo())
    dia.append(validar_dia())

# Ingrese for para impresion de datos
for s in range(z):
    print("")
    print(apodo[s])
    print(f"El nombre del artista es {nombre [s]}")
    print(f"El apellido del artista es {apellido[s]}")
    print(f"el sueldo del artista es de {sueldo[s]}")
    print(f"Se presentara el {fecha}")
    print("")