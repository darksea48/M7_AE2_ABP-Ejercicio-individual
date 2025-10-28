from decimal import Decimal
from tracemalloc import start
from turtle import mode
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

#### RETO 24-10 ####
from productos.models import *
import time
from django.db import connection
from django.db.models import F

# 2.- Agrega al menos 5 productos más para poder trabajar mejor y que las consultas sean más claras e interactivas
Producto.objects.create(
    nombre="Jabón Líquido",
    descripcion="Jabón para manos con aroma a lavanda",
    precio=50.00,
    stock=30
)
Producto.objects.create(
    nombre="Crema Hidratante",
    descripcion="Crema para piel seca",
    precio=75.00,
    stock=20
)
Producto.objects.create(
    nombre="Aceite de Argan",
    descripcion="Aceite de argan puro para el cabello",
    precio=120.00,
    stock=15
)
Producto.objects.create(
    nombre="Acondicionador",
    descripcion="Acondicionador para cabello seco",
    precio=80.00,
    stock=25
)
Producto.objects.create(
    nombre="Alcohol en Gel",
    descripcion="Alcohol en gel antibacterial",
    precio=50.00,
    stock=100
)

# 3.- Recupera todos los registros de la tabla Producto.
productos = Producto.objects.all()
for p in productos:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}, Disponible: {p.disponible}")

# 4.- Con filtros, obtén todos los productos con precio mayor a 50
productos_mayor_50 = Producto.objects.filter(precio__gt=50)
print("Productos con precio mayor a 50:")
for p in productos_mayor_50:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}")

# 5.- Con filtros, obtén todos los productos cuyo nombre empiecen con la letra A
productos_A = Producto.objects.filter(nombre__istartswith='a')
for p in productos_A:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}, Disponible: {p.disponible}")

# 6.- Utilizando raw, obtén todos los productos con precio menor a 100
productos_bajo_100 = Producto.objects.raw('SELECT * FROM productos_producto WHERE precio < %s', [100])
for p in productos_bajo_100:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, stock: {p.stock}")

# 7.- Utilizando raw, obtén todos los productos con bajo stock (menos de 10 productos en stock)
productos_bajo_stock = Producto.objects.raw('SELECT * FROM productos_producto WHERE stock < %s', [10])
for p in productos_bajo_stock:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, stock: {p.stock}")

# 8.- Crea un índice en el campo nombre del modelo Producto.
# Ya se encuentra creado un índice en el campo nombre en el modelo Producto (unique=True).

# 9.- Utilizando time.time(), Verifica el impacto en la eficiencia de búsqueda.
time_start = time.time()
productos = Producto.objects.all()
for p in productos:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}, Disponible: {p.disponible}")
time_end = time.time()
print(f"Tiempo de ejecución con índice: {time_end - time_start} segundos")

# 10.- Obtén todos los productos y excluye el campo de disponible
lista_productos = Producto.objects.all().defer('disponible')
for p in lista_productos:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}")

# 11.- Usa annotate() para calcular un campo adicional llamado precio_con_impuesto, donde el impuesto sea del 16%.
producto_con_impuesto = Producto.objects.annotate(precio_con_impuesto=('precio') * (Decimal('1.16')))
for p in producto_con_impuesto:
    print(f"Nombre: {p.nombre}, Precio: {p.precio}, Precio con Impuesto: {p.precio_con_impuesto}")

# 12.- Usando connection.cursor() agrégale al precio de todos los productos 5 pesos.
with connection.cursor() as cursor:
    cursor.execute('UPDATE productos_producto SET precio = precio + %s', [5])
