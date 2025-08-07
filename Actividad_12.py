def ingreso_repartidor():

    repartidores={}
    cantidad=int(input("Cuanto repartidores desea ingresar: "))

    for i in range(cantidad):
        nombre=input("Ingrese el nombre: ")
        if nombre in repartidores:
            print("Este repartidor ya fue ingresado")
        else:
            break
        paquetes=int(input("Ingrese la cantidad de paquetes entregados: "))
        zona=input("Ingrese la zona asignada: ")

        repartidores[nombre]={
        "paquetes_entregados":paquetes,
        "Zona":zona
         }



