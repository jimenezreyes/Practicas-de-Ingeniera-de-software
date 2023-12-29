import mysql.connector


"""
Alumno: Jimenez reyes abraham 
"""

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="conector"
)

# Crear un cursor para ejecutar las consultas
cursor = conexion.cursor()


#Define una clase que represente una tabla en tu base de datos:

# Sentencia SQL para crear la primera tabla

tabla_cliente = """
CREATE TABLE IF NOT EXISTS Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    domicilio VARCHAR(200),
    ciudad VARCHAR(200),
    estado VARCHAR(200),
    codigopostal INT,
    email VARCHAR(200)
)
"""

# Sentencia SQL para crear la segunda tabla
tabla_pedido = """
CREATE TABLE IF NOT EXISTS PEDIDOS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombrepedido VARCHAR (255),
    vendedor VARCHAR(255),
    fechadepedido DATE,
    producto VARCHAR(255),
    cantidad INT,
    precio DECIMAL(10, 2),
    total DECIMAL(10, 2)
)
"""

# Sentencia SQL para crear la tercera tabla

tabla_proveedor = """
CREATE TABLE IF NOT EXISTS PROVEEDORES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empresa VARCHAR (255),
    nombredelcontacto VARCHAR (255),
    direccion VARCHAR (255),
    ciudad VARCHAR(255),
    estado VARCHAR(255),
    codigopostal INT,
    email VARCHAR(255)
)
"""

tabla_producto = """
CREATE TABLE IF NOT EXISTS PRODUCTO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR (255),
    precio INT,
    marca VARCHAR (255),
    existencia INT
)
"""

# Ejecutar las sentencias SQL para crear las tablas
cursor.execute(tabla_cliente)
cursor.execute(tabla_pedido)
cursor.execute(tabla_proveedor)
cursor.execute(tabla_producto)


# Confirmar los cambios en la base de datos
conexion.commit()


