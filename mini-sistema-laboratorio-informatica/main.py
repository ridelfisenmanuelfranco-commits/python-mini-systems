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
    [1] A
    [2] B
    [3] C
    [4] D
    [5] E
    [6] F
    [7] Salir.
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

        match(opcion):
            case 1:
                return 'A'
            case 2:
                return 'B'
            case 3:
                return 'C'
            case 4:
                return 'D'
            case 5: 
                return 'E'
            case 6:
                return 'F'
            case 7:
                break

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
#                                       CREAR PC      
# ==============================================================================================
def crear_pc(codigo, procesador, ram, estado):
    return {
        'Codigo': codigo,
        'Procesador': procesador,
        'Ram': ram,
        'Estado': estado
    }


