import random

import self as self


class Requirement:
    def __init__(self, nombre):
        self.nombre = nombre
        self.valores = [1] * num_requisitos
        self.valorFinal = 0
        self.getValorFinal()
        self.peso = 1

    def getValorFinal(self):
        mid = 0
        for val in self.valores:
            mid += val
        self.valorFinal = mid / len(self.valores)


    def __str__(self):
        return f"{self.nombre} - Valor final: {self.valorFinal}"

    def __lt__(self, other):
        return self.valorFinal > other.valorFinal



class StakeHolder:
    def __init__(self, nombre):
        self.nombre = nombre
        self.valores = [1] * num_stakeholders
        self.valorFinal = 0
        self.getValorFinal()

    def getValorFinal(self):
        mid = 0
        for val in self.valores:
            mid += val
        self.valorFinal = mid / len(self.valores)

    def __str__(self):
        return f"{self.nombre} - Valor final: {self.valorFinal}"

    def __lt__(self, other):
        return self.valorFinal > other.valorFinal




# Obtener el numero de stakeholders y requisitos
num_stakeholders = int(input("Introduce el numero de stakeholders: "))
num_requisitos = int(input("Introduce el numero de requisitos: "))

# Crear las listas vacias para stakeholders y requisitos
stakeholders = [StakeHolder("S" + str(i+1)) for i in range(num_stakeholders)]
requisitos = [Requirement("R" + str(i+1)) for i in range(num_requisitos)]
ordenStake = []


# Llenar las listas de stakeholders y requisitos con valores aleatorios
for i in range(num_stakeholders):
    for j in range(num_stakeholders):
        if i == j:
            print("pasa")
            stakeholders[i].valores[j] = 0
            #stakeholders[i].append(None)
        else:
            stakeholders[i].valores[j] = random.randint(1, 10)
            #stakeholders[i].append(random.randint(1, 1))

for i in range(num_requisitos):
    for j in range(num_stakeholders):
        requisitos[i].valores[j] = (random.randint(1, 10))

#En funcion de la importancia del stakeholder aumentara el valor del requisito


def valueStakeHolder():
    #Se calcula el valor de cada stakeholder
    for i in range(num_stakeholders):
        stakeholders[i].getValorFinal()


    #Ordena los stakeholders en funcion de su valor
    ordenStake = sorted(stakeholders)
    for i in range(num_stakeholders):
        #A partir del nombre obtenemos el index del objeto al que pertenece
        index = int(ordenStake[i].nombre[1]) - 1
        valor = stakeholders[index].valorFinal
        for j in range(num_requisitos):
            #Para dar mas importancia a los stakeholders mejores valorados sumamos el valor final
            #Obteniendo mayor valor los requisitos determinados por este
            requisitos[j].valores[int(index)] = valor + requisitos[j].valores[int(index)]

def valueRequeriment():
    #Se calcula el valor de cada stakeholder
    for i in range(num_requisitos):
        requisitos[i].getValorFinal()

    #Ordena los stakeholders en funcion de su valor
    ordenReq = sorted(requisitos)
    for i in range(num_requisitos):
        print(ordenReq[i])
    return ordenReq

# Ciclo principal del programa
while True:
    # Mostrar menu de opciones
    print("¿Que deseas hacer?")
    print("1. Ver la valoracion de los stakeholders")
    print("2. Ver la valoracion de los requisitos")
    print("3. Valorar un stakeholder")
    print("4. Valorar un requisito")
    print("5. Salir")
    print("6. Algoritmo")

    opcion = int(input("Introduce el numero de la opcion que deseas: "))

    if opcion == 1:
        # Mostrar los valores actuales de stakeholders
        print("Valoracion actual de los stakeholders:")
        for i in range(num_stakeholders):
            print(stakeholders[i].valores)
            #print(f"Stakeholder {i+1}: {stakeholders[i].valores[j]}")

    elif opcion == 2:
        # Mostrar los valores actuales de requisitos
        print("Valoracion actual de los requisitos:")
        for i in range(num_requisitos):
            print(f"Requisito {i+1}: {requisitos[i].valores}")

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
        stakeholders[stakeholder-1].valores[stakeholder_valorado-1] = valoracion
        #stakeholders[stakeholder-1][stakeholder_valorado-1] = valoracion

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
        requisitos[requisito-1].valores[stakeholder-1] = valoracion

    elif opcion == 5:
        # Salir del programa
        print("¡Hasta luego!")
        break


    elif opcion == 6:
        #Algoritmo mochila
        total_capacity = int(input("Introduce el peso deseado: "))

        # Obtencion del valoraciones de stakeholder
        valueStakeHolder()
        # Ordenacion de valoraciones de requisitos
        ordenReq = valueRequeriment()

        selected_items = []
        capacity = 0
        for item in ordenReq:
            if capacity + item.peso <= total_capacity:
                selected_items.append(item.nombre)
                capacity += item.peso

        print(selected_items)
        break

    else:
        print("Opcion invalida. Por favor, intenta de nuevo.")


