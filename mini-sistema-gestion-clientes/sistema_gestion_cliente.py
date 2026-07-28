print('*** SISTEMA DE GESTION DE CLIENTES. ***')
# ======================================================================================
#                           SISTEMA DE GESTION DE CLIENTES
# ======================================================================================

# ======================================================================================
#                                   DATOS
# ======================================================================================
clientes = [
    {
        "Nombre": "Juan Perez",
        "Telefono": 8097898899,
        "Correo": "juan@gmail.com",
        "Direccion": "Pekin, Santo Domingo",
        "Ciudad": "Santo Domingo"
    },
    {
        "Nombre": "Maria Rodriguez",
        "Telefono": 8294561234,
        "Correo": "maria@hotmail.com",
        "Direccion": "Villa Olga",
        "Ciudad": "Santiago"
    },
    {
        "Nombre": "Pedro Santos",
        "Telefono": 8493216547,
        "Correo": "pedro@yahoo.com",
        "Direccion": "Las Colinas",
        "Ciudad": "Santiago"
    },
    {
        "Nombre": "Ana Garcia",
        "Telefono": 8096549871,
        "Correo": "ana@gmail.com",
        "Direccion": "Los Jardines",
        "Ciudad": "La Vega"
    },
    {
        "Nombre": "Luis Martinez",
        "Telefono": 8297412589,
        "Correo": "luis@hotmail.com",
        "Direccion": "Centro Ciudad",
        "Ciudad": "Puerto Plata"
    },
    {
        "Nombre": "Carla Gomez",
        "Telefono": 8498529637,
        "Correo": "carla@gmail.com",
        "Direccion": "Villa Mella",
        "Ciudad": "Santo Domingo"
    },
    {
        "Nombre": "Jose Ramirez",
        "Telefono": 8099638527,
        "Correo": "jose@yahoo.com",
        "Direccion": "Bella Vista",
        "Ciudad": "Santiago"
    },
    {
        "Nombre": "Laura Fernandez",
        "Telefono": 8293571598,
        "Correo": "laura@gmail.com",
        "Direccion": "Los Alamos",
        "Ciudad": "Moca"
    }
]

# ======================================================================================
#                                       MENU
# ======================================================================================
def mostrar_menu():
    print('''
    ====================================
       SISTEMA DE GESTION DE CLIENTES
    ------------------------------------
    1. Registrar cliente
    2. Mostrar clientes
    3. Buscar cliente
    4. Actualizar cliente
    5. Eliminar cliente
    6. Salir
    ====================================
    ''')

# ======================================================================================
#                             OBTENER NOMBRE DEL CLIENTE         
# ======================================================================================
def obtener_nombre_cliente():
    while True:
        nombre_cliente = input('Nombre del cliente: ').strip().title()

        if nombre_cliente == "":
            print('\nNombre del cliente invalido.\n')
            continue

        return nombre_cliente
    
# ======================================================================================
#                           OBTENER APELLIDO DEL CLIENTE           
# ======================================================================================
def obtener_apellido_cliente():
    while True:
        apellido_cliente = input('Apellido cliente: ').strip().title()

        if apellido_cliente == "":
            print('\nEl apellido del cliente es invalido.\n')
            continue

        return apellido_cliente
    
# ======================================================================================
#                            OBTENER TELEFONO DEL CLIENTE           
# ======================================================================================
def obtener_telefono_cliente():
    while True:
        try:
            telefono_cliente = int(input('telefono del cliente: '))

            if len(str(telefono_cliente)) != 10:
                print('\nTelefono dle cliente invalido.\n')
                continue
            
            if str(telefono_cliente)[:3] not in ['809', '829', '849']:
                print('\nNumero de telefono invalido.\n')
                continue

        except ValueError:
            print('\nDato invalido.\n')
            continue

        return telefono_cliente

# ======================================================================================
#                           OBTENER CORREO DEL CLIENTE                   
# ======================================================================================
def obtener_correo_cliente():
    while True:
        correo_cliente = input('Correo del cliente: ').strip().lower()

        if correo_cliente == "":
            print('\nCorreo del cliente invalido.\n')
            continue

        if '@' not in correo_cliente or '.' not in correo_cliente:
            print('\nCorreo electorinico no valido.\n')
            continue

        return correo_cliente

# ======================================================================================
#                               OBTENER DIRECCION DEL CLIENTE                   
# ======================================================================================
def obtener_direccion_cliente():
    while True:
        direccion_cliente = input('Direccion del cliente: ').strip().title()

        if direccion_cliente == "":
            print('\nDireccion del cliente invalida.\n')
            continue

        return direccion_cliente
    

# ======================================================================================
#                           OBTENER CIUDAD DEL CLIENTE                  
# ======================================================================================
def obtener_ciudad_cliente():
    while True:
        ciudad_cliente = input('Ciudad del cliente: ').strip().title()

        if ciudad_cliente == "":
            print('\nCiudad del cliente invalida.\n')
            continue

        return ciudad_cliente


# ======================================================================================
#                           OBTENER NOMBRE COMPLETO DEL CLIENTE                
# ======================================================================================
# el proposito de esta funcion es simplificar un poco el uso 
# de nombre completo en algunas partes del codigo.
def obtener_nombre_completo_cliente():
    nombre_cliente = obtener_nombre_cliente()
    apellido_cliente = obtener_apellido_cliente()
    return f'{nombre_cliente} {apellido_cliente}'

