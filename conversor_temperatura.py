# programa para convertir una cantidad a grados centigrados a su equivalencia en Farenheit y kelvin

print("-------------------------------------------")
print("-------Valor De Grados Centigrados --------")
print("-------------------------------------------")

# input
c = int (input ("digite el valor de c:"))

# processing
F =  ( c * 1.8 + 32 )
k = (c + 273.15)

# output
print("-------------------------------------------")
print("---------------RESULTADOS------------------")
print("-------------------------------------------")
print ( "la coversion en farenhell en" + str (F))
print ( "la conversion de kelvin es" + str (k))
