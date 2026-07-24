# ===========================================================================================
#                                 SISTEMA DE BIBLIOTECA
# ===========================================================================================

# ===========================================================================================
#                                             DATOS
# ===========================================================================================
libros = [
    {
        'titulo': 'Don Quijote De La Mancha',
        'autor': 'Miguel De Cervantes',
        'categoria': 'Novela',
        'estado': 'Disponible'
    },
    {
        'titulo': 'Cien Anios De Soledad',
        'autor': 'Gabriel Garcia Marquez',
        'categoria': 'Realismo Magico',
        'estado': 'Disponible'
    },
    {
        'titulo': 'Habitos Atomicos',
        'autor': 'James Clear',
        'categoria': 'Desarrollo Personal',
        'estado': 'Disponible'
    }
]


# ===========================================================================================
#                                          MENU
# ===========================================================================================

def mostrar_menu():
    print('''
====================================
        SISTEMA DE BIBLIOTECA
------------------------------------
    1. Agregar libro
    2. Mostrar libros
    3. Buscar libro
    4. Prestar libro
    5. Devolver libro
    6. Mostrar libros prestados
    7. Mostrar libros Disponibles
    8. Eliminar libro
    9. Salir
====================================
''')

    
# ===========================================================================================
#                                OBTENER TITULO DEL LIBRO
# ===========================================================================================
def obtener_titulo_libro():
    while True:
        titulo_libro = input('titulo del libro: ').strip().title()

        if titulo_libro == 'Salir':
            return None
        
        if titulo_libro == "":
            print('\ntitulo del libro invalido.\n')
            continue

        return titulo_libro

# ===========================================================================================
#                                OBTENER AUTOR DEL LIBRO
# ===========================================================================================
def obtener_autor_libro():
    while True:
        autor_libro = input('autor del libro: ').strip().title()

        if autor_libro == "":
            print('\nautor del libro incorrecto.\n')
            continue

        return autor_libro
    
# ===========================================================================================
#                                OBTENER CATEGORIA DEL LIBRO
# ===========================================================================================
def obtener_categoria_libro():
    while True:
        categoria_libro = input('categoria del libro: ').strip().title()

        if categoria_libro == "":
            print('\ncategoria del libro incorrecta.\n')
            continue

        return categoria_libro


# ===========================================================================================
#                                      AGREGAR LIBRO
# ===========================================================================================
def agregar_libro(libros):
    titulo_libro = obtener_titulo_libro()
    existe = False
    if titulo_libro is None:
        return
    
    for libro in libros:
        if libro['titulo'] == titulo_libro:
            existe = True
            break

    if existe:
        print(f'\nel libro {titulo_libro} ya existe.\n')
        return
    
    autor_libro = obtener_autor_libro()
    categoria_libro = obtener_categoria_libro()


    libro = {
        'titulo': titulo_libro,
        'autor': autor_libro,
        'categoria': categoria_libro,
        'estado': 'Disponible'
    }

    libros.append(libro)

    print('\nel libro se agrego correctamente.\n')
    
# ===========================================================================================
#                                       MOSTRAR LIBRO
# ===========================================================================================
def mostrar_libro(i, libro):
    print(f"""
            ====================================
            ID #{i + 1}
            ====================================
            Titulo: {libro['titulo']}
            Autor: {libro['autor']}
            Categoria: {libro['categoria']}
            Estado: {libro['estado']}
            ====================================
            """)
# ===========================================================================================
#                                       MOSTRAR LIBROS
# ===========================================================================================

def mostrar_libros(libros):

    if libros:

        for i, libro in enumerate(libros):
            mostrar_libro(i, libro)
            
    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                           BUSCAR LIBRO
# ===========================================================================================

def buscar_libro(libros):

    if libros:

        while True:

            existe = False
            titulo_libro_buscar = obtener_titulo_libro()
            if titulo_libro_buscar is None:
                return 

            
            for i, libro in enumerate(libros):

                if libro['titulo'] == titulo_libro_buscar or libro['autor'] == titulo_libro_buscar:

                    existe = True
                    mostrar_libro(i, libro)

                    break

            if not existe:
                print(f'\nel libro {titulo_libro_buscar} no existe.\n')
                continue

            break

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                           PRESTAR LIBRO
# ===========================================================================================

