print('*** SISTEMA DE REGISTRO DE PRODUCTO ***')

# =============================================================================
#                       FUNCIONES DE REGISTRO DE PRODUCTOS
# =============================================================================

# =============================================================================
#                                       DATOS
# =============================================================================
productos = [
    {"Nombre": "Laptop", "Precio": 50000, "Stock": 10},
    {"Nombre": "Mouse", "Precio": 500, "Stock": 3},
    {"Nombre": "Teclado", "Precio": 1200, "Stock": 5},
    {"Nombre": "Monitor", "Precio": 8500, "Stock": 12},
    {"Nombre": "Impresora", "Precio": 7000, "Stock": 2},
    {"Nombre": "Auriculares", "Precio": 1500, "Stock": 8},
    {"Nombre": "Webcam", "Precio": 2200, "Stock": 4},
    {"Nombre": "Disco SSD", "Precio": 3500, "Stock": 15}
]

ventas = [
    {"Nombre": "Laptop", "Precio": 50000, "Cantidad": 2, "Total": 100000},
    {"Nombre": "Mouse", "Precio": 500, "Cantidad": 4, "Total": 2000},
    {"Nombre": "Teclado", "Precio": 1200, "Cantidad": 3, "Total": 3600},
    {"Nombre": "Monitor", "Precio": 8500, "Cantidad": 1, "Total": 8500},
    {"Nombre": "Auriculares", "Precio": 1500, "Cantidad": 2, "Total": 3000}
]


# ===========================================================================================
#                                   MENU
# ===========================================================================================

def mostrar_menu():
    print('''
====================================
        SISTEMA DE INVENTARIO
------------------------------------
    1. Registrar producto
    2. Mostrar productos
    3. Buscar producto
    4. Actualizar stock
    5. Eliminar producto
    6. Registrar venta
    7. Mostrar ventas
    8. Mostrar total vendido
    9. Mostrar stock bajo
    10. Salir
====================================
''')
    
# --------------------------------------------------------------------------------
# ----------------------------- FUNCIONES DE ENTRADA -----------------------------
# --------------------------------------------------------------------------------

# =============================================================================
#                         OBTENER NOMBRE DEL PRODUCTO
# =============================================================================
def obtener_nombre_producto():
    while True:
        nombre_producto = input('Nombre del producto: ').strip().title()

        if nombre_producto == "":
            print('\nNombre del producto invalido.\n')
            continue

        return nombre_producto

# =============================================================================
#                            OBTENER PRECIO DEL PRODUCTO
# =============================================================================
def obtener_precio_producto():
    while True:
        try:
            precio_producto = float(input('Precio del producto: '))
        except ValueError:
            print('\nDato invalido.\n')
            continue

        if precio_producto <= 0:
            print('\nPrecio del producto invalido.\n')
            continue

        return precio_producto

# =============================================================================
#                       OBTENER STOCK DEL PRODUCTO
# =============================================================================
def obtener_stock_producto():
    while True:
        try:
            stock_producto = int(input('Stock del producto: '))
        except ValueError:
            print('\nDato invalido.\n')
            continue

        if stock_producto < 0:
            print('\nStock de producto invalido.\n')
            continue

        return stock_producto

# =============================================================================
#                       OBTENER NOMBRE DEL PRODUCTOA BUSCAR
# =============================================================================
def obtener_nombre_producto_buscar():
    while True:
        nombre_producto = input('Nombre del producto: ').strip().title()

        if nombre_producto == "":
            print('\nNombre del producto invalido.\n')
            continue

        return nombre_producto
    
