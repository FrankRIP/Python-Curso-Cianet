'''
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
'''

practica1 = float(input("Ingrese el valor de la Practica 1: "))
practica2 = float(input("Ingrese el valor de la Practica 2: "))
practica3 = float(input("Ingrese el valor de la Practica 3: "))
examparc = float(input("Ingrese el valor del examen parcial: "))
examfin = float (input("Ingrese el valor del examen final: "))

promedioprac = (practica1 + practica2 + practica3) / 3
promediofin = (promedioprac + 2*examparc + 3*examfin) /6

print ("El promedio de practicas del alumno es de:\n", promedioprac, "\n Y el promedio final es de:\n ", promediofin)