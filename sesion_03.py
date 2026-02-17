# loops

mi_lista = [1, 2, 3, 4, 5]

for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"el resultado de la suma de mi lista es: {resultado}")

for i in range(2, 9):
    print(i)

mi_lista2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for dia in mi_lista2:
    print(f"feliz {dia}")

for i in range(6):
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i es ahora mayor o igual a 5")
#Practica 2
# Dada la lista mi_lista_2 = ["Lunes", "Martes", "Miercoles", "Jurves", "Viernes"]
# Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# Pista: Usa los dos tipos loops while y for en el mismo programa para lograrlo
# Resultado:
# martes
# miercoles
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes
mi_lista_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

contador = 0
while contador < 3:   # repetir 3 veces
    for dia in mi_lista_2:   # recorrer la lista
        if dia != "Lunes":   # excluir lunes
            print(dia)
    contador += 1
