def quick_sort_repartidor(lista,clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x[1][clave] >= pivote[1][clave]]
        menores = [x for x in lista[1:] if x[1][clave] < pivote[1][clave]]
        return quick_sort_repartidor(mayores,clave) + [pivote] + quick_sort_repartidor(menores,clave)


def ingreso_repartidor(repartidores):
    while True:
        try:
            cantidad = int(input("¿Cuántos repartidores desea ingresar?: "))
            if cantidad <= 0:
                print("Debe ingresar al menos 1 repartidor.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número válido.")

    for i in range(cantidad):
        print(f"\n--- Ingreso de Repartidor #{i + 1} ---")

        while True:
            codigo = input("Ingrese código del repartidor: ").strip()
            if not codigo:
                print("El código no puede estar vacío.")
            elif codigo in repartidores:
                print("Este código ya existe. Intente con otro.")
            else:
                break

        while True:
            nombre = input("Ingrese el nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
            else:
                break

        while True:
            try:
                paquetes = int(input("Ingrese la cantidad de paquetes entregados: "))
                if paquetes < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        # Validar zona
        while True:
            zona = input("Ingrese la zona asignada: ").strip()
            if not zona:
                print("La zona no puede estar vacía.")
            else:
                break

        # Guardar los datos
        repartidores[codigo] = {
            "nombre": nombre,
            "paquetes_entregados": paquetes,
            "zona": zona
        }


def ranking(repartidores):
    if not repartidores:
        print("Lista vacia...")
        return

    lista_repartidores = list(repartidores.items())
    lista_ordenada = quick_sort_repartidor(lista_repartidores,'paquetes_entregados')
    print("\n RANKING DE REPARTIDORES POR PAQUETES ENTREGADOS (Mayor a menor):")

    for pos, (codigo, datos) in enumerate(lista_ordenada, start=1):
        print(f"{pos}. Nombre: {datos['nombre']}, "
              f"Paquetes: {datos['paquetes_entregados']}, Zona: {datos['zona']}")


def buscar_repartidor(repartidores):
    if not repartidores:
        print("No hay repartidores ingresados")
        return

    codigo_buscar = input("Ingrese el código del repartidor a buscar: ").strip()

    if codigo_buscar in repartidores:
        datos = repartidores[codigo_buscar]
        print(f"\nRepartidor encontrado:")
        print(f"Código: {codigo_buscar}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Paquetes entregados: {datos['paquetes_entregados']}")
        print(f"Zona: {datos['zona']}")
    else:
        print("No se encontró ningún repartidor con ese código.")


def menu():
    repartidores = {}
    while True:
        print("****Menu****")
        print("1. Ingreso de repartidores")
        print("2. Mostrar ranking de mayor a menor")
        print("3. Buscar Repartidor")
        print("4.Salir")

        opcion = input("Ingrese una opcion: ").strip()

        match opcion:
            case "1":
                ingreso_repartidor(repartidores)
            case "2":
                ranking(repartidores)
            case "3":
                buscar_repartidor(repartidores)
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion Invalida...")

menu()