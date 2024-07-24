"""
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito)
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida,
el medio de pago y su precio correspondiente.

 * Lista de precios:
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%.
Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
"""

ENTRADA_GENERAL = "GENERAL"
ENTRADA_CAMPO = "CAMPO"
ENTRADA_PLATEA = "PLATEA"

PRECIO_ENTRADA_GENERAL = 16000
PRECIO_ENTRADA_CAMPO = 25000
PRECIO_ENTRADA_PLATEA = 30000

PAGO_CREDITO = "CREDITO"
PAGO_EFECTIVO = "EFECTIVO"
PAGO_DEBITO = "DEBITO"

GENERO_FEMENINO = "F"
GENERO_MASCULINO = "M"
GENERO_OTRO = "O"


DESCUENTO_CREDITO = 0.8
DESCUENTO_DEBITO = 0.85

contador_platea_debito = 0
contador_entradas_totales = 0
#descuento
acumulador_descuento_credito = 0

contador_femenino = 0
contador_masculino = 0
contador_otro = 0
contador_general_y_pago_credito = 0

flag_entrada_general_debito = True
nombre_persona_entrada_mas_cara = None
edad_persona_entrada_mas_cara = None

contador_personas_plateas_edad_par = 0

acumulador_platea_debito_edad_multiplo_6 = 0


edades_generales = 0

flag = True

while flag:

    nombre_ingresado = (input("Ingrese su nombre: "))

    edad_ingresada = int(input("Ingrese su edad: "))
    while edad_ingresada < 16:
        edad_ingresada = int(input("ERROR, su edad es menor a 16 años. Ingrese nuevamente su edad: "))

    genero_ingresado = input(f"Ingrese su genero: [{GENERO_MASCULINO} para masculino] [{GENERO_FEMENINO} para femenino] [{GENERO_OTRO} para otro]: ").upper()
    while genero_ingresado != GENERO_MASCULINO and genero_ingresado != GENERO_FEMENINO and genero_ingresado != GENERO_OTRO:
        genero_ingresado = input(f"ERROR. Ingrese su genero correctamente => [{GENERO_MASCULINO} para masculino] [{GENERO_FEMENINO} para femenino] [{GENERO_OTRO} para otro]: ").upper()

    tipo_de_entrada_ingresada = input(f"Ingrese su ubicación [{ENTRADA_GENERAL}/{ENTRADA_CAMPO}/{ENTRADA_PLATEA}]: ").upper()
    while tipo_de_entrada_ingresada != ENTRADA_GENERAL and tipo_de_entrada_ingresada != ENTRADA_CAMPO and tipo_de_entrada_ingresada != ENTRADA_PLATEA:
        tipo_de_entrada_ingresada = input(f"ERROR. Ingrese su ubicación correctamente => [{ENTRADA_GENERAL}/{ENTRADA_CAMPO}/{ENTRADA_PLATEA}]: ").upper()
    medio_de_pago = input(f"Ingrese el medio de pago [{PAGO_CREDITO}] [{PAGO_EFECTIVO}] [{PAGO_DEBITO}]: ").upper()
    while medio_de_pago != PAGO_CREDITO and medio_de_pago != PAGO_EFECTIVO and medio_de_pago != PAGO_DEBITO:
        medio_de_pago = input(f"ERROR. Ingrese su medio de pago correctamente => [{PAGO_CREDITO}/{PAGO_EFECTIVO}/{PAGO_DEBITO}]: ").upper()
    contador_entradas_totales += 1

    if tipo_de_entrada_ingresada == ENTRADA_GENERAL:
        precio_final = PRECIO_ENTRADA_GENERAL
    elif tipo_de_entrada_ingresada == ENTRADA_CAMPO:
        precio_final = PRECIO_ENTRADA_CAMPO
    elif tipo_de_entrada_ingresada == ENTRADA_PLATEA:
        precio_final = PRECIO_ENTRADA_PLATEA

    if medio_de_pago == PAGO_DEBITO:
        precio_final *= DESCUENTO_DEBITO
    elif medio_de_pago == PAGO_CREDITO:
        descuento = precio_final * (1 - DESCUENTO_CREDITO)
        precio_final *= DESCUENTO_CREDITO
