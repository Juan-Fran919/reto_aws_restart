import json
import time
stop_while = True
archivo_json = "articulos.json"

def producto_existe(nombre, productos):
    return any(producto['nombre'] == nombre for producto in productos)

def leer_regresar_datos():
    # Leer el archivo JSON existente
    try:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        datos = {"articulos": []}
        return datos

def buscar_producto(nombre):
    datos = leer_regresar_datos()
    for producto in datos['articulos']:
        if producto['nombre'] == nombre:
            return producto
    return None

def imprimir_informe():
    datos = leer_regresar_datos()
    articulos = datos['articulos']

    if not articulos:
        print("No hay artículos en el inventario.")
        return

    print("Informe de Artículos:")
    for articulo in articulos:
        print(f"Nombre: {articulo['nombre']}, Precio: {articulo['precio']}, Cantidad: {articulo['cantidad']}, Descripción: {articulo['descripcion']}")
    print("Informe generado con éxito")

def actualizar_producto(nombre, articulo_actualizado):
    datos = leer_regresar_datos()
    for i, producto in enumerate(datos['articulos']):
        if producto['nombre'] == nombre:
            datos['articulos'][i] = articulo_actualizado
            with open(archivo_json, 'w') as file:
                json.dump(datos, file, indent=4)
            return

def eliminar_producto(nombre):
    datos = leer_regresar_datos()
    articulos = datos['articulos']

    for i, producto in enumerate(articulos):
        if producto['nombre'] == nombre:
            del articulos[i]
            with open(archivo_json, 'w') as file:
                json.dump(datos, file, indent=4)
            return

def agregar_producto(articulo_nuevo):
    datos = leer_regresar_datos()

    # Verificar si el producto ya existe
    if producto_existe(articulo_nuevo['nombre'], datos['articulos']):
        print("Error: El producto ya existe.")
        return

    # Agregar el nuevo producto
    datos['articulos'].append(articulo_nuevo)

    # Escribir de nuevo al archivo JSON
    with open(archivo_json, 'w') as file:
        json.dump(datos, file, indent=4)
    
    print("Producto guardado con éxito")

def es_flotante(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

while stop_while:
    print("Bienvenido al Sistema de Gestión de Inventario")
    print("Seleccione una opción:")
    print("""1. Ingresar un nuevo producto
          2. Actualizar un producto
          3. Eliminar un producto
          4. Buscar un producto
          5. Generar informe de inventario
          6. Salir del sistema
          """)
    opcion = input("Ingrese una opción: ")
    opcion = opcion.strip()
    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Opción inválida solo escribe el número de la opción que deseas")
        opcion = input("Ingrese una opción: ")

    #Opcion 1 Agregar un nuevo producto
    if opcion == "1":
        print("Ingresar un nuevo producto")
        print("Ingrese los datos del producto")
        nombre = input("Nombre: ")
        nombre = nombre.upper()
        precio = input("Precio: ")
        while not es_flotante(precio):
            print("El precio debe ser un número flotante")
            precio = input("Precio: ")
        precio = float(precio)
        cantidad = input("Cantidad: ")
        while cantidad.isnumeric() == False:
            print("La cantidad debe ser un número entero")
            cantidad = input("Cantidad: ")
        cantidad = int(cantidad)
        descripcion = input("Descripción: ")
        articulo_nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "descripcion": descripcion}
        agregar_producto(articulo_nuevo)
        time.sleep(3)
        print("\n")

    #Opcion 2 Actualizar un producto
    elif opcion == "2":
        print("Actualizar un producto")
        print("Ingrese el nombre del producto a actualizar")
        nombre_busqueda = input("Nombre: ")
        nombre_busqueda = nombre_busqueda.upper()
        producto = buscar_producto(nombre_busqueda)

        if producto:
            print(f"Datos actuales del producto: {producto}")
            
            #Actualice los datos del producto:
            nombre = input("Nombre: ")
            nombre = nombre.upper()
            precio = input("Precio: ")
            while not es_flotante(precio):
                print("El precio debe ser un número flotante")
                precio = input("Precio: ")
            precio = float(precio)
            cantidad = input("Cantidad: ")
            while cantidad.isnumeric() == False:
                print("La cantidad debe ser un número entero")
                cantidad = input("Cantidad: ")
            cantidad = int(cantidad)
            descripcion = input("Descripción: ")
            articulo_actualizado = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "descripcion": descripcion}
            actualizar_producto(nombre_busqueda, articulo_actualizado)
            print("Producto actualizado con éxito")
        else:
            print("No se encontró el producto")
        time.sleep(3)
        print("\n")
    
    #Opcion 3 Eliminar un producto
    elif opcion == "3":
        print("Eliminar un producto")
        print("Ingrese el nombre del producto a eliminar")
        nombre_busqueda = input("Nombre: ")
        nombre_busqueda = nombre_busqueda.upper()
        producto = buscar_producto(nombre_busqueda)

        if producto:
            print(f"Datos actuales del producto: {producto}")
            print("¿Está seguro que desea eliminar el producto? (S/N)")
            opcion = input("Opción: ")
            opcion = opcion.upper()
            while opcion not in ["S", "N"]:
                print("Opción inválida")
                opcion = input("Opción: ")
                opcion = opcion.upper()
            if opcion == "S":
                eliminar_producto(nombre_busqueda)
                print("Producto eliminado con éxito")
            else:
                print("No se eliminó el producto")
        else:
            print("No se encontró el producto")
        time.sleep(3)
        print("\n")
    
    #Opcion 4 Buscar un producto
    elif opcion == "4":
        print("Buscar un producto")
        print("Ingrese el nombre del producto a buscar")
        nombre_busqueda = input("Nombre: ")
        nombre_busqueda = nombre_busqueda.upper()
        producto = buscar_producto(nombre_busqueda)

        if producto:
            print("Producto encontrado")
            print(f"Datos actuales del producto: {producto}")
        else:
            print("No se encontró el producto")
        time.sleep(3)
        print("\n")
    
    #Opcion 5 Generar informe de inventario
    elif opcion == "5":
        print("Generando informe de inventario")
        imprimir_informe()
        time.sleep(3)
        print("\n")
    
    #Opcion 6 Salir del sistema
    elif opcion == "6":
        print("Gracias por utilizar el sistema")
        stop_while = False
        time.sleep(3)
        print("\n")

    else:
        print("Opción inválida")
        time.sleep(3)
        print("\n")