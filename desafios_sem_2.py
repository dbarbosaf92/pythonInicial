
#Ejericios 2A
#1
""" a = int(input("Ingrese un numero entero:"))

if a == 18:
    print("Usted tiene", a, "años");

#2

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Usted es mayor de edad")
else:
    print("Ustes es menor de edad")

#3

altura = float(input("Ingrese su altura en cm: "));

if altura > 1.80:
    print("Usted puede ser pivot");
else:
    print("Usted no puede ser pivot"); 

#4

edad = int(input("Ingrese su edad: "));

if edad >= 13 and edad <= 17:
    print("Ustes es un adoslecente");


#5

edad = int(input("Ingrese su edad: "));

if edad < 10:
    print("Usted es un niño");
elif edad >= 10 and edad < 13:
    print("usted es un pre-adoslecente");
elif  edad >= 13 and edad <= 17:
    print("Ustes es un adoslecente"); 

 """


#Desafio 1

""" contador = 1

while contador <= 10:
    print(contador);
    contador += 1;

print("termino el ciclo") """


#Ejercicios Prácticos 2-B.


#1

suma_pares = 0;
contador = 1;


while contador < 10:
    if contador % 2 == 0:
        suma_pares += contador;
    contador += 1;

print("suma de los pares:", suma_pares)         


#2

secret_password = "utn750"

password = input("Ingrese su contraseña: ");

while password != secret_password:
        print("Contraseña incorrecta");
        password = input("Ingrese nuevamente la contraseña: ");

print("Contraseña correcta ya puede ingresar.");


#3

numero = int(input("ingrese un numero entre 0 y 9 inclusive: "));

while numero > 9 or numero < 0:
        print("el numero es:", numero);
        print("el numero tiene que ser entre 0 y 9 inclusive"); 
        numero = int(input("ingrese el numero: "));

print("El numero ingresado es:", numero);

#4

letra = input("Ingrese una letra en mayusculas: ");

while letra != "U" and letra != "T" and letra != "N":
        print("la letra es incorrecta")
        letra = input("Ingrese una letra: ");
print("Ingreso una letra correcta:", letra)

#5

suma_numero = 0;
contador = 1;


while contador <= 5:
    numero = int(input("Ingrese un numero: "));
    suma_numero += numero
    contador += 1

promedio = suma_numero / 5
print("la suma de los numeros son:", suma_numero);
print("y el promedio es:", promedio);    



