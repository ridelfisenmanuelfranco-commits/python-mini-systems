# ========================================================================================
#                           SISTEMA DE GESTION DE PEDIDOS                                   
# ========================================================================================

# ========================================================================================
#                                           DATOS
# ========================================================================================
pedidos = [
    {
        "Cliente": "Juan Perez",
        "Producto": "Laptop",
        "Cantidad": 2,
        "Estado": "Pendiente"
    },
    {
        "Cliente": "Maria Rodriguez",
        "Producto": "Mouse",
        "Cantidad": 3,
        "Estado": "Entregado"
    },
    {
        "Cliente": "Pedro Santos",
        "Producto": "Teclado",
        "Cantidad": 1,
        "Estado": "En Proceso"
    },
    {
        "Cliente": "Ana Garcia",
        "Producto": "Monitor",
        "Cantidad": 2,
        "Estado": "Pendiente"
    },
    {
        "Cliente": "Luis Martinez",
        "Producto": "Impresora",
        "Cantidad": 1,
        "Estado": "Cancelado"
    },
    {
        "Cliente": "Carla Gomez",
        "Producto": "Disco SSD",
        "Cantidad": 4,
        "Estado": "Entregado"
    },
    {
        "Cliente": "Jose Ramirez",
        "Producto": "Memoria RAM",
        "Cantidad": 2,
        "Estado": "Pendiente"
    },
    {
        "Cliente": "Laura Fernandez",
        "Producto": "Tablet",
        "Cantidad": 1,
        "Estado": "En Proceso"
    }
]

# ========================================================================================
#                                     MENU DEL SISTEMA
# ========================================================================================
def mostrar_menu():
    print('''
    ====================================
        GESTION DE PEDIDOS
        ------------------------------------
        1. Registrar pedido
        2. Mostrar pedidos
        3. Buscar pedido
        4. Actualizar estado
        5. Eliminar pedido
        6. Mostrar pedidos pendientes
        7. Salir
        ====================================
    ''')


# ========================================================================================
#                                 OBTENER NOMBRE DEL CLIENTE
# ========================================================================================
def obtener_nombre_cliente():
    while True:
        nombre_cliente = input('Nombre del cliente: ').strip().title()

        if nombre_cliente == 'Salir':
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
#                               OBTENER CANTIDAD DEL PRODUCTO
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
#                                 OBTENER ESTADO DEL PEDIDO
# ========================================================================================
def obtener_estado_pedido():
    while True:
        estado_pedido = input('Estado del pedido: ').strip().title()

        if estado_pedido == "":
            print('\nEstado del pedido invalido.\n')
            continue

        if estado_pedido not in ['Pendiente', 'En Proceso', 'Entregado', 'Cancelado']:
            print('\nEstado de pedido invalido.\n')
            continue

        return estado_pedido
    
# ========================================================================================
#                                      CREAR PEDIDO        
# ========================================================================================
def crear_pedido(cliente, producto, cantidad, estado):
    return {
        'Cliente': cliente,
        'Producto': producto,
        'Cantidad': cantidad,
        'Estado': estado
    }


# ========================================================================================
#                                       AGREGAR PEDIDO
# ========================================================================================
def agregar_pedido(pedido):
    pedidos.append(pedido)


# ========================================================================================
#                                   REGISTRAR PEDIDO
# ========================================================================================
def registrar_pedido():
    nombre_cliente = obtener_nombre_cliente()
    if nombre_cliente is None:
        return
    
    nombre_producto = obtener_nombre_producto()
    cantidad_producto = obtener_cantidad_producto()
    estado_pedido = obtener_estado_pedido()

    pedido = crear_pedido(nombre_cliente,
                          nombre_producto,
                          cantidad_producto,
                          estado_pedido)
    agregar_pedido(pedido)
    print('\nPedido agregado correctamente.\n')


# ========================================================================================
#                                       MOSTRAR PEDIDOS
# ========================================================================================
def mostrar_pedidos():
    if pedidos:
        for i, pedido in enumerate(pedidos):
            print(f'''
            ========================================
                        PEDIDO
            ========================================
            ID        : {i + 1}
            Cliente   : {pedido['Cliente']}
            Producto  : {pedido['Producto']}
            Cantidad  : {pedido['Cantidad']}
            Estado    : {pedido['Estado']}
            ========================================
            ''')
            
        print(f'\nTotal de pedidos: {len(pedidos)}\n')

    else:
        print('\nNo hay pedidos registrados.\n')

