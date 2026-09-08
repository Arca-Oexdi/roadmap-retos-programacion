"""
Estructuras de datos en Python
"""


# Listas: Varios elementos odernados.
from os import name


from os import name
from unittest import case


print("LISTAS:")
print()

mi_lista = ["sunjamer", # Orden 0
            "Pedro", # Orden 1
            "@canal_sunjamer", # Orden 2
            "47"] # Orden 3
print(mi_lista)
print() 

# Inserción de datos en una lista
mi_lista.append("Agregado") 
print(mi_lista)
print()

# Eliminación de datos en una lista
mi_lista.remove("Agregado")
print(mi_lista)
print()

# Acceso a la posición de la lista
print(mi_lista[2]) # Imprime "@canal_sunjamer"
print()

# Modificación de un elemento en la lista
mi_lista[0] = "Nuevo Valor"
print(mi_lista)
print()

# Ordenación de la lista
mi_lista.sort() # Ordena alfabéticamente
print(mi_lista)
print(type(mi_lista)) # Muestra el tipo de la variable, que es <class 'list'>
print()

# Tuplas: Varios elementos ordenados, pero inmutables.
print("TUPLAS:")
print()

mi_tupla: tuple = ("Gatos", "Carros", "Edificios", "Heroes")
print(mi_tupla)
print(type(mi_tupla)) # Muestra el tipo de la variable, que es <class 'tuple'>
print()

# Acceso a los elementos de la tupla
print(mi_tupla[1]) # Imprime en el orden que se selecciono de la tupla
print()

# Ordenacion de la tupla
mi_tupla = tuple(sorted(mi_tupla)) # Ordena alfabéticamente
print("Ordenada en orden alfabético:", mi_tupla)

# Acceso a los elementos de la tupla
print("El orden 2 de la tupla mi_tuple es:", mi_tupla[2]) # Imprime en el orden que se selecciono de la tupla
print()

# Ordenacion de la tupla
mi_tupla = tuple(sorted(mi_tupla)) # Ordena alfabéticamente
print(type(mi_tupla)) # Muestra el tipo de la variable, que es <class 'tuple'>
print()

print("Ordenada en orden alfabético:", mi_tupla)
print(type(mi_tupla)) # Muestra el tipo de la variable, que es <class 'tuple'>
print()

# Sets: Varios elementos desordenados, pero no permite duplicados.
print("SETS:")

my_set: set = {"Colombia", "Carros", "@Edificios", "Cococete"}
print("Conjunto inicial:", my_set)
print()

my_set.add("Confinamiento") # Inserción
print("Conjunto después de agregar 'Confinamiento':", my_set)
print()

my_set.remove("Carros") # Eliminación
print("Se elimino 'Carros':", my_set)
print()

my_set = set(sorted(my_set)) # Ordenación
print(my_set)
print(type(my_set)) # Muestra el tipo de la variable, que es <class 'set'>
print()

# Diccionarios: Varios elementos desordenados, pero con clave y valor.
print("DICCIONARIOS:")
print()

my_dict: dict = {
    "name": "Colombia",
    "surname": "Sebastian",
    "alias": "@el_makia",
    "age": "27"
}
print("Diccionario inicial:", my_dict)
print()

print("Insercion de un nuevo elemento en el diccionario:")
print()

my_dict["moto"] = "honda"
print(my_dict)
print()

print("Eliminacion de un elemento del diccionario:")
print()

del my_dict["surname"] # Eliminación
print(my_dict)
print()

print("Acceso a un elemento del diccionario:")
print(my_dict["name"]) # Acceso
print()

print("Actualizacion de un elemento del diccionario:")
print()

my_dict["age"] = "28" # Actualización
print(my_dict)
print()

print("Ordenacion del diccionario:")
print()

my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict)) # Muestra el tipo de la variable, que es <class 'dict'>


# Uso de funciones con el uso de las estructuras de control de datos
print("USO DE FUNCIONES CON EL USO DE LAS ESTRUCTURAS DE CONTROL DE DATOS:")
print()

def my_agents():

    agenda = {}

    def add_contact():
        phone = input("Ingresa tu número de teléfono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes de ingresar un numero de telefono maximo de 11 digitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Agregar contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Ingresa el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Igrese el nombre del contacto: ")
                add_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar")
                if name in agenda:
                    add_contact()
                else:
                    print(f"El contaco {name} no existe.")
            case "4":
                name = input("Ingrese el nombre del contaco a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado")
                else:
                    print(f"El contacto {name} no existe para ser eliminado.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Esta opcion no es valida. Elige alguna de las opciones del 1 al 5.")

my_agents()