# =============================================================================
#                           OBTENER NUEVO STOCK
# =============================================================================
def obtener_nuevo_stock():
    while True:
        try:
            nuevo_stock = int(input('Nuevo stock: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        if nuevo_stock < 0:
            print('\nEl nuevo stock es invalido.\n')
            continue

        return nuevo_stock
    

# =============================================================================
#                       CANTIDAD DE PRODUCTOS A VENDER
# =============================================================================
def obtener_cantidad_vendida():
    while True:
        try:
            cantidad_vendida = int(input('Cantidad a vender: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if cantidad_vendida <= 0:
            print('\nLa cantidad ingresada es invalida.\n')
            continue
        
        return cantidad_vendida
    

# --------------------------------------------------------------------------------
# ----------------------------- FUNCIONES DE CREACION ----------------------------
# --------------------------------------------------------------------------------

# =============================================================================
#                       CREAR PRODUCTO
# =============================================================================
def crear_producto(nombre, precio, stock):
    return {
        "Nombre": nombre,
        "Precio": precio,
        "Stock": stock
    }


# =============================================================================
#                               CREAR VENTA
# =============================================================================
def crear_venta(nombre_producto, cantidad_producto, precio_producto, total_venta):
    return {
        "Nombre": nombre_producto,
        "Precio": precio_producto,
        "Cantidad": cantidad_producto,
        "Total": total_venta
    }




# --------------------------------------------------------------------------------
# ------------------------------- FUNCIONES DE CRUD ------------------------------
# --------------------------------------------------------------------------------
# =============================================================================
#                           REGISTRAR PRODUCTO
# =============================================================================
def registrar_producto():
    existe = False
    nombre = obtener_nombre_producto()

    for producto in productos:
        if producto['Nombre'] == nombre:
            existe = True
            break

    if existe:
        print(f'\nEl producto: {nombre} ya existe.\n')
        return

    precio = obtener_precio_producto()
    stock = obtener_stock_producto()

    producto = crear_producto(
    nombre,
    precio,
    stock
    )

    productos.append(producto)
    print('\nProducto registrado correctamente.\n')


# =============================================================================
#                           MOSTRAR PRODUCTO
# ========================= ====================================================
def mostrar_productos():
    if productos:
        for producto in productos:
            print(f'''
                ======================================   
                            PRODUCTO
                ======================================   
                Nombre: {producto['Nombre']}
                Precio:  ${producto['Precio']:.2f}
                Stock:    {producto['Stock']}
                ======================================   
            ''')
    else:
        print('\nNo hay productos.\n')

# =============================================================================
#                           BUSCAR PRODUCTO
# =============================================================================
def buscar_producto():
    encontrado = False
    nombre_producto = obtener_nombre_producto_buscar()

    for producto in productos:
        if producto['Nombre'] == nombre_producto:
            encontrado = True
            print(f'''
            ======================================   
                        PRODUCTO
            ======================================   
            Nombre: {producto['Nombre']}
            Precio:  ${producto['Precio']:.2f}
            Stock:    {producto['Stock']}
            ======================================   
        ''')
            break

    if not encontrado:
        print('\nProducto no encontrado.\n')


# =============================================================================
#                           ACTUALIZAR STOCK
# =============================================================================
def actualizar_stock():
    encontrado = False
    nombre_producto = obtener_nombre_producto_buscar()
    for producto in productos:
        if nombre_producto == producto['Nombre']:
            encontrado = True
            nuevo_stock = obtener_nuevo_stock()
            print(f'''
            ======================================   
                        PRODUCTO
            ======================================   
            Nombre: {producto['Nombre']}
            Precio:  ${producto['Precio']:.2f}
            Stock:    {producto['Stock']}
            ======================================   
            \n''')
            producto['Stock'] = nuevo_stock

            print('\nEl stock se ha actualizado correctamente.\n')
            print(f'''
            ======================================   
                        PRODUCTO
            ======================================   
            Nombre: {producto['Nombre']}
            Precio:  ${producto['Precio']:.2f}
            Stock:    {producto['Stock']}
            ======================================   
            \n''')
            break

    if not encontrado:
        print('\nProducto no encontrado.\n')

# =============================================================================
#                          ELIMINAR PRODUCTO
# =============================================================================
def eliminar_producto():
    encontrado = False
    nombre_producto = obtener_nombre_producto_buscar()
    for producto in productos:
        if producto['Nombre'] == nombre_producto:
            encontrado = True
            print(f'''
            ======================================   
                        PRODUCTO
            ======================================   
            Nombre: {producto['Nombre']}
            Precio:  ${producto['Precio']:.2f}
            Stock:    {producto['Stock']}
            ======================================   
            \n''')

            productos.remove(producto)
            print('\nEl producto ha sido eliminado correctamente.\n')
            break

    if not encontrado:
        print('\nProducto no encontrado.\n')


# --------------------------------------------------------------------------------
# ------------------------------ FUNCIONES DE VENTAS -----------------------------
# --------------------------------------------------------------------------------
# =============================================================================
#                             REGISTRAR VENTA
# =============================================================================
def registrar_venta():
    existe = False
    nombre_producto = obtener_nombre_producto_buscar()

    for producto in productos:
        if producto['Nombre'] == nombre_producto:
            existe = True
            nombre = producto['Nombre']
            precio = producto['Precio']
            stock = producto['Stock']

            if stock == 0:
                print('\nNo hay suficiente stock.\n')
                return
            
            break

    if not existe:
        print('\nEl producto no existe.\n')       
        return
    
    cantidad_vendida = obtener_cantidad_vendida()
    if cantidad_vendida > stock:
        print('\nLa cantidad a compar es mayor al stock disponible.\n')
        return
    
    total_venta = precio * cantidad_vendida
    
    venta = crear_venta(
        nombre,
        cantidad_vendida,
        precio,
        total_venta
    )
    ventas.append(venta)

    producto['Stock'] -= cantidad_vendida
    print('\nVenta registrada correctamente.\n')

# =============================================================================
#                             MOSTRAR VENTAS
# =============================================================================
def mostrar_ventas():
    if ventas:
        for venta in ventas:
            print(f'''
            ======================================
                        VENTA
            ======================================
            Nombre: {venta['Nombre']}
            Precio: ${venta['Precio']:.2f}
            Cantidad: {venta['Cantidad']}
            Total: ${venta['Total']:.2f}
            ======================================
            ''')    
    else:
        print('\nNo hay ventas registradas.\n')

# =============================================================================
#                           MOSTRAR TOTAL VENDIDO
# =============================================================================
def mostrar_total_vendido():
    if ventas:
        total_vendido = 0
        for i, venta in enumerate(ventas):
            total_vendido += venta['Total']

        print(f'Total vendido: ${total_vendido:.2f}')

    else:
        print('\nNo hay ventas registradas.\n')


# =============================================================================
#                           MOSTRAR STOCK BAJO
# =============================================================================
def mostrar_stock_bajo():
    if productos:
        encontrado = False
        for producto in productos:
            if producto['Stock'] <= 5:
                encontrado = True
                print(f'''
            ======================================   
                        PRODUCTO
            ======================================   
            Nombre: {producto['Nombre']}
            Precio:  ${producto['Precio']:.2f}
            Stock:    {producto['Stock']}
            ======================================   
            \n''')
                
        if not encontrado:
            print('\nproducto no encontrado.\n')

    else:
        print('\nNo hay productos.\n')


# --------------------------------------------------------------------------------
# -------------------------------- BUCLE PRINCIPAL -------------------------------
# --------------------------------------------------------------------------------
while True:

    mostrar_menu()

    try:
        opcion = int(input('Elija una opcion: '))

    except ValueError:
        print('\ndato invalido.\n')
        continue

    if opcion == 1:
        registrar_producto()

    elif opcion == 2:
        mostrar_productos()

    elif opcion == 3:
       buscar_producto()

    elif opcion == 4:
        actualizar_stock()

    elif opcion == 5:
        eliminar_producto()

    elif opcion == 6:
        registrar_venta()

    elif opcion == 7:
        mostrar_ventas()

    elif opcion == 8:
        mostrar_total_vendido()

    elif opcion == 9:
        mostrar_stock_bajo()


    elif opcion == 10:
        print('\nsaliendo del sistema.....\n')
        break

    else:
        print('\nopcion invalida.\n')