#       precio_final = precio_final * DESCUENTO_CREDITO
        acumulador_descuento_credito = acumulador_descuento_credito + descuento

    if tipo_de_entrada_ingresada == ENTRADA_CAMPO and genero_ingresado == GENERO_FEMENINO:
        contador_femenino += 1
    elif tipo_de_entrada_ingresada == ENTRADA_CAMPO and genero_ingresado == GENERO_MASCULINO:
        contador_masculino += 1
    elif tipo_de_entrada_ingresada == ENTRADA_CAMPO and genero_ingresado == GENERO_OTRO:
        contador_otro += 1

    if tipo_de_entrada_ingresada == ENTRADA_GENERAL and medio_de_pago == PAGO_CREDITO:
        contador_general_y_pago_credito += 1
        edades_generales += edad_ingresada
    if tipo_de_entrada_ingresada == ENTRADA_PLATEA and medio_de_pago == PAGO_DEBITO:   
        contador_platea_debito += 1

    if flag_entrada_general_debito and tipo_de_entrada_ingresada == ENTRADA_GENERAL and medio_de_pago == PAGO_DEBITO:
        nombre_persona_entrada_mas_cara = nombre_ingresado
        edad_persona_entrada_mas_cara = edad_ingresada
        flag_entrada_general_debito = False


    if tipo_de_entrada_ingresada == ENTRADA_PLATEA and (edad_ingresada % 2) == 0:
        contador_personas_plateas_edad_par += 1

    
    if tipo_de_entrada_ingresada == ENTRADA_PLATEA and medio_de_pago == PAGO_DEBITO and (edad_ingresada % 6) == 0:
        acumulador_platea_debito_edad_multiplo_6 += precio_final

    continuar_compra = input("¿Desea seguir comprando? [SI/NO]: ").upper()
    if continuar_compra != "SI" and continuar_compra != "NO":
        continuar_compra = input("ERROR. Ingrese la respuesta correcta => [SI/NO]: ").upper()
    elif continuar_compra != "SI":
        flag = False


    
#! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo"

if contador_femenino > contador_masculino and contador_femenino > contador_otro:
    print("El genero que mas entradas campo compró es el femenino.")
elif contador_masculino > contador_femenino and contador_masculino > contador_otro:
    print("El genero que mas entradas campo compró es el masculino.")
elif contador_otro > contador_femenino and contador_otro > contador_masculino:
    print("El genero que mas entradas campo compró es el masculino.")

#! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio

if contador_general_y_pago_credito > 0:
    promedio_edades = edades_generales / contador_general_y_pago_credito
    print(f"{contador_general_y_pago_credito} personas compraron la entrada general pagando con tarjeta de credito, y la edad promedio de los compradores es de {promedio_edades:.0f} años.")

#! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito  respecto al total de personas en la lista.
if contador_entradas_totales > 0:
    porcentaje_debito_general =  contador_platea_debito / contador_entradas_totales
    print(f'El porcentaje de entradas sector platea  medio de pago debito fue del: {porcentaje_debito_general * 100}%')

#! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito

print(f'El descuento total tarjeta de credito es: {acumulador_descuento_credito}')

#! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito
# (Solo la primera que se encuentre)

if not flag_entrada_general_debito :
    print(f'La persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito es {nombre_persona_entrada_mas_cara} con {edad_persona_entrada_mas_cara}')
else:
    print(f'Ninguna persona compro una entrada de tipo "General" y pagó con tarjeta de débito')

if contador_personas_plateas_edad_par != 0 :
    print(f'La cantidad de personas que compraron entradas del tipo "Platea" y cuya edad es par es de: {contador_personas_plateas_edad_par}' )
else:
    print('Ninguna persona compro entradas de tipo "Platea" y su edad es par')


if acumulador_platea_debito_edad_multiplo_6 != 0 :
    print(f'el monto total recaudado por la venta de entradas "Platea" pagadas con Debito por personas cuyas edades son múltiplos de 6 es de: {acumulador_platea_debito_edad_multiplo_6}')
else:
    print('Ninguna persona compro entradas de tipo "Platea", pago con Debito y su edad es multiplo de 6')
