# Tarea práctica: Colecciones de datos
# Tema: Registro de productos de una tienda
# Estructura utilizada: diccionario

productos = {}

def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()

    if codigo in productos:
        print("Ese código ya se encuentra registrado.")
        return

    nombre = input("Ingrese el nombre del producto: ").strip()

    try:
        precio = float(input("Ingrese el precio del producto: $"))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        print("Error: el precio y la cantidad deben ser valores numéricos.")
        return

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Producto agregado correctamente.")


def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if not productos:
        print("No hay productos registrados.")
        return

    for codigo, datos in productos.items():
        print(
            f"Código: {codigo} | "
            f"Producto: {datos['nombre']} | "
            f"Precio: ${datos['precio']:.2f} | "
            f"Cantidad: {datos['cantidad']}"
        )


def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto que desea buscar: ").strip()

    if codigo in productos:
        datos = productos[codigo]
        print("Producto encontrado:")
        print(f"Nombre: {datos['nombre']}")
        print(f"Precio: ${datos['precio']:.2f}")
        print(f"Cantidad: {datos['cantidad']}")
    else:
        print("El producto no está registrado.")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto que desea eliminar: ").strip()

    if codigo in productos:
        eliminado = productos.pop(codigo)
        print(f"Producto '{eliminado['nombre']}' eliminado correctamente.")
    else:
        print("El producto no está registrado.")


def menu():
    while True:
        print("\n==============================")
        print("   REGISTRO DE PRODUCTOS")
        print("==============================")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Programa finalizado. Gracias.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
