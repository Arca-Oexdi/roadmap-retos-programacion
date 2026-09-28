"""
Ejercicio

"""

# Pila/Stack (LIFO)

stack = []

# push 
stack.append(1)
stack.append(2)
stack.append(3)
print("Esto imprime", stack)
print()

# pop
stack_item = stack[len(stack) -1]
print("Antes de ser eliminada es:", stack_item)
print()
del stack[len(stack) - 1]
print("Segunda impresion", stack_item)
print()

print("Tercera impresion", stack.pop(0))
print()

print("Cuarta impresion", stack)
print()

# Cola / Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print("Quinta impresion", queue)
print()

# dequeue
queue_item = queue[0]
del queue[0]
print("Sexta impresion", queue_item)
print()

print("Septima impresion", queue.pop(0))
print()

print("Octava impresion", queue)
print()

"Extra"

def web_navigation():
    stack = []

    while True:
        action = input(
            "Añade una url o interactua con palabras delante/atras/sallir"
        )
        if action == "salir":
            print("Saliendo del navegador web.")
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estas en la pagina de inicio.")

web_navigation()