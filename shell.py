from productos.models import Producto

# Crear una instancia de Producto
producto = Producto(
    nombre="Desodorante",
    descripcion="Olor chocolate",
    precio=1000,
    stock=10
)
producto.save()

Producto.objects.create(
    nombre="Shampoo de mascota",
    descripcion="Shampoo para perritos y gatitos",
    precio=500,
    stock=5
)

# Obtener uno de los productos
producto1 = Producto.objects.get(nombre="Desodorante")

print("".center(40, "="))
print("Detalles del producto:")
print(f"Nombre: {producto1.nombre}")
print(f"Descripción: {producto1.descripcion}")
print(f"Precio: {producto1.precio}")
print(f"Stock: {producto1.stock}")
print("".center(40, "="))

# Actualizar el precio del producto
producto1.precio = 989
producto1.save()

# Eliminar un producto
producto1.delete()

# salir del shell
# exit()