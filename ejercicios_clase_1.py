
# Escribir un programa que muestre por pantalla “bienvenidos a la utn”

#saludo = 'bienvenidos a la UTN'
#print(saludo)

'''
    Escribir un programa que pregunte el nombre del usuario en la consola(usando input) y
    después de que el usuario lo introduzca muestre por pantalla la cadena ”<nombre>”,
    donde <nombre> es el nombre que el usuario haya introducido
'''

#nombre_usuario = input('Ingrese su nombre: ')

#print("Su nombre es:",nombre_usuario)
#print("Su nombre es: " + nombre_usuario)

'''
    Se deberá obtener tanto el nombre como la edad usando input y luego mostrar los datos concatenados con print.
        Ej: "Usted se llama José y su edad es 66 años
'''

# nombre_usuario = input('Ingrese su nombre: ')
# edad_usuario = int(input('Ingrese su edad: '))

# print("Usted se llama",nombre_usuario, "y su edad es", edad_usuario, "años.")
# print("Usted se llama " + nombre_usuario + " y su edad es " + str(edad_usuario) + " años.")

'''
    Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b), transformarlos en números enteros, realizar la operación suma y luego mostrar el resultado de la misma utilizando print.
        Ej: "El resultado de la suma es: 755"
'''
# operador_a = int(input("Ingrese el primer numero: "))
# operador_b = int(input("Ingrese el segundo numero: "))

# suma = operador_a + operador_b

# print("El resultado de la suma es:", suma)

'''
    Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y división), tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b), transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado de la misma utilizando print.
        Ej: "El resultado de la …… es: 755"
'''
# operador_a = int(input("Ingrese el primer numero entero: "))
# operador_b = int(input("Ingrese el segundo numero entero: "))

# opcion = int(input("Ingrese: 1 => sumar, 2 => restar, 3 => multiplicar o 4 => dividir: "))

# if(opcion == 1):
#     suma = operador_a + operador_b
#     print("El resultado de la suma es:", suma)
# elif(opcion == 2):
#     resta = operador_a - operador_b
#     print("El resultado de la resta es:", resta)
# elif(opcion == 3):
#     multiplicacion = operador_a * operador_b
#     print("El resultado de la multiplicacion es:", multiplicacion)
# elif(opcion == 4):

#     if(operador_b == 0):
#         operador_b = int(input("Error!!. El numero no puede ser 0. Ingrese el segundo numero entero: "))
    
#     division = operador_a // operador_b
#     print("El resultado de la division es:", division)
# else: 
#     print("Error!!. Opcion incorrecta. Ingrese una opcion entre 1 y 4.")

# match opcion:
#     case 1:
#         suma = operador_a + operador_b
#         print("El resultado de la suma es:", suma)
#     case 2:
#         resta = operador_a - operador_b
#         print("El resultado de la resta es:", resta)
#     case 3:
#         multiplicacion = operador_a * operador_b
#         print("El resultado de la multiplicacion es:", multiplicacion)
#     case 4:
#         if(operador_b == 0):
#             operador_b = int(input("Error!!. El numero no puede ser 0. Ingrese el segundo numero entero: "))

#         division = operador_a // operador_b
#         print("El resultado de la division es:", division)
#     case _:
#         print("Error!!. Opcion incorrecta. Ingrese una opcion entre 1 y 4.")


'''
    Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b), transformarlos en números enteros, realizar la operación que nos permita obtener el resto de una división y luego mostrar el resultado de la misma utilizando print.
        Ej: "El resto de dividir 7 por 2 es: 1"
'''

# operador_a = int(input("Ingrese el primer numero entero: "))
# operador_b = int(input("Ingrese el segundo numero entero: "))

# if(operador_b == 0):
#     operador_b = int(input("Error!!. El numero no puede ser 0. Ingrese el segundo numero entero: "))


# resto = operador_a % operador_b

# print("El resto de dividir ", operador_a, " por ", operador_b ," es:", resto)


'''
    Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , transformarlo en número entero y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando print
'''

# sueldo = int(input("Ingrese su sueldo: "))
# INCREMENTO = 15

# sueldo += ((sueldo * INCREMENTO) / 100)
# print("Su sueldo actualizado es :", sueldo)

'''
    Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
    transformarlos en números enteros y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando print
'''

# sueldo = int(input("Ingrese su sueldo: "))
# incremento = input("Ingrese el incremento: ")

# if(not incremento.isdigit()):
#     incremento = int(input("Error!!, El incremento no puede ser menor a 0. Ingrese el incremento: "))

# aumento = ((sueldo * incremento) / 100)
# sueldo_actualizado = sueldo + aumento

# print("Su sueldo actualizado es :", sueldo_actualizado, "y el aumento fue de:", aumento)

'''
    Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por consola(input), transformar en número y mostrar el importe actualizado con un descuento del 20% utilizando print
'''
# importe = float(input("Ingrese su sueldo: "))
# DESCUENTO = 20

# importe -= ((importe * DESCUENTO) / 100)
# importe = importe - ((importe * DESCUENTO) / 100)
# print("El importe actualizado es :", importe)

'''
    Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el usuario por consola, transformarlos en números y mostrar el importe actualizado con el descuento utilizando print.
'''

""" importe = float(input("Ingrese un importe: "))
descuento = float(input("Ingrese el descuento: "))

if(descuento <= 0):
    descuento = int(input("Error!!, El descuento no puede ser menor a 0. Ingrese el descuento: "))

descuento = ((importe * descuento) / 100)
importe_actualizado = importe - descuento

print("El importe actualizado es :", importe_actualizado, "y el descuento fue de:", str(descuento) + "%")

mensaje = f"{descuento}%"
mensaje_2 = "{0}%".format(descuento)

print(mensaje_2)
 """

""" Para el departamento de logística:
A. Es necesario saber la cantidad de camiones que harían falta para transportar los
materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la
cantidad de toneladas necesarias de materiales a transportar. El programa deberá
informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por
viaje 3500kg.
B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo
(en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir
a una velocidad máxima y constante de 90 km/h. """





cantidad_materiales = float(input("Ingrese la cantidad de materiales(en TN): "))

cantidad_en_kg = cantidad_materiales * 1000

peso_maximo_camiones = 3500

camiones_necesarios = cantidad_en_kg // peso_maximo_camiones

if cantidad_en_kg % camiones_necesarios!= 0 :
    camiones_necesarios += 1

print(camiones_necesarios)

print(f"la cantidad de camiones para transportar los materiales son:")

