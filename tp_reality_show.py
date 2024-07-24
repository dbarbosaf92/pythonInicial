


contador = 0
max_votos = -1
min_votos = float("inf")
suma_edades = 0
total_votos = 0

while contador < 3:
     
    participante = input("ingrese el nombre del candidato: ");
    edad = int(input("Ingrese la edad del candidato: "));
    #Usamos bucle para que la edad sea mayor de 25
    while edad < 25:
        print("Ingrese una edad mayor de 25: ")
        edad = int(input(""));
    votos = int(input("Ingrese la cantidad de votos: "));
    #Usamos bucle para que la cantidad de votos sea mayor de 0
    while votos < 0:
        print("La cantidad de votos tiene que ser mayor a 0: ")
        votos = int(input(""));

    # Participante con mas votos
    if votos > max_votos:
        max_votos = votos
        max_votos_nombre = participante
    # Participante con menos votos
    if votos < min_votos:
        min_votos = votos
        min_votos_nombre = participante
        min_votos_edad = edad

     # suma de edades
    suma_edades += edad
    
    # Suma de votos
    total_votos += votos
    
    contador += 1;
#Promedio de las edades
promedio_edades = suma_edades / 3

print("Candidatos con mas votos es:", max_votos_nombre, "con:", max_votos, "votos")
print("Candidatos con menos votos es:", min_votos_nombre, "edad:", min_votos_edad, "años")
print("El promedio de las edades es:", promedio_edades)
print("El total de votos emitidos son:", total_votos)