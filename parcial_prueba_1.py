""" Debemos realizar la carga de 5(cinco) productos de prevención de contagio,
de cada una debo obtener los siguientes datos:
el tipo (validar "barbijo" , "jabón" o "alcohol", “guardapolvo”, “guantes”) ,
el precio (validar entre 100 y 300),
la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades),
la Marca y el fabricante.
Se debe Informar al usuario lo siguiente:
a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
b) Del ítem con más unidades, el fabricante
c) Cuántas unidades de jabones hay en total """



TIPO_BARBIJO = "BARBIJO"
TIPO_JABON = "JABON"
TIPO_ALCOHOL = "ALCOHOL"
TIPO_GUARDAPOLVO = "GUARDAPOLVO"
TIPO_GUANTES = "GUANTES"

PRECIO_MIN = 100
PRECIO_MAX = 300

UNIDADES_MAXIMA = 1000
UNIDADES_MINIMA = 1

BARBIJO_MAS_CARO = 0

PRODUCTO_MAX_UNIDADES = 0

TOTAL_JABON = 0

cantidad_barbijo_mas_caro = 0
fabricate_barbijo_mas_caro = ""

fabricante_producto_max = ""
item_producto_max = ""


contador = 0
    
print("Ingrese el producto que desea elegir entre")
print(f"{TIPO_ALCOHOL}")
print(f"{TIPO_BARBIJO}")
print(f"{TIPO_GUANTES}")
print(f"{TIPO_GUARDAPOLVO}")
print(f"{TIPO_JABON}")

while contador < 3:
    tipo_producto = input("Ingrese el tipo de producto: ").upper()

    while tipo_producto != TIPO_GUARDAPOLVO and tipo_producto != TIPO_ALCOHOL and tipo_producto != TIPO_BARBIJO and tipo_producto != TIPO_GUANTES and tipo_producto != TIPO_JABON:
        print ("ERROR!!! Producto incorrecto")
        tipo_producto = input("Ingrese un producto valido:")

    precio_producto = float(input(f"Ingrese el valor del productos precio min [{PRECIO_MIN}] y el precio max [{PRECIO_MAX}] : "))
    while not(precio_producto >= PRECIO_MIN and precio_producto <= PRECIO_MAX):
        precio_producto = float (input("ERROR!!! Ingrese un valor de productos valido: "))    

    
    cantidad_producto = int(input("Ingrese la cantidad del productos: "))
    while not(cantidad_producto >= UNIDADES_MINIMA and cantidad_producto <= UNIDADES_MAXIMA):
        precio_producto = float (input("ERROR!!! Ingrese una cantidad de producto valida: "))

    marca_producto = input("Ingrese la marca del producto: ")
    fabricante_producto = input("Ingrese el fabricante del producto: ")

    #a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante

    if cantidad_producto == TIPO_BARBIJO and (BARBIJO_MAS_CARO == 0 or precio_producto > BARBIJO_MAS_CARO) :
        BARBIJO_MAS_CARO = precio_producto
        cantidad_barbijo_mas_caro = cantidad_producto
        fabricate_barbijo_mas_caro = fabricante_producto 


    #b) Del ítem con más unidades, el fabricante
    if cantidad_producto > PRODUCTO_MAX_UNIDADES:
        PRODUCTO_MAX_UNIDADES = cantidad_producto
        item_producto_max = tipo_producto
        fabricante_producto_max = fabricante_producto

    #c) Cuántas unidades de jabones hay en total
    if tipo_producto == TIPO_JABON:
        TOTAL_JABON += cantidad_producto

    contador += 1


#a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
if BARBIJO_MAS_CARO > 0:
    print(f"El barbijo más caro cuesta ${BARBIJO_MAS_CARO}, la cantidad de unidades es {cantidad_barbijo_mas_caro}, y el fabricante es {fabricate_barbijo_mas_caro}.")
else:
    print("No se ingresaron barbijos.")
    

#b) Del ítem con más unidades, el fabricante
print(f"El ítem con más unidades es {item_producto_max}, el fabricante es {fabricante_producto_max}, y la cantidad es {PRODUCTO_MAX_UNIDADES}.")

#c) Cuántas unidades de jabones hay en total
print(f"En total hay {TOTAL_JABON} unidades de jabones.")