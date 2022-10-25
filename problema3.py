# Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], 
# imprimirlos de la siguiente forma:

# 1 -> Jose : 20
# 2 -> Juan : 18
# 3 -> Marcelo : 15

notas = [15,20,18]
alumnos = ["Marcelo", "José", "Juan"]
def notas_alumnos(l):
     for l1,l2 in l:
        yield l1,l2

for cont,(v1,v2) in enumerate(notas_alumnos(sorted(zip(alumnos,notas)))):
    print(cont+1,"->",v1,":",v2)
