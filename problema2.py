# Dada la siguiente lista ['Hola', True, 5, 6.04]

# Imprimir los valores e índices sin utilizar un contador o range.

lista = ['Hola', True, 5, 6.04]
def notas_alumnos(l):
     for l1 in l:
        yield l1

for cont,(v1) in enumerate(notas_alumnos((lista))):
    print(cont,"->",v1)
