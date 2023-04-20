import random

# Obtener el numero de stakeholders y requisitos
num_stakeholders = int(input("Introduce el numero de stakeholders: "))
num_requisitos = int(input("Introduce el numero de requisitos: "))

# Crear las listas vacias para stakeholders y requisitos
stakeholders = [[] for _ in range(num_stakeholders)]
requisitos = [[] for _ in range(num_requisitos)]

# Llenar las listas de stakeholders y requisitos con valores aleatorios
for i in range(num_stakeholders):
    for j in range(num_stakeholders):
        if i == j:
            stakeholders[i].append(None)
        else:
            stakeholders[i].append(random.randint(1, 10))
    for j in range(num_requisitos):
        stakeholders[i].append(random.randint(1, 10))

for i in range(num_requisitos):
    for j in range(num_stakeholders):
        requisitos[i].append(random.randint(1, 10))

# Ciclo principal del programa
while True:
    # Mostrar menu de opciones
    print("¿Que deseas hacer?")
    print("1. Ver la valoracion de los stakeholders")
    print("2. Ver la valoracion de los requisitos")
    print("3. Valorar un stakeholder")
    print("4. Valorar un requisito")
    print("5. Salir")

    opcion = int(input("Introduce el numero de la opcion que deseas: "))

    if opcion == 1:
        # Mostrar los valores actuales de stakeholders
        print("Valoracion actual de los stakeholders:")
        for i in range(num_stakeholders):
            print(f"Stakeholder {i+1}: {stakeholders[i]}")

    elif opcion == 2:
        # Mostrar los valores actuales de requisitos
        print("Valoracion actual de los requisitos:")
        for i in range(num_requisitos):
            print(f"Requisito {i+1}: {requisitos[i]}")

    elif opcion == 3:
        # Valorar un stakeholder
        print("¿A que stakeholder deseas valorar?")
        for i in range(num_stakeholders):
            print(f"{i+1}. Stakeholder {i+1}")
        stakeholder = int(input("Introduce el numero del stakeholder: "))

        print("¿Que stakeholder deseas valorar?")
        for i in range(num_stakeholders):
            if i+1 != stakeholder:
                print(f"{i+1}. Stakeholder {i+1}")
        stakeholder_valorado = int(input("Introduce el numero del stakeholder a valorar: "))

        valoracion = int(input("Introduce la valoracion del stakeholder: "))

        # Actualizar la valoracion del stakeholder
        stakeholders[stakeholder-1][stakeholder_valorado-1] = valoracion

    elif opcion == 4:
        # Valorar un requisito
        print("¿Que requisito deseas valorar?")
        for i in range(num_requisitos):
            print(f"{i+1}. Requisito {i+1}")
        requisito = int(input("Introduce el numero del requisito: "))

        print("¿Que stakeholder deseas valorar?")
        for i in range(num_stakeholders):
            print(f"{i+1}. Stakeholder {i+1}")
        stakeholder = int(input("Introduce el numero del stakeholder: "))

        valoracion = int(input("Introduce la valoracion del requisito: "))

        # Actualizar la valoracion del requisito

        requisitos[requisito-1][stakeholder-1] = valoracion

    elif opcion == 5:
        # Salir del programa
        print("¡Hasta luego!")
        break

    else:
        print("Opcion invalida. Por favor, intenta de nuevo.")
