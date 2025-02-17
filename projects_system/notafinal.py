#Calcular nota final del estudiante 
nombre = input("Introduce el nombre del estudiante: ")
#El sistema pide la nota del estudiante
nota1 = float(input("Introduce la nota 1: "))
nota2 = float(input("Introduce la nota 2: "))
nota3 = float(input("Introduce la nota 3: "))

#Calcular la nora final 
notafinal = (nota1 + nota2 + nota3)/3

#Mostrar nombre de estudiante en mayuscula 
nombreMayuscula = nombre.upper()
#Mostrar nombre de estudiante en minuscula 
nombreMinuscula = nombre.lower()

#Imprimimos el resultado 
print("Introduce la nota 1: ", nota1)
print("Introduce la nota 2: ", nota2)
print("Introduce la nota 3: ", nota3)
print("Nota final: ", notafinal)
print("Nombre en Mayuscula: ", nombreMinuscula)
print(nombreMayuscula)
