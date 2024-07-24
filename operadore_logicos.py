Edad_minima = 21

edad = int(input("Ingrese su edad:"))
categoria = input("Ingrese su categoria(A, B, C, D, E, F, G)")

if edad >= Edad_minima and (categoria == "D" or categoria == "d"):
    print("Puede conducir ambulancia")
else:
    print("No puede conducir ambulancia")    