# Definir la función para cargar los datos en las tablas
def datos():
    # Tabla cliente
    insert_cliente = """
    INSERT INTO Clientes (nombre, domicilio, ciudad, estado, codigopostal, email)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    datos_clientes = [
    ("Juan Pérez", "Calle 123, Colonia A", "Mexico", "Estado A", 12345, "juan@email.com"),
    ("María Rodríguez", "Avenida 456, Colonia B", "España", "Durango", 54321, "maria@email.com"),
    ("Carlos López", "Calle 789, Colonia C", "Inglaterra", "Estado C", 98765, "carlos@email.com"),
    ("Ana García", "Calle 101, Colonia D", "London", "Estado D", 10101, "ana@email.com"),
    ("Luis Martínez", "Avenida 202, Colonia E", "Brasil", "Estado E", 20202, "luis@email.com"),
    ("Laura González", "Calle 303, Colonia F", "CDMX", "Estado F", 30303, "laura@email.com"),
    ("Pedro Sánchez", "Avenida 404, Colonia G", "CDMX", "Durango", 40404, "pedro@email.com"),
    ("Sofía Torres", "Calle 505, Colonia H", "H", "Estado H", 50505, "sofia@email.com"),
    ("Miguel Ruiz", "Avenida 606, Colonia I", "I", "Estado I", 60606, "miguel@email.com"),
    ("Carmen Vargas", "Calle 707, Colonia J", "J", "Estado J", 70707, "carmen@email.com"),
    ("Fernando Ríos", "Avenida 808, Colonia K", "K", "Estado K", 80808, "fernando@email.com"),
    ("Isabel Morales", "Calle 909, Colonia L", "L", "Estado L", 90909, "isabel@email.com"),
    ("Roberto Paredes", "Avenida 010, Colonia M", "M", "Durango", 10101, "roberto@email.com"),
    ("Gabriela Silva", "Calle 111, Colonia N", "N", "Estado N", 11111, "gabriela@email.com"),
    ("Javier Castro", "Avenida 121, Colonia O", "O", "Durango", 12121, "javier@email.com"),
    ]
    # Insertar los datos de clientes en la tabla
    for datos_cliente in datos_clientes:
        cursor.execute(insert_cliente, datos_cliente)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    #Tabla pedido
    insert_pedido= """
    INSERT INTO PEDIDOS (nombrepedido,vendedor,fechadepedido,producto,cantidad,precio,total)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    datos_pedidos = [
    ("Luces led", "Octavio", "2023-04-12", "Luz roja", 3, 10, 30),
    ("Televisor 4K", "Ana", "2023-04-15", "TV Samsung", 1, 500, 500),
    ("Portátil", "Carlos", "2023-04-18", "Laptop HP", 2, 800, 1600),
    ("Teléfono móvil", "Laura", "2023-04-20", "iPhone 13", 1, 1000, 1000),
    ("Aire acondicionado", "Roberto", "2023-04-22", "AC LG", 1, 600, 600),
    ("Sofá", "Isabel", "2023-04-25", "Sofá de cuero", 1, 700, 700),
    ("Mesa de comedor", "Miguel", "2023-04-28", "Mesa de madera", 1, 300, 300),
    ("Lavadora", "Carmen", "2023-05-02", "Lavadora Samsung", 1, 400, 400),
    ("Refrigerador", "Javier", "2023-05-05", "Refrigerador LG", 1, 600, 600),
    ("Bicicleta", "Sofía", "2023-05-08", "Bicicleta de montaña", 2, 250, 500),
    ("Micrófono", "Fernando", "2023-05-10", "Micrófono Shure", 10, 150, 1500),
    ("Impresora", "María", "2023-05-15", "Impresora HP", 10, 120, 1200),
    ("Monitor", "Pedro", "2023-05-18", "Monitor Dell", 2, 180, 360),
    ("Muebles de jardín", "Gabriela", "2023-05-22", "Juego de muebles", 10, 350, 3500),
    ("Horno de microondas", "Luis", "2023-05-25", "Microondas Panasonic", 10, 80, 800),
    ]
    # Insertar los datos de clientes en la tabla
    for datos_pedidos in datos_pedidos:
        cursor.execute(insert_pedido, datos_pedidos)

    # Confirmar los cambios en la base de datos
    conexion.commit()  

    #Tabla proveedor
    insert_proveedor = """
    INSERT INTO PROVEEDORES (empresa,nombredelcontacto,direccion,ciudad,estado,codigopostal,email)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    datos_proveedor = [
    ("ALPLA", "Pedro", "Lomas calle 3", "CDMX", "Mexico", 53719, "pedrojf@hotmail.com"),
    ("FabricaTech", "Ana", "Avenida Principal 45", "Guadalajara", "Mexico", 44000, "ana@gmail.com"),
    ("Suministros Industriales", "Carlos", "Calle Industrial 12", "Monterrey", "Mexico", 64000, "carlos@suministros.com"),
    ("Materiales Constructivos", "Luisa", "Avenida Construcción 78", "Puebla", "Mexico", 72000, "luisa@materiales.com"),
    ("TechSolutions", "María", "Calle Innovación 9", "Tijuana", "Mexico", 22000, "maria@techsolutions.com"),
    ("Proveedora de Componentes", "Javier", "Avenida Componentes 22", "Hermosillo", "Mexico", 83000, "javier@proveedora.com"),
    ("Productos Electrónicos", "Sofía", "Calle Electrónica 33", "Querétaro", "Mexico", 76000, "sofia@gmail.com"),
    ("Distribuidora de Acero", "Miguel", "Avenida Acero 15", "Aguascalientes", "Mexico", 20000, "miguel@distribuidora.com"),
    ("Papel y Suministros", "Carmen", "Calle Papel 7", "Cancún", "Mexico", 77500, "carmen@papelysuministros.com"),
    ("Industrias Plásticas", "Fernando", "Calle Plástico 26", "Mérida", "Mexico", 97000, "fernando@plasticas.com"),
    ("Productos Químicos", "Isabel", "Avenida Químicos 18", "Cuernavaca", "Mexico", 62000, "isabel@gmail.com"),
    ("Logística y Transporte", "Roberto", "Avenida Logística 13", "Veracruz", "Mexico", 91700, "roberto@logistica.com"),
    ("Suministros de Oficina", "Gabriela", "Calle Oficina 54", "Oaxaca", "Mexico", 68000, "gabriela@gmail.com"),
    ("Maquinaria Pesada", "Lorenzo", "Avenida Maquinaria 31", "Chihuahua", "Mexico", 31000, "lorenzo@maquinaria.com"),
    ("Construcciones S.A.", "Natalia", "Calle Construcción 62", "Durango", "Mexico", 34000, "natalia@gmail.com"),
    ]
    # Insertar los datos de clientes en la tabla
    for datos_proveedor in datos_proveedor:
        cursor.execute(insert_proveedor, datos_proveedor)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    #Tabla producto
    insert_producto = """
    INSERT INTO PRODUCTO (descripcion,precio,marca,existencia)
    VALUES (%s, %s, %s, %s)
    """

    datos_producto = [
    ("Cuidados para piso", 10, "Bandai", 8),
    ("Laptop HP", 799, "HP", 15),
    ("Teléfono Samsung", 499, "Samsung", 20),
    ("Impresora Canon", 149, "Canon", 5),
    ("Refrigerador LG", 1299, "LG", 10),
    ("Camiseta Nike", 25, "Nike", 50),
    ("Zapatos Adidas", 70, "Adidas", 30),
    ("Smart TV Sony", 899, "Sony", 8),
    ("Cámara Canon", 399, "Canon", 12),
    ("Tablet Apple", 349, "Apple", 18),
    ("Mouse Logitech", 20, "Logitech", 25),
    ("Auriculares Bose", 149, "Bose", 15),
    ("Silla de Oficina", 79, "IKEA", 30),
    ("Licuadora Oster", 39, "Oster", 7),
    ("Teclado Razer", 89, "Razer", 10),
    ("Mochila North Face", 69, "The North Face", 20)
    ]  

    # Insertar los datos de clientes en la tabla
    for datos_producto in datos_producto:
        cursor.execute(insert_producto, datos_producto)

    # Confirmar los cambios en la base de datos
    conexion.commit()


def ejecutar_consulta(consulta):
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    if resultados:
        for resultado in resultados:
            print(resultado)

def consultas():
    print("\n                                                          Consulta de datos")
    print("1. Buscar a todos los clientes que viven en el estado de Durango. ")
    print("2. Buscar los proveedores que su correo contenga '@gmail'. ")
    print("3. Buscar los productos que tengan un precio mayor a 100. ")
    print("4. Buscar los productos que tengan un precio entre 15 y 50. ")
    print("5. Buscar los pedidos que su total sea mayor a 200 y su cantidad sea mayor o igual a 10")
    print("6. Buscar los proveedores que su empresa tenga una 'i'.")

    opcion = input("Seleccione una opción:")

    # Ejecutar la consulta según la opción seleccionada
    if opcion == "1":
        consulta = "SELECT * FROM Clientes WHERE estado = 'Durango'"
        ejecutar_consulta(consulta)
    elif opcion == "2":
        consulta = "SELECT * FROM PROVEEDORES WHERE email LIKE '%@gmail%'"
        ejecutar_consulta(consulta)
    elif opcion == "3":
        consulta = "SELECT * FROM PRODUCTO WHERE precio > 100"
        ejecutar_consulta(consulta)
    elif opcion == "4":
        consulta = "SELECT * FROM PRODUCTO WHERE precio BETWEEN 15 AND 50"
        ejecutar_consulta(consulta)
    elif opcion == "5":
        consulta = "SELECT * FROM PEDIDOS WHERE total > 200 AND cantidad >= 10"
        ejecutar_consulta(consulta)
    elif opcion == "6":
        consulta = "SELECT * FROM PROVEEDORES WHERE empresa LIKE '%i%'"
        ejecutar_consulta(consulta)
    else:
        print("Opción no válida.")


# Función para obtener los datos anteriores de un registro
def obtener_datos_anteriores(tabla, campo_id, registro_id):
    consulta = f"SELECT * FROM {tabla} WHERE {campo_id} = {registro_id}"
    cursor.execute(consulta)
    return cursor.fetchone()


# Función genérica para actualizar registros en cualquier tabla
def actualizar_registro(tabla,campo_id, registro_id, nuevos_datos):
    datos_anteriores = obtener_datos_anteriores(tabla,campo_id, registro_id)

    if datos_anteriores:
        # Construir la consulta de actualización
        campos_actualizacion = ", ".join([f"{campo} = '{valor}'" for campo, valor in nuevos_datos.items()])
        consulta = f"UPDATE {tabla} SET {campos_actualizacion} WHERE {campo_id} = {registro_id}"
        
        # Obtener los nombres de campo y valores anteriores
        nombres_campos = [desc[0] for desc in cursor.description]
        valores_anteriores = list(datos_anteriores)

        # Ejecutar la consulta de actualización
        cursor.execute(consulta)
        conexion.commit()

        print(f"\n{tabla} actualizado correctamente.")

        # Mostrar los registros modificados
        print("\nDatos anteriores:")
        for nombre_campo, valor_anterior in zip(nombres_campos, valores_anteriores):
            print(f"{nombre_campo.capitalize()}: {valor_anterior}")

        print("\nDatos actualizados:")
        for campo, valor in nuevos_datos.items():
            print(f"{campo.capitalize()}: {valor}")
    else:
        print(f"No se encontraron los campos.")


def actualizar():
    while True:
        print("\n                     Actualización de datos")
        print("1. Actualizar cliente")
        print("2. Actualizar proveedor")
        print("3. Actualizar producto")
        print("4. Actualizar pedido")
        print("\n5. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")

        # Actualizar datos según la opción seleccionada
        if opcion == "1":
            # Obtener los valores necesarios para la actualización
            tabla = "Clientes"
            campo_id ="id"
            registro_id = input("Ingrese el ID del cliente que desea actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_domicilio = input("Nuevo domicilio: ")
            nuevo_ciudad = input("Nueva ciudad: ")
            nuevo_estado = input("Nuevo estado: ")
            nuevo_codigopostal = input("Nuevo código postal: ")
            nuevo_email = input("Nuevo email: ")
            nuevos_datos = {
                "nombre": nuevo_nombre,
                "domicilio": nuevo_domicilio,
                "ciudad": nuevo_ciudad,
                "estado": nuevo_estado,
                "codigopostal": nuevo_codigopostal,
                "email": nuevo_email
            }
            actualizar_registro(tabla,campo_id, registro_id, nuevos_datos)  

        elif opcion == "2":
            # Obtener los valores necesarios para la actualización
            tabla = "PROVEEDORES"
            campo_id = "id"
            registro_id = input("Ingrese el ID del proveedor que desea actualizar: ")
            n_nombredelcontacto = input ("Ingrese el nombre del contacto: ")
            n_direccion = input("Ingrese la direccion del proveedor: ")
            n_ciudad = input ("Ingrese la ciudad del proveedor: ")
            n_estado = input ("Ingrese el estado del proveedor: ")
            n_codigopostal = input ("Ingrese el codigo postal del proveedor: ")
            n_email = input ("Ingrese el email del proveedor")

            nuevos_datos = {
                "nombre del contaco ": n_nombredelcontacto,
                "domicilio": n_domicilio,
                "ciudad": n_ciudad,
                "estado": n_estado,
                "codigopostal": n_codigopostal,
                "email": n_email
            }
            actualizar_registro(tabla,campo_id, registro_id, nuevos_datos)

        elif opcion == "3":
            # Obtener los valores necesarios para la actualización
            tabla = "PRODUCTO"
            campo_id = "id"
            registro_id = input("Ingrese el ID del producto que desea actualizar: ")
            n_descripcion = input ("Ingrese la descripcion del producto: ")
            n_precio = input("Ingrese el precio del producto: ")
            n_marca = input("Ingrese la marca del producto: ")
            n_existencia = input ("Ingrese la existencia del producto")
            
            nuevos_datos = {
                "descripcion": n_descripcion,
                "precio": n_precio,
                "marca": n_marca,
                "existencia": n_existencia
            }
            actualizar_registro(tabla,campo_id, registro_id, nuevos_datos)


        elif opcion == "4":
            # Obtener los valores necesarios para la actualización
            tabla = "PEDIDO"
            campo_id = "id"
            registro_id = input ("Ingrese el Id del pedido que desea actualizar: ")
            n_nombrepedido = input ("Ingrese el nombre de pedido: ")
            n_vendedor = input ("Ingrese el vendedor del pedido: ")
            n_fecha = input ("Ingrese la fecha del pedido: ")
            n_producto = input ("Ingrese el producto: ")
            n_cantidad = input ("Ingrese la cantidad del pedido: ")
            n_precio = input ("Ingrese el precio del pedido: ")
            n_total = input ("Ingrese el total del pedido: ")

            datospedido = {
                "nombredepedido": n_nombrepedido,
                "vendedor": n_vendedor,
                "fecha": n_fecha,
                "producto": n_producto,
                "cantidad": n_cantidad,
                "precio": n_precio,
                "total": n_total
            }
            actualizar_registro(tabla,campo_id, registro_id, nuevos_datos)
            
        elif opcion == "5":
            break    
        else:
            print("Opción no válida.")


def eliminar_registro(tabla, campo_id, registro_id):
    # Verificar si el registro existe antes de eliminarlo
    cursor.execute(f"SELECT * FROM {tabla} WHERE {campo_id} = {registro_id}")
    registro = cursor.fetchone()

    if registro:
        # Ejecutar la consulta de eliminación
        cursor.execute(f"DELETE FROM {tabla} WHERE {campo_id} = {registro_id}")
        conexion.commit()
        print(f"Registro eliminado correctamente en la tabla {tabla}.")
    else:
        print(f"No se encontró un registro con {campo_id} = {registro_id} en la tabla {tabla}.")

def eliminar():
    
    while True:
        # Menú de opciones para eliminar registros
        print("\nEliminación de registros")
        print("1. Eliminar cliente")
        print("2. Eliminar proveedor")
        print("3. Eliminar producto")
        print("4. Eliminar pedido")
        print("\n5. Regresar al Menú Principal")

        opcion = input("Seleccione una opción: ")

        # Eliminar registro según la opción seleccionada
        if opcion == "1":
            id_cliente = input("Ingrese el ID del cliente que desea eliminar: ")
            eliminar_registro("Clientes", "id", id_cliente)
        elif opcion == "2":
            id_proveedor = input ("Ingrese el ID del proveedor que desea eliminar :")
            eliminar_registro("PROVEEDORES", "id", id_proveedor)
            
        elif opcion == "3":
            id_producto = input ("Ingrese el ID del producto que desea eliminar: ")
            eliminar_registro("PRODUCTO", "id", id_producto)
        elif opcion == "4":
            id_pedido = input ("Ingrese el ID del pedido que desea eliminar: ")
            eliminar_registro("PEDIDO", "id", id_pedido)
        
        elif opcion == "5":
            break    
        
        else:
            print("Opción no válida.")

def menu():
    print("\n                        Menú de Operaciones: \n")
    print("1. Agregar datos a tablas")
    print("2. Realizar Consultas")
    print("3. Actualizar Registros")
    print("4. Eliminar Registros \n")
    print("5. Salir")

while True:
    menu()
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        datos()
        print("Llenamos los datos con exito.")
    elif opcion == "2":
        consultas()
    elif opcion == "3":

        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("\nSaliendo del programa.")
        break
    else:
        print("\nOpción no válida. Por favor, selecciona una opción válida.")
        

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()