# ========================================================================================
#                                       BUSCAR PEDIDO
# ========================================================================================
def buscar_pedido():
    if pedidos:
        encontrado = False
        nombre_pedido_buscado = obtener_nombre_cliente()

        for i, pedido in enumerate(pedidos):
            if pedido['Cliente'] == nombre_pedido_buscado:
                encontrado = True
                print('\nPedido encontrado.\n')
                print(f'''
                ========================================
                            PEDIDO
                ========================================
                ID        : {i + 1}
                Cliente   : {pedido['Cliente']}
                Producto  : {pedido['Producto']}
                Cantidad  : {pedido['Cantidad']}
                Estado    : {pedido['Estado']}
                ========================================
                ''')
                break
        
        if not encontrado:
            print('\nEl pedido no fue encontrado.\n')

    else:
        print('\nNo hay pedidos registrados.\n')

# ========================================================================================
#                                   ACTUALIZAR ESTADO
# ========================================================================================
def actualizar_estado():
    if pedidos:
        encontrado = False
        nombre_pedido_buscado = obtener_nombre_cliente()

        for i, pedido in enumerate(pedidos):
            if pedido['Cliente'] == nombre_pedido_buscado:
                encontrado = True
                print('\nPedido encontrado.\n')
                print(f'''
                ========================================
                            PEDIDO
                ========================================
                ID        : {i + 1}
                Cliente   : {pedido['Cliente']}
                Producto  : {pedido['Producto']}
                Cantidad  : {pedido['Cantidad']}
                Estado    : {pedido['Estado']}
                ========================================
                ''')

                pedido['Estado'] = obtener_estado_pedido()
                print('\nPedido actualizado correctamente.\n')
                break
        
        if not encontrado:
            print('\nPedido no encontrado.\n')
    
    else:
        print('\nNo hay pedidos registrados.\n')


# ========================================================================================
#                                   ELIMINAR PEDIDO
# ========================================================================================
def eliminar_pedido():
    if pedidos:
        encontrado = False
        nombre_pedido_buscado = obtener_nombre_cliente()

        for i, pedido in enumerate(pedidos):
            if pedido['Cliente'] == nombre_pedido_buscado:
                encontrado = True
                print('\nPedido encontrado.\n')
                print(f'''
                ========================================
                            PEDIDO
                ========================================
                ID        : {i + 1}
                Cliente   : {pedido['Cliente']}
                Producto  : {pedido['Producto']}
                Cantidad  : {pedido['Cantidad']}
                Estado    : {pedido['Estado']}
                ========================================
                ''')
                
                pedidos.remove(pedido)
                print('\nPedido eliminado correctamente.\n')
                break
        if not encontrado:
            print('\nPedido no encontrado.\n')
    else:
        print('\nNo hay pedidos registrados.\n')


# ========================================================================================
#                                   PEDIDOS PENDIENTES
# ========================================================================================
def mostrar_pedidos_pendientes():
    if pedidos:
        hay_pendientes = False
        cantidad_pendiete = 0
        for i, pedido in enumerate(pedidos):
            if pedido['Estado'] == 'Pendiente':
                hay_pendientes = True
                print(f'''
                ========================================
                            PEDIDO
                ========================================
                ID        : {i + 1}
                Cliente   : {pedido['Cliente']}
                Producto  : {pedido['Producto']}
                Cantidad  : {pedido['Cantidad']}
                Estado    : {pedido['Estado']}
                ========================================
                ''')
                cantidad_pendiete += 1

        print(f'\nTotal de pedidos pendientes: {cantidad_pendiete}\n')

        if not hay_pendientes:
            print('\nNo tenemos pedidos pendientes.\n')
    else:
        print('\nNo hay pedidos registrados.\n')

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
        registrar_pedido()

    elif opcion == 2:
        mostrar_pedidos()

    elif opcion == 3:
        buscar_pedido()

    elif opcion == 4:
        actualizar_estado()

    elif opcion == 5:
        eliminar_pedido()

    elif opcion == 6:
        mostrar_pedidos_pendientes()

    elif opcion == 7:
        print('\nSaliendo del sistema.\n')
        break

    else:
        print('\nOpcion invalida.\n')