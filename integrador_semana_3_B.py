'''En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán
pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan
$800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez)
se aplicará el siguiente descuento:
● Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.
● Si compra 5 lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si
es de otra marca el descuento es del 30%.
● Si compra 4 lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un
descuento del 25 % y si es de otra marca el descuento es del 20%.
● Si compra 3 lámparas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es
“FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
Por otro lado, si el importe final con descuento suma más de $4000 se obtiene un descuento adicional
de 5%.
Mostrar por pantalla:
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el
descuento adicional (si corresponde) y el total a pagar con descuento.'''

#Establezco la constante del precio de la lampara, ya que esta es igual para todas las marcas que existe.
PRECIO_LAMPARAS = 800

MARCA_ARGENTINA_LUZ = "ArgentinaLuz"
MARCA_FELIPE_LAMPARAS = "FelipeLamparas"
MARCA_OTRAS = "Otras"



print("\nTENER EN CUENTA QUE SOLO PUEDE COMPRAR UNA MARCA POR VEZ\n")
print("OPCIONES DE MARCA")
print("ArgentinaLuz")
print("FelipeLamparas")
print("Otras")
marca= input("Elegir opcion: ")

#Creamos la variable cantidad de lamparas, en donde el usuario pondra la cantidad de lamparas deseadas.
cantidad_lamparas=int(input("Ingrese la cantidad de lamparas: "))

#Creamos un while para validar la cantidad de lamparas
while cantidad_lamparas <= 0:
    cantidad_lamparas=int(input("ERROR...Ingrese la cantidad de lamparas: "))


precio_sin_descuento = cantidad_lamparas * PRECIO_LAMPARAS

descuento = 0

#Usamos los condicionales para saber el descuento segun la cantidad o marca
if cantidad_lamparas >= 6:
    descuento = 0.5
elif cantidad_lamparas == 5:
    if marca == MARCA_ARGENTINA_LUZ:
        descuento = 0.4
    else:
        descuento = 0.3
elif cantidad_lamparas == 4:
    if marca == MARCA_OTRAS:
        descuento = 0.20
    else:
        descuento = 0.25
elif cantidad_lamparas == 3:
    if marca == MARCA_ARGENTINA_LUZ :
        descuento = 0.15
    elif marca == MARCA_FELIPE_LAMPARAS:
        descuento = 0.10
    else:
        descuento = 0.05


importe_descontado = precio_sin_descuento * descuento

precio_con_descuento = precio_sin_descuento - importe_descontado 

descuento_adicional = 0

precio_con_descuento_adicional = precio_con_descuento

#Usamos condicional si el precio supera los 4000
if precio_con_descuento > 4000:
    descuento_adicional = 0.05
    precio_con_descuento_adicional -= precio_con_descuento_adicional * descuento_adicional

importe_descuento_adicional = precio_con_descuento * descuento_adicional

#Usamos el condicional para saber si el precio tiene o no descuento en el precio final
if importe_descuento_adicional !=0:
    print(f"\nLa marca es {marca}\n La cantidad de lamparas es {cantidad_lamparas}\n El total a pagar sin descuento {precio_sin_descuento}\n El descuento obtenido fue {importe_descontado}\n El descuento adicional fue de {importe_descuento_adicional}\n Total a pagar con descuento {precio_con_descuento_adicional}")
else:
    print(f"\nLa marca es {marca}\n La cantidad de lamparas es {cantidad_lamparas}\n El total a pagar sin descuento {precio_sin_descuento}\n El descuento obtenido fue {importe_descontado}\n Total a pagar con descuento {precio_con_descuento_adicional}")
