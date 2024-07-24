
#Desafio del mago

""" print(
"""
""" +================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
|¿Cuál es el número secreto? |
+================================+
 """""")

secret_number = 777

numberUser = int(input(":"));

while numberUser != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!");
    numberUser = int(input("Elige nuevamente un numero: "));

print("¡Bien hecho, Junior! Eres libre ahora.");
print("El numero secreto es:", secret_number);

 """
##### --------MAX----------- ######## 

""" contador=0
max_numero = 0

while(contador<4):
    print("Ingrese un numero")
    num = int(input())

    if num > max_numero:
        max_numero = num

    contador+=1

print("ejecuciones: ",contador)
print("el valor maximo es: ", max_numero) """

### ------------------- MIN ----------------- ###

""" contador=0
min_numero = float("inf")

while(contador<4):
    print("Ingrese un numero")
    num = int(input())

    if num < min_numero:
        min_numero = num

    contador+=1

print("ejecuciones: ",contador)
print("el valor minimo es: ", min_numero) """


contador = 0

while contador < 3: 
    numero_nuevo=float (input("Ingrese un número: "))
    if contador == 0 or numero_nuevo>numero_mayor:
        numero_mayor=numero_nuevo
    contador += 1

print(f"El numero mayor es {numero_mayor}")