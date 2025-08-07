def ingreso_repartidor():
    repartidores = {}
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
ingreso_repartidor()
