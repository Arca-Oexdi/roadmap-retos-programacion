"""
Operaciones

"""
print("OPERADORES ")
print()

s1 = "Hola"
s2 = "Python"

# Concatenacion
print("CONCATENACION:")
print()

print(s1 + ", " + s2 + "! ")
print()

# Repeticion
print("REPETICION:")
print()

print(s1[0] + s1[1] + s1[2] + s1[3])
print()

# Longitud
print("LONGITUD:")
print()

print("La longitud de ", s2, "son")
print(len(s2), "caracteres")
print()

# Slicing (Porcion)
print("SLICING:")
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])
print()

# Busqueda
print("BUDQUEDA:")
print("a" in s1)
print("i" in s1)
print()

# Remplazo
print("REMPLAZO:")
print("Se semplaza la", s1.replace("o", "a"))
print()

# Division
print("DIVISION:")
print(s2.split("h"))
print()

# Mayusculas, minusculas y letras en mayusculas
print("La funcion 'upper' transforma la letra ", s1.upper(), "'A MAYUCULA'")
print("La funcion 'lower' transforma la letra ", s1.lower(), "'a minuscula'")
print()

# Eliminacion de espacio al principio y al final
print("ELIMINACION DE ESPACIOS PRINCIPIO+FINAL")
print(" somos unidos ".strip())
print()

# Busqueda al principio y al final
print("BUSQUEDA DE PRINCIPIO Y FINAL")
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))
print()

# Busqueda de la posicion
print("BUQUEDA DE LA POSICION")
print()

s3 = "Colombia es grandisimo"

print(s3.find("grandisimo"))
print(s3.find("Grandisimo"))
print(s3.find("g"))
print(s3.find("e"))

# Busqueda de ocurrencias
print("Imprime lower", s3.lower().count("m"))

# Formateo
print("Saludo:  {}, lenguaje: {}!".format(s1, s2))

# Interpolacion
print(f"Saludo: {s1}, lenguaje: {s2}!")


# Transofomacion
print(list(s3))


# Transformacion de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transofrmaciones numericas
s4 = "123456"
print(s4)
s4 = type(int(s4))
print(s4)

# Comprobaciones variadas
s4 = "123456"
print("isalnum", s1.isalnum())
print("isalpha", s1.isalpha())
print("isalpha", s4.isalpha())
print("isnumeric", s4.isnumeric())

# Codgio extra

def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("somos", "seremos")
# check("amor", "roma")