# ======================================================================================
#                                   CREAR CLIENTE                  
# ======================================================================================
def crear_cliente(nombre, apellido, telefono, correo, direccion, ciudad):
    nombre_completo = f'{nombre} {apellido}'
    return {
        "Nombre": nombre_completo,
        "Telefono": telefono,
        "Correo": correo,
        "Direccion": direccion,
        "Ciudad": ciudad
    }


# ======================================================================================
#                                   REGISTRAR CLIENTE                  
# ======================================================================================
def registrar_cliente():
    existe = False
    nombre = obtener_nombre_cliente()
    apellido = obtener_apellido_cliente()
    nombre_completo = f'{nombre} {apellido}'

    for cliente in clientes:
        if cliente['Nombre'] == nombre_completo:
            existe = True
            break
    if existe:
        print('\nEl cliente ya existe.\n')
        return
    
    telefono = obtener_telefono_cliente()
    correo = obtener_correo_cliente()
    direccion = obtener_direccion_cliente()
    ciudad = obtener_ciudad_cliente()

    cliente = crear_cliente(
        nombre,
        apellido,
        telefono,
        correo,
        direccion,
        ciudad
    )

    clientes.append(cliente)
    print('\nCliente agregado correctamente.\n')

# ======================================================================================
#                                   MOSTRAR CLIENTE                  
# ======================================================================================
def mostrar_clientes():
    if clientes:
        for i, cliente in enumerate(clientes):
            print(f'''
            ========================================
                        CLIENTE
            ========================================
            ID: {i + 1}
            Nombre     : {cliente['Nombre']}
            Telefono   : {cliente['Telefono']}
            Correo     : {cliente['Correo']}
            Direccion  : {cliente['Direccion']}
            Ciudad     : {cliente['Ciudad']}
            ========================================
            ''')
        print(f'\nTotal de clientes: {len(clientes)}\n')
    else:
        print('\nNo hay clientes registrados.\n')

# ======================================================================================
#                                   BUSCAR CLIENTE                  
# ======================================================================================
def buscar_cliente():
    if clientes:
        existe = False
        nombre_cliente_completo = obtener_nombre_completo_cliente()

        for i, cliente in enumerate(clientes):
            if cliente['Nombre'] == nombre_cliente_completo:
                existe = True
                print(f'''
                ========================================
                            CLIENTE
                ========================================
                ID: {i + 1}
                Nombre     : {cliente['Nombre']}
                Telefono   : {cliente['Telefono']}
                Correo     : {cliente['Correo']}
                Direccion  : {cliente['Direccion']}
                Ciudad     : {cliente['Ciudad']}
                ========================================
                ''')
                break

        if not existe:
            print('\nCliente no encontrado.\n')
            
    else:
        print('\nNo hay clientes registrados.\n')


# ======================================================================================
#                                   ACTUALIZAR CLIENTE                  
# ======================================================================================
def actualizar_cliente():
    if clientes:
        existe = False
        nombre_cliente = obtener_nombre_completo_cliente()

        for i, cliente in enumerate(clientes):
            if cliente['Nombre'] == nombre_cliente:
                existe = True
                print(f'''
                ========================================
                            CLIENTE
                ========================================
                ID: {i + 1}
                Nombre     : {cliente['Nombre']}
                Telefono   : {cliente['Telefono']}
                Correo     : {cliente['Correo']}
                Direccion  : {cliente['Direccion']}
                Ciudad     : {cliente['Ciudad']}
                ========================================
                ''')

                cliente['Telefono'] = obtener_telefono_cliente()
                cliente['Correo'] = obtener_correo_cliente()
                cliente['Direccion'] = obtener_direccion_cliente()
                cliente['Ciudad'] = obtener_ciudad_cliente()

                print('\nCliente actualizado correctamente.\n')
                break

        if not existe:
            print('\nCliente no existe.\n')     
    else:
        print('\nNo hay clientes registrados.\n')

# ======================================================================================
#                                    ELIMINAR CLIENTE                 
# ======================================================================================
def eliminar_cliente():
    if clientes:
        existe = False
        nombre_cliente = obtener_nombre_completo_cliente()

        for i, cliente in enumerate(clientes):
            if cliente['Nombre'] == nombre_cliente:
                existe = True
                print(f'''
                ========================================
                            CLIENTE
                ========================================
                ID: {i + 1}
                Nombre     : {cliente['Nombre']}
                Telefono   : {cliente['Telefono']}
                Correo     : {cliente['Correo']}
                Direccion  : {cliente['Direccion']}
                Ciudad     : {cliente['Ciudad']}
                ========================================
                ''')

                clientes.remove(cliente)
                print('\nCliente eliminado correctamente.\n')
                break

        if not existe:
            print('\nCliente no existe.\n')
    else:
        print('\nNo hay clientes registrados.\n')


# ======================================================================================
#                                    BUCLE PRINCIPAL                 
# ======================================================================================

while True:
    mostrar_menu()

    try:
        opcion = int(input('Elije una opcion: '))
    
    except ValueError:
        print('\nDato invalido.\n')
        continue

    if opcion == 1:
        registrar_cliente()

    elif opcion == 2:
        mostrar_clientes()

    elif opcion == 3:
        buscar_cliente()

    elif opcion == 4:
        actualizar_cliente()

    elif opcion == 5:
        eliminar_cliente()

    elif opcion == 6:
        print('\nSaliendo del sistema.\n')
        break
    else:
        print('\nOpcion invalida.\n')

        


