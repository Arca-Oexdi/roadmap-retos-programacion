""" Operadores de Python"""

# Operadores Aritméticos
print('Operadores Aritmeticos')
print("Sumar a = 10 + b = 3")
a = 10
b = 3
print()
print(f"Suma: {a+b}")
print()
print(f"Resta:{a-b}")
print()
print(f"Multiplicación: {a*b}")
print()
print(f"Division: {a/b}")
print()
print(f"Modulo: {a%b}")
print()
print(f"Exponenciacion: {a**b}")
print()

# Operadores de Comparacion
print('Operadores de Comparacion')
x = 5
y = 8 
print(f"x == y: {x==y}") # Igual a
print(f"x != y: {x!=y}") # Distinto de
print(f"x > y: {x > y}") # Mayor que
print(f"x < y: {x < y}") # Menor que
print(f"x >= y: {x >= y}") # Mayor o igual que
print(f"x <= y: {x <= y}") # Menor o igual que
print()

# Operadores Logicos
print('Operadores Logicos')
p = True
q = False
print(f"p and q: {p and q}") # AND logico (ambos deben ser True)
print(f"p or q: {p or q}") # OR logico (al menos uno debe ser True)
print(f"not p: {not p}") # NOT logico (invierte el valor de verdad)
print()


# Operadores de Asignacion
print('Operadores de Asignacion')
z = 20

z += 5 # z = z + 5
print(f"Operador de asignacion de suma z += 5: igual a {z}")

z -= 3 # z = z - 3
print(f"Operador de asignacion de resta z -= 3: igual a {z}")

z *= 2 # z = z * 2
print(f"Operador de asignacion de multiplicacion z *= 2: igual a {z}")

z /= 4 # z = z / 4
print(f"Operador de asignacion de division z /= 4: igual a {z}")
print()

# Operadores de Identidad
print('Operadores de Identidad')
lista1 = [1, 2, 3]
lista2 = [1, 4, 3]
lista3 = lista1
print(f"lista1 is lista2: {lista1 is lista2}") # False (objetos diferentes)
print(f"lista1 is lista3: {lista1 is lista3}") # True (
print()

# Operadores de Pertenencia
print('Operadores de Pertenencia')
print(f"1 in lista1: {1 in lista1}") # True
print(f"4 in lista1: {4 in lista1}") # False
print()

# Estructuras de Control en Python
print('Estructuras de Control en Python')

edad = input("Ingrese su edad: ")
edad = int(edad)
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65: # Combina comparacion y operadores logicos
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
print()

# Bucles en Python
print('Bucles en Python en for, while')
print()

for i in range(5): # Este bucle for itera sobre un rango de números del 0 al 4
    print(f"La iteracion sobre 5 obtiene: {i}")
print()

contador = 0
while contador < 5: # Este bucle while itera mientras se cumpla la condicion
    print(f"La iteracion sobre 5 obtiene: {contador}")
    contador += 1
print()

# Excepciones (try, except, else, finally)
try:
    resultado = 10 / 0 # Division por cero (genera una excepcion)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else: # Se ejecuta si no hay excepcion
    print(f"El resultado es: {resultado}")
finally: # Se ejecuta siempre, haya o no excepcion
    print("Fin del programa.")