def prestar_libro(libros):

    if libros:

        while True:

            existe = False

            titulo_libro_prestar = obtener_titulo_libro()
            if titulo_libro_prestar is None:
                return 

            for libro in libros:

                if libro['titulo'] == titulo_libro_prestar or libro['autor'] == titulo_libro_prestar:
                
                    existe = True

                    if libro['estado'] == 'Disponible':

                        libro['estado'] = 'Prestado'

                        print(
                            '\nel libro ha sido prestado exitosamente.\n'
                        )

                        break

                    print('\nel libro ya esta prestado.\n')
                    break

            if not existe:

                print(f'\nel libro {titulo_libro_prestar} no fue encontrado.\n')

                continue

            break

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                           DEVOLVER LIBRO
# ===========================================================================================

def devolver_libro(libros):

    if libros:

        while True:

            existe = False

            titulo_libro_devolver = obtener_titulo_libro()
            if titulo_libro_devolver is None:
                return

            for libro in libros:

                if libro['titulo'] == titulo_libro_devolver or libro['autor'] == titulo_libro_devolver:
                    existe = True

                    if libro['estado'] == 'Prestado':

                        libro['estado'] = 'Disponible'

                        print(
                            '\nel libro ha sido devuelto correctamente.\n'
                        )

                        break

                    print(
                        f'\nel libro "{titulo_libro_devolver}" ya esta Disponible.\n'
                    )

                    break

            if not existe:

                print(
                    f'\nel libro "{titulo_libro_devolver}" no existe.\n'
                )

                continue

            break

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                       MOSTRAR LIBROS PRESTADOS
# ===========================================================================================

def mostrar_libros_prestados(libros):

    if libros:

        hay_prestados = False

        for i, libro in enumerate(libros):

            if libro['estado'] == 'Prestado':

                hay_prestados = True

                mostrar_libro(i, libro)

        if not hay_prestados:
            print('\nno hay libros prestados.\n')

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                   MOSTRAR LIBROS DisponibleS
# ===========================================================================================

def mostrar_libros_Disponibles(libros):

    if libros:

        hay_Disponibles = False

        for i, libro in enumerate(libros):

            if libro['estado'] == 'Disponible':

                hay_Disponibles = True

                mostrar_libro(i, libro)

        if not hay_Disponibles:
            print('\nno hay libros Disponibles.\n')

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                           ELIMINAR LIBRO
# ===========================================================================================

def eliminar_libro(libros):

    if libros:

        while True:

            existe = False

            titulo_libro_eliminar = obtener_titulo_libro()
            if titulo_libro_eliminar is None:
                return

            for libro in libros:

                if libro['titulo'] == titulo_libro_eliminar or libro['autor'] == titulo_libro_eliminar:

                    existe = True

                    libros.remove(libro)

                    print(
                        '\nel libro ha sido eliminado correctamente.\n'
                    )

                    break

            if not existe:

                print(
                    f'\nel libro "{titulo_libro_eliminar}" no existe.\n'
                )

                continue

            break

    else:
        print('\nno hay libros Disponibles.\n')


# ===========================================================================================
#                                       PROGRAMA PRINCIPAL
# ===========================================================================================

while True:

    mostrar_menu()

    try:
        opcion = int(input('Elija una opcion: '))

    except ValueError:
        print('\ndato invalido.\n')
        continue

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        mostrar_libros(libros)

    elif opcion == 3:
        buscar_libro(libros)

    elif opcion == 4:
        prestar_libro(libros)

    elif opcion == 5:
        devolver_libro(libros)

    elif opcion == 6:
        mostrar_libros_prestados(libros)

    elif opcion == 7:
        mostrar_libros_Disponibles(libros)

    elif opcion == 8:
        eliminar_libro(libros)

    elif opcion == 9:
        print('\nsaliendo del sistema.....\n')
        break

    else:
        print('\nopcion invalida.\n')