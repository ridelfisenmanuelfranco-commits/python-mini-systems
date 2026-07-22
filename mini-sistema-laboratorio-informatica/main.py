import os
print('***[ SISTEMA DE GESTION DE LABORATORIO DE INFORMATICA ]***')
# ==============================================================================================
#                               SISTEMA DE GESTION DE LABORATORIO DE INFORMATICA
# ==============================================================================================

# ==============================================================================================
#                                           DATOS 
# ==============================================================================================
computadoras = []
contador = len(computadoras) + 1


# ==============================================================================================
#                               MENU PRINCIPAL DEL SISTEMA
# ==============================================================================================
def mostrar_menu_principal():
    print('''
    ==========================================
       SISTEMA DE LABORATORIO DE INFORMÁTICA
    ==========================================
    [1] Registrar computadora.
    [2] Mostrar computadoras.
    [3] Buscar computadora.
    [4] Enviar a mantenimiento.
    [5] Finalizar mantenimiento.
    [6] Mostrar computadoras disponibles.
    [7] Mostrar computadoras en mantenimiento.
    [8] Eliminar computadora.
    [9] Salir.
    ==========================================
    ''')

# ==============================================================================================
#                               OBTENER CODIGO DE LA COMPUTADORA
# ==============================================================================================
def obtener_codigo():
    global contador
    codigo_pc = f'{contador:03}'
    contador += 1

    return codigo_pc

# ==============================================================================================
#                                   MOSTRAR LABORATORIOS
# ==============================================================================================
def mostrar_laboratorios():
    print('''
    ================================
              LABORATORIOS
    ================================
    [1] LAB-A.
    [2] LAB-B.
    [3] LAB-C.
    [4] LAB-D.
    [5] Salir.
    ================================
    ''')


# ==============================================================================================
#                                       OBTENER LABORATORIO        
# ==============================================================================================
def obtener_laboratorio():
    while True:
        mostrar_laboratorios()

        try: 
            opcion = int(input('Elija un laboratorio: '))
        except ValueError:
            print('\n[ El dato ingresado es invalido. ]\n')
            continue
   
        
        if opcion == 1:
            return 'LAB-A'
        
        elif opcion == 2:
            return 'LAB-B'
        
        elif opcion == 3:
            return 'LAB-C'
        
        elif opcion == 4:
            return 'LAB-D'
        
        elif opcion == 5:
            print('\n[ Saliendo de agregar computadora. ]\n')
            return None


# ==============================================================================================
#                                       OBTENER TEXTO
# ==============================================================================================
def obtener_texto(prompt):
    while True:
        dato = input(prompt).strip().title()

        if dato == 'Salir':
            return None

        if dato == "":
            print('\n[ El dato ingresado es invalido. ]\n')
            continue

        return dato
# ==============================================================================================
#                                 CREAR CODIGO COMPLETO DE LA PC
# ==============================================================================================
def crear_codigo_computadora():
    codigo = obtener_codigo()
    laboratorio = obtener_laboratorio()
    if laboratorio is None:
        return 
    
    codigo_completo = f'{laboratorio}-PC-{codigo}'.upper()

    return codigo_completo

# ==============================================================================================
#                                       CREAR PC      
# ==============================================================================================
def crear_computadora(codigo, procesador, ram, estado):
    return {
        'Codigo': codigo,
        'Procesador': procesador,
        'Ram': ram,
        'Estado': estado
    }


# ==============================================================================================
#                                        REGISTRO DE PC   
# ==============================================================================================
def registrar_computadora():
    existe = False

    codigo = crear_codigo_computadora()
    if codigo is None:
        return
    
    for i, computadora in enumerate(computadoras):
        if computadora['COdigo'] == codigo:
            existe = True
            break

    if existe:
        return
    
    procesador = obtener_texto('Ingrese el procesador de la computadora: ')

    if procesador is None:
        return 
    
    ram = obtener_texto('Ingrese la capacidad de memoria ram de la computadora: ')
    if ram is None:
        return
    
    

    computadora = crear_computadora(codigo, procesador, ram, estado ='Disponible')

    computadoras.append(computadora)
    print('\n[ Computadora creada correctamente. ]\n')


# ==============================================================================================
#                                        MOSTRAR COMPUTADORA
# ==============================================================================================
def mostrar_computadora(i, computadora):
    print(f'''
    ========================================
    Estacion           ||            {i+1}
    ========================================
    Codigo: {computadora['Codigo']}
    Procesador: {computadora['Procesador']}
    Ram: {computadora['Ram']}
    Estado: {computadora['Estado']}
    ========================================
    ''')

# ==============================================================================================
#                                        MOSTRAR COMPUTADORAS
# ==============================================================================================
def mostrar_computadoras():

    if computadoras:
        for i, computadora in enumerate(computadoras):
            mostrar_computadora(i, computadora)

        if len(computadoras) > 1:
            print(f'\n[ Tenemos: {len(computadoras)} computadoras registradas. ]\n')

        else:
            print(f'\n[ Tenemos: {len(computadoras)} computadora registrada. ]\n')

    else:
        print('\n[ No hay "Computadoras" registradas. ]\n')


# ==============================================================================================
#                                      BUSCAR POR CODIGO  
# ==============================================================================================
def buscar_por_codigo(codigo):
    for i, computadora in enumerate(computadoras):
        if computadora['Codigo'] == codigo:
            print("¡Encontrada!")
            return i, computadora

    return None, None

# ==============================================================================================
#                                      BUSCAR COMPUTADORA POR CODIGO 
# ==============================================================================================
def buscar_computadora():
    codigo_computadora_buscada = input('Ingrese el codigo de la computadora buscada: ').strip().upper()
    i, computadora = buscar_por_codigo(codigo_computadora_buscada)

    if computadora:
        mostrar_computadora(i, computadora)

    else:
        print('\n[ Computadora no encontrada. ]\n')


