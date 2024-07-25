numero = int(input("Ingrese un numero: "))

divisor = 2
es_primo = True

if(numero <= 1):
    es_primo = False
    
while es_primo and divisor < numero:
    if (numero % divisor == 0):
        es_primo = False
        
    divisor += 1
    
if es_primo:
    print("Es primo")
else:
    print("No es primo")