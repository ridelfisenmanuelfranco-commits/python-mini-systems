# ==========================================================================================
#                      SISTEMA DE GESTION DE COMPRA A PROVEEDOR
# ==========================================================================================

# ========================================================================================
#                                           DATO    
# ========================================================================================
compras = [

    {
        "Proveedor": "Tecnologia Global",
        "Producto": "Laptop",
        "Cantidad": 10,
        "Costo": 25000,
        "Total": 250000
    },
    {
        "Proveedor": "Distribuidora Nacional",
        "Producto": "Mouse",
        "Cantidad": 50,
        "Costo": 350,
        "Total": 17500
    },
    {
        "Proveedor": "Comercial Perez",
        "Producto": "Monitor",
        "Cantidad": 8,
        "Costo": 8500,
        "Total": 68000
    },
    {
        "Proveedor": "Inversiones Rodriguez",
        "Producto": "Teclado",
        "Cantidad": 25,
        "Costo": 1200,
        "Total": 30000
    },
    {
        "Proveedor": "Suplidores Del Cibao",
        "Producto": "Disco SSD",
        "Cantidad": 15,
        "Costo": 3200,
        "Total": 48000
    }
]


# ========================================================================================
#                                           MENU
# ========================================================================================
def mostrar_menu():
    print('''
    ====================================
          GESTION DE COMPRAS
    ------------------------------------
    1. Registrar compra
    2. Mostrar compras
    3. Buscar compra
    4. Eliminar compra
    5. Salir
    ====================================
    ''')


# ========================================================================================
#                                   OBTENER NOMBRE DEL PROVEEDOR
# ========================================================================================
def obtener_nombre_proveedor():
    while True:
        nombre_proveedor = input('Nombre del proveedor: ').strip().title()

        if nombre_proveedor == 'Salir':
            return None
        
        if nombre_proveedor == "":
            print('\nNombre del proveedor invalido.\n')
            continue

        return nombre_proveedor
    
# ========================================================================================
#                                OBTENER NOMBRE DE PRODUCTO     
# ========================================================================================
def obtener_nombre_producto():
    while True:
        nombre_producto = input('Nombre del producto: ').strip().title()

        if nombre_producto == "":
            print('\nNombre del producto invalido.\n')
            continue

        return nombre_producto
    


# ========================================================================================
#                                  OBTENER CANTIDAD DE PRODUCTO
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
#                              OBTENER COSTO POR PRODUCTOS         
# ========================================================================================
def obtener_costo_producto():
    while True:
        try:
            costo_producto = float(input('Costo por unidad de producto: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if costo_producto <= 0:
            print('\nCosto de producto invalido.\n')
            continue

        return costo_producto
    


# ========================================================================================
#                                       CREAR COMPRA           
# ========================================================================================
def crear_compra(proveedor, producto, cantidad, costo, total):
    return {
        'Proveedor': proveedor,
        'Producto': producto,
        'Cantidad': cantidad,
        'Costo': costo,
        'Total': total
    }

# ========================================================================================
#                                    REGISTRAR COMPRA
# ========================================================================================
def registrar_compra():
    existe = False
    nombre_proveedor = obtener_nombre_proveedor()

    if nombre_proveedor is None:
        return
    
    nombre_producto = obtener_nombre_producto()
    for compra in compras:
        if (
            compra['Proveedor'] == nombre_proveedor and
            compra['Producto'] == nombre_producto
        ):
            existe = True
            break

    if existe:
        print('\nLa compra ya existe.\n')
        return
    
    cantidad_producto = obtener_cantidad_producto()
    costo_producto = obtener_costo_producto()
    total_compra = cantidad_producto * costo_producto

    compra = crear_compra(nombre_proveedor,
                          nombre_producto,
                          cantidad_producto,
                          costo_producto,
                          total_compra)
    
    compras.append(compra)
    print('\nCompra agregada correctamente.\n')


# ========================================================================================
#                                       MOSTRAR COMPRAS  
# ========================================================================================
def mostrar_compras():
    if compras:

        total_comprado = 0
        print(f'\nTotal de compras: {len(compras)}\n')
        for i, compra in enumerate(compras):
            print(f'''
            ========================================
                        COMPRA
            ========================================
            ID         : {i + 1}
            Proveedor  : {compra['Proveedor']}
            Producto   : {compra['Producto']}
            Cantidad   : {compra['Cantidad']}
            Costo      : ${compra['Costo']:.2f}
            Total      : ${compra['Total']:.2f}
            ========================================
            ''')

            total_comprado += compra['Total']
        
        print(f'''
        ========================================
                    TOTAL COMPRADO
        ========================================
        Total: ${total_comprado:.2f}
        ========================================
        ''')

    else:
        print('\nNo hay compras registradas.\n')


# ========================================================================================
#                                       BUSCAR COMPRA
# ========================================================================================
def buscar_compra():
    if compras:
        encontrada = False
        nombre_compra_buscada = obtener_nombre_proveedor()
        nombre_producto_buscado = obtener_nombre_producto()
        
        for i, compra in enumerate(compras):
            if compra['Proveedor'] == nombre_compra_buscada and compra['Producto'] == nombre_producto_buscado:
                encontrada = True
                print('\nCompra encontrada.\n')
                print(f'''
                ========================================
                            COMPRA
                ========================================
                ID         : {i + 1}
                Proveedor  : {compra['Proveedor']}
                Producto   : {compra['Producto']}
                Cantidad   : {compra['Cantidad']}
                Costo      : ${compra['Costo']:.2f}
                Total      : ${compra['Total']:.2f}
                ========================================
                ''')
                break

        if not encontrada:
            print('\nCompra no encontrada.\n')
    
    else:
        print('\nNo hay compras registradas.\n')

# ========================================================================================
#                                    ELIMINAR COMPRA   
# ========================================================================================
def eliminar_compra():
    if compras:
        encontrada = False
        nombre_compra_buscada = obtener_nombre_proveedor()
        nombre_producto_buscado = obtener_nombre_producto()

        for i, compra in enumerate(compras):
            if compra['Proveedor'] == nombre_compra_buscada and compra['Producto'] == nombre_producto_buscado:
                encontrada = True
                print('\nCompra encontrada.\n')
                print(f'''
                ========================================
                            COMPRA
                ========================================
                ID         : {i + 1}
                Proveedor  : {compra['Proveedor']}
                Producto   : {compra['Producto']}
                Cantidad   : {compra['Cantidad']}
                Costo      : ${compra['Costo']:.2f}
                Total      : ${compra['Total']:.2f}
                ========================================
                ''')

                compras.remove(compra)
                print('\nCompra eliminada correctamente.\n')
                break
        if not encontrada:
            print('\nCompra no encontrada.\n')
    else:
        print('\nNo hay compras registradas.\n')

# ========================================================================================
#                                      SISTEMA PRINCIPAL
# ========================================================================================
while True:
    
    mostrar_menu()

    try:
        opcion = int(input('Elije una opcion: '))

    except ValueError:
        print('\nDato invalido.\n')
        continue

    if opcion == 1:
        registrar_compra()

    elif opcion == 2:
        mostrar_compras()

    elif opcion == 3:
        buscar_compra()

    elif opcion == 4:
        eliminar_compra()

    elif opcion == 5:
        print('\nSaliendo del sistema.\n')
        break
    else:
        print('\nOpcion invalida.\n')