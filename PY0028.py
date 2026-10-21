nombre_pizza = "Pizzeria la Beata";

#Habrá un mínimo de 3 tipos de pizzas. Pon las que quieras. cada precio se guardará en una variable distinta a las demás.
p_margarita = 8.50
p_cuatro_quesos = 10.00
p_barbacoa = 11.50
p_pepperoni = 9.50
p_hawaiana = 9.00
p_carnivora = 8.00

pizzas = [  {"nombre": "Margarita", "precio": p_margarita},
            {"nombre": "Cuatro quesos", "precio": p_cuatro_quesos},
            {"nombre": "Barbacoa", "precio": p_barbacoa},
            {"nombre": "Pepperoni", "precio": p_pepperoni},
            {"nombre": "Hawaiana", "precio": p_hawaiana},
            {"nombre": "Carnivora", "precio": p_carnivora}]

ingredientes = [
    {"nombre": "Queso extra", "precio": 1.50},
    {"nombre": "Bacon", "precio": 2.00},
    {"nombre": "Champiñones", "precio": 1.00},
    {"nombre": "Aceitunas", "precio": 0.80}
]
#Muestra el nombre de la pizzería. Por ejemplo Pizzería La Beata
print(nombre_pizza);

#El usuario introducirá el dinero que tenga.
dinero = float(input("¿Cuanto dinero tiene? "))

#Muestra las pizzas que hay disponibles y su precio.
for pizza in pizzas:
    print(f"{pizza['nombre']} : {pizza['precio']:.2f} €");

#El usuario solo elegirá una pizza.
eleccion = input("¿Que pizza desea?").strip().lower();

#Una vez que se elija la pizza se le indicará al usuario el precio que lleva, y lo que le queda de saldo.
encontrada = False

for pizza in pizzas:
    if pizza["nombre"].lower() == eleccion:
        encontrada = True
        precio = pizza["precio"]

        if dinero >= precio:
            saldo = dinero - precio
            print(f"El precio de la pizza es {precio:.2f} €")
            print(f"Le queda un saldo de {saldo:.2f} €")
        else:
            print("No tiene suficiente dinero para comprar esta pizza.")
            print(f"Le faltan {precio - dinero:.2f} €")
        break

if not encontrada:
    print("La pizza elegida no está disponible.")

#Se debe dar a elegir si quiere añadir ingredientes extras. Los cuales tendrán un precio extra que se añadirá al de la pizza. Se debe ofrecer al menos 3 ingredientes distintos. El usuario podrá elegir los que quiera. Sin límite. 
else:
    print(f"\nEl precio de la pizza es {precio:.2f} €")

    # Ingredientes extra disponibles
    ingredientes = [
        {"nombre": "Queso extra", "precio": 1.50},
        {"nombre": "Bacon", "precio": 2.00},
        {"nombre": "Champiñones", "precio": 1.00},
        {"nombre": "Aceitunas", "precio": 0.80}
    ]

    # Preguntar si quiere ingredientes extra
    extras = []
    respuesta = input("\n¿Desea añadir ingredientes extra? (si/no): " ).strip().lower()

    while respuesta == "si" or respuesta == "sí":

        print("\n--- INGREDIENTES EXTRA ---")

        for ingrediente in ingredientes:
            print(
                f"{ingrediente['nombre']}: "
                f"{ingrediente['precio']:.2f} €"
            )

        eleccion_extra = input(
            "\n¿Qué ingrediente desea añadir? "
        ).strip().lower()

        ingrediente_encontrado = False

        for ingrediente in ingredientes:
            if ingrediente["nombre"].lower() == eleccion_extra:
                extras.append(ingrediente)
                precio += ingrediente["precio"]
                ingrediente_encontrado = True

                print(
                    f"{ingrediente['nombre']} añadido por "
                    f"{ingrediente['precio']:.2f} €"
                )
                break

        if not ingrediente_encontrado:
            print("Ese ingrediente no está disponible.")

        print(f"\nPrecio actual: {precio:.2f} €")

        respuesta = input(
            "¿Desea añadir otro ingrediente? (si/no): "
        ).strip().lower()

    print("\n--- RESUMEN DEL PEDIDO ---")
    print(f"Pizza elegida: {pizza['nombre']}")

    if extras:
        print("Ingredientes extra:")

        for ingrediente in extras:
            print(
                f"- {ingrediente['nombre']}: "
                f"{ingrediente['precio']:.2f} €"
            )
    else:
        print("Sin ingredientes extra.")

    print(f"Precio total: {precio:.2f} €")

    # Comprobar si tiene dinero suficiente para pagar
    if dinero >= precio:
        saldo = dinero - precio

        # Mostrar el ticket
        print("\n--- Su Pedido ---")
        print(f"El total de su pedido es {precio:.2f}€")
        print(f"Su cambio de {dinero:.2f}€ es: {saldo:.2f}€")
        print()

        print(f"- {pizza['nombre']} {pizza['precio']:.2f}€")

        for ingrediente in extras:
            print(
                f"- Extra de {ingrediente['nombre']} "
                f"{ingrediente['precio']:.2f}€"
            )

        print("\nGracias por su visita.")

    else:
        print("\nNo tiene suficiente dinero para pagar.")
        print("Le faltan {:.2f}€".format(precio - dinero))
        print("Por favor, vuelva a empezar su pedido.")