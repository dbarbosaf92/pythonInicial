""" La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

CONFECCIÓN DE UN COMETA: 

Medidas:

AB = Diágonal mayor

DC = Diágonal menor

BD y BC = lados menores

AD y AC = lados mayores

El usuario ingresará las medidas  BC, CD y DA.

Detalles de construcción

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
 """

#establecemos las cosntantes
CENTIMETROS_EN_METRO = 100
CANTIDAD_COMETAS = 10
PORCENTAJE_COLA = 0.10


#establecemos variables correspondientes a cada lado
lado_bc = float(input("Ingrese la medida del lado menor BC en centimetros: "))
#establecer de que no puedan poner un lado negativo
while lado_bc <= 0: 
    lado_bc = float(input("ERROR!!. Ingrese nuevamente la medida del lado menor BC en centimetros: "))

lado_cd = float(input("Ingrese la medida de la diagonal menor CD en centimetros: "))
#establecer de que no puedan poner un lado negativo
while lado_cd <= 0: 
    lado_cd =  float(input("ERROR!!.I ngrese nuevamente la medida de la diagonal menor CD en centimetros: "))    

lado_da = float(input("Ingrese la medida del lado mayor DA en centimetros: "))
while lado_da <= 0 or lado_da > lado_cd: 
#establecer de que no puedan poner un lado negativo y que el lado mayor sea mayor al menor
    lado_da =  float(input("ERROR!!. Ingrese nuevamente la medida del lado mayor DA en centimetros: "))


#Calculamos ab usando el teorema de pitagoras
lado_ab = (lado_da**2 + lado_bc**2)**0.5


# Establecemos el perímetro del cometa (varillas necesarias para los lados)
perimetro = (lado_bc * 2) + (lado_da * 2)

#medidas de las varillas incluyendo las diagonales
total_varillas = perimetro + lado_ab + lado_cd

#establecemos el area del cometa
area = float((lado_ab * lado_cd) / 2)

#la cola de la cometa es = area del cometa * el 10%
cola_cometa = area * PORCENTAJE_COLA

total_papel = area + cola_cometa

#creamos la variable papel, el cual es igual a el area + la cola por la cantidad de cometas (10) divido 100 (centimetros para 1 metro)
total_papel_metros = ( total_papel * CANTIDAD_COMETAS) / (CENTIMETROS_EN_METRO**2)

#establecemos el total de metros para las varillas 
total_varillas_metros = (total_varillas * CANTIDAD_COMETAS) / CENTIMETROS_EN_METRO

#Resultado
print(f"Se necesitara {total_papel_metros: .2f} metros de papel y {total_varillas_metros:.2f} metros de varilla para construir 10 cometas") 


