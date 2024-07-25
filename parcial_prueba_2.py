""" En el ingreso a un viaje en crucero nos solicitan
nombre ,
edad(mayores de 18),
sexo("f" o "m") y
estado civil("soltero", "casado" o "viudo");
Se debe Informar al usuario lo siguiente:
a)El nombre del hombre casado más joven.
b)El sexo y nombre del pasajero/a más viejo.
c)La cantidad de mujeres que hay casadas o viudas.
d)El promedio de edad entre las mujeres.
e)El promedio de edad entre los hombres solteros. """


flag = True

EDAD_MAYOR = 18

ESTADO_SOLTERO = "SOLTERO"
ESTADO_CASADO = "CASADO"
ESTADO_VIUDO = "VIUDO"

SEXO_F = "F"
SEXO_M = "M"

edad_casado_joven = 0
nombre_casado_joven = None

edad_pasajero_mas_viejo = None
nombre_pasajero_mas_viejo = None
sexo_pasajero_mas_viejo = None

mujeres_casadas_viudas = 0

edad_suma_mujer = 0 
promedio_edad_mujer = 0
total_promedio_edad_mujer = 0

edad_suma_hombre_soltero = 0
promedio_edad_hombre_soltero = 0
total_promedio_edad_hombre_soltero = 0

while flag:
    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad(Mayor de 18): "))
    while edad < 18:
        print("Error!! Ingrese una edad valida")
        edad = int(input("Ingrese su edad(Mayor de 18): "))

    sexo = input(f"Ingrese el sexo: [{SEXO_F}] [{SEXO_M}]: ").upper()
    while sexo != SEXO_F and sexo != SEXO_M:
        print("Error!! Ingrese un sexo valido")
        sexo = input("Ingrese el sexo: [F] [M]")


    estado_civil = input(f"Ingrese su estado civil {ESTADO_CASADO}, {ESTADO_SOLTERO}, {ESTADO_VIUDO}: ").upper()
    while estado_civil != ESTADO_CASADO and estado_civil != ESTADO_SOLTERO and estado_civil != ESTADO_VIUDO:
        print("Error!! Ingrese un estado civil valido")
        estado_civil = input(f"Ingrese su estado civil {ESTADO_CASADO}, {ESTADO_SOLTERO}, {ESTADO_VIUDO}").upper()

#a)El nombre del hombre casado más joven.
    if estado_civil == ESTADO_CASADO and sexo == SEXO_M and (edad_casado_joven == 0 or edad < edad_casado_joven):
        edad_casado_joven = edad
        nombre_casado_joven = nombre 


#b)El sexo y nombre del pasajero/a más viejo.
    if edad_pasajero_mas_viejo == None  or edad > edad_pasajero_mas_viejo:
        edad_pasajero_mas_viejo = edad
        nombre_pasajero_mas_viejo = nombre
        sexo_pasajero_mas_viejo = sexo



#c)La cantidad de mujeres que hay casadas o viudas.
    if sexo == SEXO_F and (estado_civil != ESTADO_SOLTERO):
        mujeres_casadas_viudas += 1

#d)El promedio de edad entre las mujeres.
    if sexo == SEXO_F:
        edad_suma_mujer += edad
        promedio_edad_mujer += 1
        

#e)El promedio de edad entre los hombres solteros.
    if sexo == SEXO_M and estado_civil == ESTADO_SOLTERO:
        edad_suma_hombre_soltero += edad
        promedio_edad_hombre_soltero += 1

    continuar_ingresando_pasajeros = input("¿Desea seguir ingresando? [SI/NO]: ").upper()
    if continuar_ingresando_pasajeros != "SI" and continuar_ingresando_pasajeros != "NO":
        continuar_ingresando_pasajeros = input("ERROR. Ingrese la respuesta correcta => [SI/NO]: ").upper()
    elif continuar_ingresando_pasajeros != "SI":
        flag = False


#if edad_casado_joven > 0:
#   print(f"El nombre del hombre casado mas joven es {nombre_casado_joven}.")
#else:
#    print("No se ingreso ningun hombre casado")

#b)El sexo y nombre del pasajero/a más viejo.
#print(f"El nombre del pasajero mas viejo es {nombre_pasajero_mas_viejo} y el sexo es {sexo_pasajero_mas_viejo}")    

#c)La cantidad de mujeres que hay casadas o viudas.
#print(f"la cantidad de mujeres que hay casadas o viudas son {mujeres_casadas_viudas}")


#d)El promedio de edad entre las mujeres.
#total_promedio_edad_mujer = edad_suma_mujer / promedio_edad_mujer
#if promedio_edad_mujer > 0:
#    print(f"el promedio de edad entre las mujeres es {total_promedio_edad_mujer:.2f}")
#else:
#    print("no hay ninguna mujer")
#e)El promedio de edad entre los hombres solteros.
#total_promedio_edad_hombre_soltero = edad_suma_hombre_soltero / promedio_edad_hombre_soltero
#print(f"el promedio de edad entre las mujeres es {total_promedio_edad_hombre_soltero:.2f}")
