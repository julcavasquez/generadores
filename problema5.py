# Teniéndos los siguientes criterios:

# Desaprobado: nota < 11
# Destacado: nota > 16
# Aprobado: para el resto de casos
# notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
# alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
# alumnos_notas = zip(alumnos, notas)

notas = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
def registrar_aprobados(l):
    for l1,l2 in l:
        if l2 > 16:
            yield l1,str(l2) + " (Destacado)"
        elif l2 < 11:
            yield l1,str(l2) + " (Desaprobado)"
        else:
            yield l1,str(l2) + " (Aprobado)"

for cont,(v1,v2) in enumerate(registrar_aprobados(zip(alumnos,notas))):
    print(cont+1,"->",v1,":",v2)
















