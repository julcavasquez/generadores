# Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] 
# Imprimirlos de la siguiente forma:

# Marcelo : 15

# José : 20

# Juan : 18

notas = [15,20,18] 
alumnos = ["Marcelo", "José", "Juan"]

for i in dict(zip(alumnos,notas)):
    print(i)
 