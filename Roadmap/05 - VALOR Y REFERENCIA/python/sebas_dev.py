"""
Valor y referencia

"""

from typing import List

# Tipos de datos por valor 

my_int_a = 10
my_int_b = my_int_a
my_int_b =20
print(my_int_a)
print(my_int_b)
print()

# Tipo de dato por referencia
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)
print()

# Funciones con datos por valor
print("FUNCIONES CON DATOS POR VALOR")
print()

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)
print()


# Funcione con datos por referencia
print("FUNCIONE CON DATOS POR REFERENCIA")
print()

def my_list_func(my_list: List[int]) -> List[int]:
    my_list.append(30)

    my_list_d = my_list
    print(my_list_d)
    my_list_d.append(40)

    return my_list


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)
print()

"""
Extra
"""
print("EXTRA")
print()

# Por valor

def value(value_a: int, value_b: int) -> tuple[int, int]:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")
print()

# POR REFERENCIA
print("POR REFERENCIA")

def ref(value_a: list[int], value_b: list[int]) -> tuple[list[int], list[int]]:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]

my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")
