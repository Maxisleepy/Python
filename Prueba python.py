# Python prueba
# la venta debe tener
# Nombre
# Apellido
# fruta
# Cantidad (en kgs)
# precio de la fruta (Chileno) (Por kilo????)
# Con cuanto paga

# Funciones

# Calcular Precio total
# Calcular Vuelto
# Calcular Nombre completo

def validarvendedor():
        vendedor = ("juan", "pancha", "ruben", "carlos", "pamela")
        while True:
            vendedoor = input(""" ¿Quien lo esta atendiendo? 
juan
pancha
ruben
carlos
pamela

(porfavor escribir el nombre): """).strip().lower()
            if vendedoor in vendedor:
                print("ta bien")
                return vendedoor
                
            else: 
                print("tontito")
                print("")

def validarfruta():
        frutas = ("naranjas", "manzanas", "platanos", "arandanos", "cerezas", "mandarinas", "kiwis")
        while True:
            fruta = input("""naranjas 
manzanas
platanos
arandanos
cerezas
mandarinas
kiwis
escriba la fruta que desee comprar: """).strip().lower()
            if fruta in frutas:
                print("ta bien")
                return fruta
                
            else: 
                print("")

def cod_fruta(fruta):
                if fruta == "naranjas":
                    x = 0
                if fruta == "manzanas":
                     x = 1
                if fruta == "platanos":
                    x = 2
                if fruta == "arandanos":
                     x = 3
                if fruta == "cerezas":
                    x = 4
                if fruta == "mandarinas":
                     x = 5
                if fruta == "kiwis":
                    x = 6
                return x

precio_kilo = [1500, 2390, 1690, 5790, 2800, 1500, 2290]



def validar_kilo():
     kilo = 0 #Fuera del rango, como siempre
     while kilo < 0:
          kilo = float(input("Ingrese precio en kilos: "))
          if kilo < 0:
            print(" nope, tamal ")
            return kilo
          
def calcular_vuelto(a,b):
    vuelto = a - b
    return vuelto

def Calcular_Pago(a,b):
     pago = a * b
     return pago
     
print(" Venta de frutas :D ")

print("¿Cuantos clientes va a querer?")
cc = int(input(""))


for j in range(0,cc,1):

    print("")

    vendedoor = validarvendedor()

    print("")

    nombre = input(" Ingrese su nombre: ")

    print("")

    apellido = input(" Ingrese su apellido: ")

    print("")

    fruta = validarfruta()

    print("")

    kilo = float(input("Cuantos kilos va a comprar: "))

    print("")

    x = cod_fruta(fruta)
    TP = Calcular_Pago(kilo, precio_kilo[x])
    print(f"EL pago total es {TP}")

    moneda = float(input("Con cuanto paga: "))

    Vuelto = calcular_vuelto(moneda, TP)

    print("")

    print(f"HOLA {nombre, apellido}")

    print("")

    print(f"Su vuelto es de {Vuelto}")


    
