""" En un gimnasio se necesita un programa que permita ingresar datos de 20 socios Por cada socio, se
ingresa:
• Nombre completo.
• Tarifa Base (10000, no se podrá ingresar otro valor)
• Altura (en centímetros, mayor a 100 y menor a 250).
• Peso (en kilogramos, mayor a 30 y menor a 200).
• Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o
"Funcional".

Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por
print):
Los socios que realicen:
● Musculación, tendrán un incremento del 10%.
● Cardio, tendrán incremento del 10%.
● Funcional, un descuento del 10%

A. Por el número de DNI del alumno:
1. Terminados en 0 o 1:
● Informar la cantidad total de socios que realizan “Musculación” y su altura es
superior a “165”.

● El promedio total recaudado de los socios que realizan “Cardio” y su altura es
superior a “110”.
● El nombre y la altura del socio que realiza “Funcional” de menor peso.
2. Terminados en 2 o 3:
● Informar la cantidad total de socios que realizan “Cardio” y su altura es superior
a “165”.
● El promedio total recaudado de los socios que realizan “Funcional” y su altura es
superior a “110”.
● El nombre y la altura del socio que realiza “Musculación” de menor peso.
3. Terminados en 4 o 5:
● Informar la cantidad total de socios que realizan “Funcional” y su altura es
superior a “165”.
● El promedio total recaudado de los socios que realizan “Musculación” y su altura
es superior a “110”.
● El nombre y la altura del socio que realiza “Cardio” de menor peso.
4. Terminados en 6 o 7:
● Informar la cantidad total de socios que realizan “Musculación” y su altura es
inferior a “165”.
● El promedio total recaudado de los socios que realizan “Cardio” y su peso es
superior a “80”.
● El nombre y la altura del socio que realiza “Funcional” de mayor peso.
5. Terminados en 8 o 9:
● Informar la cantidad total de socios que realizan “Funcional” y su altura es
inferior a “165”.
● El promedio total recaudado de los socios que realizan “Musculación” y su peso
es superior a “120”.
● El nombre y la altura del socio que realiza “Musculación” de mayor peso.

B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
C. Los porcentajes de cada tipo de rutina de entrenamiento. Ejemplo: [30% Cardio, 40%
Funcional, 30% Musculación] """



contador = 0

TARIFA_BASE = 10000

ALTURA_MAX = 250
ALTURA_MIN = 100

PESO_MAX = 200
PESO_MIN = 30

RUTINA_CARDIO = "CARDIO"
RUTINA_MUSCULACION = "MUSCULACION"
RUTINA_FUNCIONAL = "FUNCIONAL"

DESCUENTO = 0.1
INCREMENTO = 0.1

socios_altura_musculacion = 0
contador_altura_cardio = 0
total_tarifa_cardio = 0

socio_funcional_menor_peso = None
peso_funcional_menor = 0


while contador < 3:

    nombre_socio = input("Ingrese su nombre de socio: ")

    tarifa_base_socio = int(input(f"Ingrese la tarifa base unica {TARIFA_BASE} : "))
    while tarifa_base_socio != TARIFA_BASE:
        print("ERROR!! Tarifa base invalida")
        tarifa_base_socio = int(input(f"Ingrese la tarifa base unica {TARIFA_BASE} : "))

    altura_socio = int(input(f"Ingrese su altura es CM mayor a {ALTURA_MIN} y menor a {ALTURA_MAX} : "))
    while not (altura_socio >= ALTURA_MIN and altura_socio <= ALTURA_MAX):
        print("ERROR!! Ingrese una altura valida")
        altura_socio = int(input(f"Ingrese su altura es CM mayor a {ALTURA_MIN} y menor a {ALTURA_MAX} : "))

    peso_socio = int(input(f"Ingrese su peso en KG mayor a {PESO_MIN} y menor a {PESO_MAX} : "))
    while not (peso_socio >= PESO_MIN and  peso_socio <= PESO_MAX):
        print("ERROR!! Ingrese un peso valido")
        peso_socio = int(input(f"Ingrese su peso en KG mayor a {PESO_MIN} y menor a {PESO_MAX} : "))

    rutina_socio = input(f"Ingrese su rutina de entrenamiento: {RUTINA_CARDIO} , {RUTINA_MUSCULACION}, {RUTINA_FUNCIONAL}: ").upper()   
    while rutina_socio != RUTINA_CARDIO and rutina_socio != RUTINA_FUNCIONAL and rutina_socio != RUTINA_MUSCULACION: 
        print("ERROR!! Ingrese una rutina de entrenamiento valida")
        rutina_socio = input(f"Ingrese su rutina de entrenamiento: {RUTINA_CARDIO} , {RUTINA_MUSCULACION}, {RUTINA_FUNCIONAL} ").upper()   

    #Descuento o incremento si es necesario
    tarifa_descuento = TARIFA_BASE * DESCUENTO
    tarifa_con_descuento = TARIFA_BASE - tarifa_con_descuento
    tarifa_con_incremento = TARIFA_BASE + tarifa_descuento
#1. Terminados en 0 o 1:

#● Informar la cantidad total de socios que realizan “Musculación” y su altura es superior a “165”.
    if rutina_socio == RUTINA_MUSCULACION and altura_socio > 165:
        socios_altura_musculacion += 1
#● El promedio total recaudado de los socios que realizan “Cardio” y su altura es superior a “110”.
    if rutina_socio == RUTINA_CARDIO and altura_socio > 110:
        contador_altura_cardio += 1
        total_tarifa_cardio += tarifa_base_socio

#● El nombre y la altura del socio que realiza “Funcional” de menor peso. 
    if rutina_socio == RUTINA_FUNCIONAL and peso_socio < peso_funcional_menor:
        peso_funcional_menor = peso_socio
        socio_funcional_menor_peso = nombre_socio


    contador += 1 


#● Informar la cantidad total de socios que realizan “Musculación” y su altura es superior a “165”

#print (f"La  cantidad total de socios que realizan “Musculación” y su altura es superior a 165 son: {socios_altura_musculacion}")    

#● El promedio total recaudado de los socios que realizan “Cardio” y su altura es superior a “110”.




#● El nombre y la altura del socio que realiza “Funcional” de menor peso. 
