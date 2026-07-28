print('*** SISTEMA DE GESTION DE FACTURAS ***')
# ========================================================================================
#                                SISTEMA DE GESTION DE FACTURAS
# ========================================================================================

# ========================================================================================
#                                           DATOS 
# ========================================================================================
facturas = [
    {
        "Cliente": "Juan Perez",
        "Producto": "Laptop",
        "Cantidad": 2,
        "Precio": 500.00,
        "Subtotal": 1000.00,
        "ITBIS": 180.00,
        "Total": 1180.00
    },
    {
        "Cliente": "Maria Rodriguez",
        "Producto": "Mouse",
        "Cantidad": 3,
        "Precio": 25.00,
        "Subtotal": 75.00,
        "ITBIS": 13.50,
        "Total": 88.50
    },
    {
        "Cliente": "Pedro Santos",
        "Producto": "Teclado",
        "Cantidad": 2,
        "Precio": 40.00,
        "Subtotal": 80.00,
        "ITBIS": 14.40,
        "Total": 94.40
    },
    {
        "Cliente": "Ana Garcia",
        "Producto": "Monitor",
        "Cantidad": 1,
        "Precio": 250.00,
        "Subtotal": 250.00,
        "ITBIS": 45.00,
        "Total": 295.00
    },
    {
        "Cliente": "Luis Martinez",
        "Producto": "Impresora",
        "Cantidad": 1,
        "Precio": 180.00,
        "Subtotal": 180.00,
        "ITBIS": 32.40,
        "Total": 212.40
    },
    {
        "Cliente": "Carla Gomez",
        "Producto": "Disco SSD",
        "Cantidad": 4,
        "Precio": 60.00,
        "Subtotal": 240.00,
        "ITBIS": 43.20,
        "Total": 283.20
    },
    {
        "Cliente": "Jose Ramirez",
        "Producto": "Memoria RAM",
        "Cantidad": 2,
        "Precio": 75.00,
        "Subtotal": 150.00,
        "ITBIS": 27.00,
        "Total": 177.00
    },
    {
        "Cliente": "Laura Fernandez",
        "Producto": "Tablet",
        "Cantidad": 1,
        "Precio": 350.00,
        "Subtotal": 350.00,
        "ITBIS": 63.00,
        "Total": 413.00
    }
]

# ========================================================================================
#                                     MENU DEL SISTEMA
# ========================================================================================
def mostrar_menu():
    print('''
    ====================================
        GESTION DE FACTURAS
    ------------------------------------
    1. Crear factura
    2. Mostrar facturas
    3. Buscar factura
    4. Eliminar factura
    5. Mostrar total facturado
    6. Salir
    ====================================
    ''')

# ========================================================================================
#                               OBTENER NOMBRE DEL CLIENTE   
# ========================================================================================
def obtener_nombre_cliente():
    while True:
        nombre_cliente = input('Nombre del cliente: ').strip().title()

        if nombre_cliente == "Salir":
            return None
        
        if nombre_cliente == "":
            print('\nNombre del cliente invalido.\n')
            continue

        return nombre_cliente


# ========================================================================================
#                              OBTENER NOMBRE DEL PRODUCTO   
# ========================================================================================
def obtener_nombre_producto():
    while True:
        nombre_producto = input('Nombre del producto: ').strip().title()

        if nombre_producto == "":
            print('\nNombre del producto invalido.\n')
            continue

        return nombre_producto
    

