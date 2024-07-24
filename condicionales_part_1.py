
#Usando el condicional IF

""" a = int(input("Coloca un numero entero A: "));
b = int(input("Coloca un numero entero B: "));

if b != 0:
    division = a / b
    print ("El resultado de la division es", division); """

#Condiciales If y Else

""" a = int(input("Coloca un numero entero A: "));
b = int(input("Coloca un numero entero B: "));

if b != 0:
    division = a / b
    print ("El resultado de la division es", division);
else:
    print ("No se puede dividir por cero, el numero entero tiene que se diferente de : 0") """

# Condicional Elif 
""" 
x = int(input("Coloca un numero entero: "));

if x == 0:
    resultado = "neutro"
elif x > 0:
    resultado = "positivo"
elif x < 0:
    resultado = "negativo"

print(x, "es", resultado)
 """

# Condicionales anidados

print("MENU DE OPCIONES")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administracion")

opcion = int(input("Elegir opcion: "))

#Usando el condicional math(SWITCH)
match opcion: 
    case 1:
        print("VENTAS")
    case 2: 
        print("SOPORTE")
    case 3: 
        print("ADMINISTRACION")
    case _:
        print("Opcion no encontrada")    


#Cadena usando elif
""" 
if opcion == 1:
    print("VENTAS")
elif opcion == 2:
    print("SOPORTE")
elif opcion == 3:
    print("ADMINISTRACION")
else:
    print("Opcion no encotrada")  """   



    