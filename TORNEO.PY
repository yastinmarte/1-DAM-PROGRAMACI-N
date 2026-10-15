
mario_kart = {"Ana", "Luis", "Pedro", "Marta", "Hugo"}
minecraft = {"Luis", "Marta", "Sara", "David"}
rocket_league = {"Pedro", "Marta", "David", "Elena"}

opcion = 0
while opcion != 9:
    print("\n1. Mostrar todos los participantes")
    print("2. Comunes a Mario Kart y Minecraft")
    print("3. Inscritos en los tres torneos")
    print("4. De Mario Kart que no están en Minecraft")
    print("5. En Minecraft o Rocket League, pero no en ambos")
    print("6. Añadir un participante a un torneo")
    print("7. Eliminar un participante de un torneo")
    print("8. Consultar torneos de una persona")
    print("9. Terminar")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(mario_kart , minecraft , rocket_league)
    elif opcion == 2:
        print(mario_kart , minecraft)
    elif opcion == 3:
        print(mario_kart , minecraft , rocket_league)
    elif opcion == 4:
        print(mario_kart - minecraft)
    elif opcion == 5:
        print(minecraft ^ rocket_league)
    elif opcion == 6 or opcion == 7:
        torneo = input("Torneo (1=Mario Kart, 2=Minecraft, 3=Rocket League): ")
        nombre = input("Nombre: ")
        if torneo == "1":
            conjunto = mario_kart
        elif torneo == "2":
            conjunto = minecraft
        else:
            conjunto = rocket_league

        if opcion == 6:
            conjunto.add(nombre)
            print("Añadido.")
        else:
            conjunto.discard(nombre)
            print("Eliminado.")
    elif opcion == 8:
        nombre = input("Nombre: ")
        if nombre in mario_kart:
            print("Mario Kart")
        if nombre in minecraft:
            print("Minecraft")
        if nombre in rocket_league:
            print("Rocket League")
    elif opcion == 9:
        print("Adiós")
    else:
        print("Opción no válida")