# ========================================================================================
#                                 OBTENER CANTIDAD DEL PRODUCTO
# ========================================================================================
def obtener_cantidad_producto():
    while True:
        try:
            cantidad_producto = int(input('Cantidad del producto: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        if cantidad_producto <= 0:
            print('\nCantidad de producto invalida.\n')
            continue

        return cantidad_producto
    
# ========================================================================================
#                                 OBTENER PRECIO DEL PRODUCTO
# ========================================================================================
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
    





# ========================================================================================
#                                       CREAR FACTURA
# ========================================================================================
def crear_factura(cliente, producto, cantidad, precio, subtotal, itbis, total):
    return {
        "Cliente": cliente,
        "Producto": producto,
        "Cantidad": cantidad,
        "Precio": precio,
        "Subtotal": subtotal,
        "ITBIS": itbis,
        "Total": total
    }


# ========================================================================================
#                                 AGREGAR FACTURA
# ========================================================================================
def agregar_factura(factura):
    facturas.append(factura)


# ========================================================================================
#                                   REGISTRAR FACTURA
# ========================================================================================
def registrar_factura():
    nombre_cliente = obtener_nombre_cliente()

    if nombre_cliente is None:
        return
    
    nombre_producto = obtener_nombre_producto()
    cantidad_producto = obtener_cantidad_producto()
    precio_producto = obtener_precio_producto()
    subtotal_factura = cantidad_producto * precio_producto
    impuestos = subtotal_factura * 0.18
    total_final = subtotal_factura + impuestos

    factura = crear_factura(
        nombre_cliente,
        nombre_producto,
        cantidad_producto,
        precio_producto,
        subtotal_factura,
        impuestos,
        total_final
        )
    agregar_factura(factura)
    print('\nFactura agregada correctamente.\n')



# ========================================================================================
#                                   MOSTRAR FACTURA
# ========================================================================================
def mostrar_facturas():
    if facturas:
        total_facturado = 0

        for i, factura in enumerate(facturas):
            print(f'''
            ========================================
                        FACTURA
            ========================================
            ID        : {i + 1}
            Cliente   : {factura['Cliente']}
            Producto  : {factura['Producto']}
            Cantidad  : {factura['Cantidad']}
            Precio    : ${factura['Precio']:.2f}
            Subtotal  : ${factura['Subtotal']:.2f}
            ITBIS     : ${factura['ITBIS']:.2f}
            Total     : ${factura['Total']:.2f}
            ========================================
            ''')
            total_facturado += factura['Total']
        
        print(f'''\n
        ========================================
                TOTAL FACTURADO
        ========================================
        Total: ${total_facturado:.2f}
        ========================================
        \n''')
    else:
        print('\nNo hay facturas registradas.\n')



# ========================================================================================
#                                   BUSCAR FACTURA
# ========================================================================================
def buscar_factura():
    if facturas:
        encontrado = False
        nombre_cliente_buscado = obtener_nombre_cliente()

        for i, factura in enumerate(facturas):
            if factura['Cliente'] == nombre_cliente_buscado:
                encontrado = True
                print('\nFactura encontrada.\n')
                print(f'''
                ========================================
                            FACTURA
                ========================================
                ID        : {i + 1}
                Cliente   : {factura['Cliente']}
                Producto  : {factura['Producto']}
                Cantidad  : {factura['Cantidad']}
                Precio    : ${factura['Precio']:.2f}
                Subtotal  : ${factura['Subtotal']:.2f}
                ITBIS     : ${factura['ITBIS']:.2f}
                Total     : ${factura['Total']:.2f}
                ========================================
                ''')
                break
        if not encontrado:
            print('\nFactura no encontrada.\n')

    else:
        print('\nNo hay facturas registradas.\n')

# ========================================================================================
#                                   ELIMINAR FACTURA
# ========================================================================================
def eliminar_factura():
    if facturas:
        encontrado = False
        nombre_cliente_buscado = obtener_nombre_cliente()

        for i, factura in enumerate(facturas):
            if factura['Cliente'] == nombre_cliente_buscado:
                encontrado = True
                print('\nFactura encontrada.\n')
                print(f'''
                ========================================
                            FACTURA
                ========================================
                ID        : {i + 1}
                Cliente   : {factura['Cliente']}
                Producto  : {factura['Producto']}
                Cantidad  : {factura['Cantidad']}
                Precio    : ${factura['Precio']:.2f}
                Subtotal  : ${factura['Subtotal']:.2f}
                ITBIS     : ${factura['ITBIS']:.2f}
                Total     : ${factura['Total']:.2f}
                ========================================
                ''')
                facturas.remove(factura)
                print('\nFactura eliminada correctamente.\n')
                break
        
        if not encontrado:
            print('\nFactura no encontrada.\n')
    
    else:
        print('\nNo hay facturas registradas.\n')


# ========================================================================================
#                                   TOTAL FACTURADO
# ========================================================================================
def mostrar_total_facturado():
    if facturas:
        total_facturado = 0

        for factura in facturas:
            total_facturado += factura['Total']
        
        print(f'''
        ========================================
          TOTAL FACTURADO
        ========================================
        Total: ${total_facturado:.2f}
        ========================================
        ''')
    else:
        print('\nNo hay facturas registradas.\n')


# ========================================================================================
#                                   SISTEMA PRINCIPAL
# ========================================================================================
while True:
    mostrar_menu()

    try:
        opcion = int(input('Elije una opcion: '))
    
    except ValueError:
        print('\nDato invalido.\n')
        continue

    if opcion == 1:
        registrar_factura()

    elif opcion == 2:
        mostrar_facturas()

    elif opcion == 3:
        buscar_factura()

    elif opcion == 4:
        eliminar_factura()

    elif opcion == 5:
        mostrar_total_facturado()

    elif opcion == 6:
        print('\nSaliendo del sistema.\n')
        break
    
    else:
        print('\nOpcion invalida.\n')
