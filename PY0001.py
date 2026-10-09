lista = []

while True:
    tarea = input("Introduce una tarea (o escribe 'fin' para terminar): ")

    if tarea.lower() == "fin":
        break

    lista.append(tarea)

print("\nLista de tareas:")

for i in range(len(lista)):
    print(str(i + 1) + ". " + lista[i])