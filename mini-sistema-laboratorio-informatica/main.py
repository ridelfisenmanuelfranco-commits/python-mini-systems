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

