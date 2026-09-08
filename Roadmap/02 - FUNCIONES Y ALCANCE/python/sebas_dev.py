"""
Funciones definidas por el usuario
"""

# Funcion simple

def greet():
    print("Funcion simple")
greet()
print()

# Funcion con retorno

def greet_with_return():
    return "Funcion con retorno"
print(greet_with_return())
print()

# Funcion con argumento
def args_greet(greet, name ): # 2. Quedan almacenados en el orden que se definieron
    print(f"{greet}, {name}") # 3. Y se imprimen en el orden que se definieron
args_greet("Hola", "Saul") # 1. Se agregan los argumentos en el orden que se definieron
print()

# Funciones con argumentos predeterminados
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")
default_arg_greet("Saul")
default_arg_greet()  # Utiliza el valor predeterminado
print()

# Funciones con un numero como variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
variable_arg_greet("Alice", "Bob", "Charlie", "David")  # Se pueden pasar múltiples argumentos
print()

# Funciones con un numero como variable que tiene argumentos de retorno
def variable_key_arg_greet(**names):
    for key, name in names.items():
        print(f"Hola, {name} ({key})")

variable_key_arg_greet(
    Alice="Alice", 
    Bob="Bob", 
    Charlie="Charlie", 
    David="David"
)