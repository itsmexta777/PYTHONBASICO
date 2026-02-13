# Numeros
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1 + 2))
print(int(10*2))
print(int(1 + 4 -2))
print(float(1 + 2.0))

# operadores matematicos
# +
# -
# *
# /
# **
# % Modulo

print(int(2**3))
print(int(4**8))
print(float(10%3))
print(float(25%4))
print(float(16%2))
print(float(10 / 3))

# variables en python
print("=======VARIBLAES========")
x = 100
y = 1
print(x + y)

ventas = 1999991
print("Nuestras ventas fueron: ", ventas)

is_active = True
print(is_active)

game_over = False
print(game_over)

some_string = "Hola soy un string"
print(some_string)

print("=========condicionales=====")
edad = 18

if (edad>= 18):
    print("Si puedes entrar al Bar")
else:
    print("No puedes entrar al Bar")

mi_numero = int(input("¿Cual es el numero que deseas verficar?"))
print(f"El numero que desea verificar es {mi_numero}")
if mi_numero % 2 == 0:
    print(f"El numero {mi_numero} es par!")
else:
    print(f"El numero {mi_numero} es inpar!!")

def par_inpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par!")
    else:
        print(f"El numero {numero} es unpae!!")

print("=========FUNCION PAR_INPAR=====")
mi_numero = int(input("¿Cual es el numero que desea verificar?"))
print(f"El numero que desea verificar es {mi_numero}")
print(par_inpar(mi_numero))
