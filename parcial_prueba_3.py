""" Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor , hasta que el cliente quiera:
peso (entre 10 y 1000)en kilo,
precio por kilo (más de cero ),
tipo validad("v";"a";"m")(vegetal,animal o mezcla )
Si compro más de 100 kilos en total tenes 15% de descuento sobre el total a pagar.
Si compro más de 300 kilos en total tenes 25% de descuento sobre el total a pagar.
Se debe Informar al usuario lo siguiente:
a)El importe total a pagar , bruto sin descuento y...
b)el importe total a pagar con descuento(solo si corresponde)
d)Informar el tipo de alimento más caro.
f)El promedio de precio por kilo en total. """

PESO_MIN = 10
PESO_MAX = 1000

PRECIO_KILO = 1

TIPO_ANIMAL = "ANIMAL"
TIPO_VEGETAL = "VEGETAL"
TIPO_MEZCLA = "MEZCLA"

DESCUENTO_100 = 0.15
DESCUENTO_300 = 0.25

flag = True

while flag:
    
    peso_comida = int(input(f"Ingrese el peso de la comida Min {PESO_MIN}kg y Max {PESO_MAX}: "))
    while peso_comida < PESO_MAX and peso_comida > PESO_MAX:
        print("Error!!!!!")
        peso_comida = int(input(f"Ingrese el peso de la comida Min {PESO_MIN}kg y Max {PESO_MAX}: "))

    precio_por_kilo = float(input("Ingrese el precio por kilo mayor a 0:"))
    while precio_por_kilo < PRECIO_KILO:
        print("Error!!!!!")
        precio_por_kilo = float(input("Ingrese el precio por kilo mayor a 0:"))



    continuar_ingresando_comida = input("¿Desea seguir ingresando? [SI/NO]: ").upper()
    if continuar_ingresando_comida != "SI" and continuar_ingresando_comida != "NO":
        continuar_ingresando_comida = input("ERROR. Ingrese la respuesta correcta => [SI/NO]: ").upper()
    elif continuar_ingresando_comida != "SI":
        flag = False
