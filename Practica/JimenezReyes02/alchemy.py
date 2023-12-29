from sqlalchemy import create_engine, Column, Integer, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from random import randint


"""
Alumno: Jimenez reyes abraham 
"""

#Crea una instancia del motor de base de datos utilizando la función create_engine. Aquí debes proporcionar la cadena de conexión a tu base de datos MySQL:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/practica2')


#Crea una clase base declarativa utilizando declarative_base:
Base = declarative_base()


#Define una clase que represente una tabla en tu base de datos:
class Cliente(Base):
    __tablename__ = 'CLIENTES'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    domicilio = Column(String(45))
    ciudad = Column(String(45))
    estado = Column(String(45))
    codigopostal = Column (Integer())
    email = Column(String(45))


class Producto(Base):
    __tablename__ = 'PRODUCTOS'
    id = Column(Integer, primary_key=True)
    descripcion = Column (String(45))
    precio = Column (Integer())
    marca = Column(String(45))
    existencia = Column(Integer())

class Proveedor(Base):
    __tablename__ = 'PROVEEDORES'
    id = Column(Integer, primary_key=True)
    empresa = Column(String(45))
    nombre_del_contacto = Column(String(45))
    direccion = Column(String(45))
    ciudad = Column(String(45))
    estado = Column(String(45))
    codigopostal = Column(Integer())
    email = Column(String(45))

class Pedido(Base):
    __tablename__ = 'PEDIDOS'
    id = Column(Integer, primary_key=True)
    nombre_de_pedido = Column(String(45))
    vendedor = Column(String(45))
    fecha_de_pedido = Column(Date())
    producto = Column(String(45))
    cantidad = Column(Integer())
    precio = Column (Integer())
    total = Column(Integer())

#Crea las tablas en la base de datos utilizando Base.metadata.create_all(engine):
Base.metadata.create_all(engine)


#Crea una sesión utilizando sessionmaker y el motor de base de datos:
Session = sessionmaker(bind=engine)
session = Session()

def create():
    # Agregar aquí el código para llenar las tablas automáticamente
    # o manualmente según tus necesidades
    
    # Llenar la tabla Cliente con datos
    cliente1 = Cliente(nombre='Eduardo',domicilio= 'Calle 2', ciudad='CDMX', estado='Mexico', codigopostal='53902', email='edu@hotmail.com')
    cliente2 = Cliente(nombre='Ana', domicilio='Avenida 5', ciudad='Guadalajara', estado='Jalisco', codigopostal='44100', email='ana@gmail.com')
    cliente3 =Cliente(nombre='Juan', domicilio='Calle 10', ciudad='Monterrey', estado='Nuevo León', codigopostal='64000', email='juan@yahoo.com')
    cliente4 =Cliente(nombre='Maria', domicilio='Paseo 3', ciudad='Puebla', estado='Puebla', codigopostal='72160', email='maria@gmail.com')
    cliente5 =Cliente(nombre='Carlos', domicilio='Boulevard 8', ciudad='Tijuana', estado='Baja California', codigopostal='22000', email='carlos@hotmail.com')
    cliente6 =Cliente(nombre='Laura', domicilio='Avenida 12', ciudad='Querétaro', estado='Querétaro', codigopostal='76000', email='laura@gmail.com')
    cliente7 =Cliente(nombre='Pedro', domicilio='Calle 15', ciudad='León', estado='Guanajuato', codigopostal='37000', email='pedro@yahoo.com')
    cliente8 = Cliente(nombre='Sofía', domicilio='Calle 7', ciudad='Merida', estado='Yucatán', codigopostal='97000', email='sofia@hotmail.com')
    cliente9 = Cliente(nombre='Luis', domicilio='Avenida 20', ciudad='Cancún', estado='Quintana Roo', codigopostal='77500', email='luis@gmail.com')
    cliente10 = Cliente(nombre='Fernanda', domicilio='Calle 9', ciudad='Acapulco', estado='Guerrero', codigopostal='39300', email='fernanda@hotmail.com')
    cliente11 = Cliente(nombre='Javier', domicilio='Paseo 25', ciudad='San Luis Potosí', estado='San Luis Potosí', codigopostal='78000', email='javier@yahoo.com')
    cliente12 = Cliente(nombre='Mariana', domicilio='Avenida 18', ciudad='Toluca', estado='México', codigopostal='50000', email='mariana@gmail.com')
    cliente13 = Cliente(nombre='Roberto', domicilio='Boulevard 14', ciudad='Hermosillo', estado='Sonora', codigopostal='83000', email='roberto@hotmail.com')
    cliente14 = Cliente(nombre='Paula', domicilio='Calle 6', ciudad='Durango', estado='Durango', codigopostal='34000', email='paula@yahoo.com')
    cliente15 = Cliente(nombre='Paul', domicilio='Calle 1', ciudad='Durango', estado='Durango', codigopostal='34000', email='paula@yahoo.com')

    # Agrega más clientes según sea necesario para cumplir con la condición

    # Llenar la tabla Proveedor con datos
    proveedor1 = Proveedor(empresa='Empresa A', nombre_del_contacto= 'Pedro',direccion= 'Calle 989', ciudad= 'CDMX', estado='Mexico',codigopostal='66098',email='pedro@ejemplo.com')
    proveedor2 = Proveedor(empresa='Empresa B', nombre_del_contacto='Luisa', direccion='Avenida 45', ciudad='Guadalajara', estado='Jalisco', codigopostal='44123', email='luisa@gmail.com')
    proveedor3 = Proveedor(empresa='Empresa C', nombre_del_contacto='Juan', direccion='Calle 12', ciudad='Monterrey', estado='Nuevo León', codigopostal='64050', email='juan@proveedor.com')
    proveedor4 = Proveedor(empresa='Empresa D', nombre_del_contacto='María', direccion='Paseo 78', ciudad='Puebla', estado='Puebla', codigopostal='72134', email='maria@hotmail.com')
    proveedor5 = Proveedor(empresa='Empresa E', nombre_del_contacto='Andrés', direccion='Boulevard 56', ciudad='Tijuana', estado='Baja California', codigopostal='22034', email='andres@empresa.com')
    proveedor6 = Proveedor(empresa='Empresa F', nombre_del_contacto='Laura', direccion='Avenida 23', ciudad='Querétaro', estado='Querétaro', codigopostal='76021', email='laura@proveedora.com')
    proveedor7 = Proveedor(empresa='Empresa G', nombre_del_contacto='Ricardo', direccion='Calle 5', ciudad='León', estado='Guanajuato', codigopostal='37080', email='ricardo@gmail.com')
    proveedor8 = Proveedor(empresa='Empresa H', nombre_del_contacto='Sofía', direccion='Calle 67', ciudad='Merida', estado='Yucatán', codigopostal='97012', email='sofia@ejemplo.com')
    proveedor9 = Proveedor(empresa='Empresa I', nombre_del_contacto='Eduardo', direccion='Paseo 14', ciudad='Cancún', estado='Quintana Roo', codigopostal='77542', email='eduardo@empresa.com')
    proveedor10 = Proveedor(empresa='Empresa J', nombre_del_contacto='Ana', direccion='Calle 33', ciudad='Acapulco', estado='Guerrero', codigopostal='39321', email='ana@proveedora.com')
    proveedor11 = Proveedor(empresa='Empresa K', nombre_del_contacto='Roberto', direccion='Avenida 7', ciudad='San Luis Potosí', estado='San Luis Potosí', codigopostal='78009', email='roberto@hotmail.com')
    proveedor12 = Proveedor(empresa='Empresa L', nombre_del_contacto='Mariana', direccion='Boulevard 21', ciudad='Toluca', estado='México', codigopostal='50089', email='mariana@ejemplo.com')
    proveedor13 = Proveedor(empresa='Empresa M', nombre_del_contacto='Javier', direccion='Calle 11', ciudad='Hermosillo', estado='Sonora', codigopostal='83076', email='javier@empresa.com')
    proveedor14 = Proveedor(empresa='Empresa N', nombre_del_contacto='Carolina', direccion='Paseo 5', ciudad='Durango', estado='Durango', codigopostal='34045', email='carolina@proveedora.com')
    proveedor15 = Proveedor(empresa='Empresa O', nombre_del_contacto='Pedro', direccion='Avenida 98', ciudad='Mérida', estado='Yucatán', codigopostal='97090', email='pedro@ejemplo.com')

    # Agrega más proveedores según sea necesario para cumplir con la condición

    # Llenar la tabla Producto con datos
    producto1 = Producto(descripcion='Gamesa',precio= 3, marca='Dell', existencia= 10)
    producto2 = Producto(descripcion='Laptop HP', precio=800, marca='HP', existencia=5)
    producto3 = Producto(descripcion='Smartphone Samsung', precio=500, marca='Samsung', existencia=8)
    producto4 = Producto(descripcion='Monitor LG', precio=200, marca='LG', existencia=12)
    producto5 = Producto(descripcion='Impresora Canon', precio=150, marca='Canon', existencia=6)
    producto6 = Producto(descripcion='Teclado Logitech', precio=30, marca='Logitech', existencia=15)
    producto7 = Producto(descripcion='Mouse Microsoft', precio=20, marca='Microsoft', existencia=20)
    producto8 = Producto(descripcion='Auriculares Sony', precio=50, marca='Sony', existencia=10)
    producto9 = Producto(descripcion='Cámara Canon', precio=300, marca='Canon', existencia=7)
    producto10 = Producto(descripcion='Tablet Lenovo', precio=150, marca='Lenovo', existencia=9)
    producto11 = Producto(descripcion='Smart TV Samsung', precio=600, marca='Samsung', existencia=4)
    producto12 = Producto(descripcion='Refrigerador Whirlpool', precio=800, marca='Whirlpool', existencia=3)
    producto13 = Producto(descripcion='Licuadora Oster', precio=40, marca='Oster', existencia=14)
    producto14 = Producto(descripcion='Silla de Oficina', precio=60, marca='Generic', existencia=25)
    producto15 = Producto(descripcion='Bicicleta Schwinn', precio=200, marca='Schwinn', existencia=6)

    # Agrega más productos según sea necesario para cumplir con la condición

    # Llenar la tabla Pedido con datos
    pedido1 = Pedido(nombre_de_pedido='Pedido 1',vendedor='Luis', fecha_de_pedido='2023-02-01',producto='Libreta', cantidad=5, precio=6, total=5*6)
    pedido2 = Pedido(nombre_de_pedido='Pedido 2', vendedor='Ana', fecha_de_pedido='2023-02-05', producto='Lápices', cantidad=10, precio=2, total=10*2)
    pedido3 = Pedido(nombre_de_pedido='Pedido 3', vendedor='Juan', fecha_de_pedido='2023-02-10', producto='Cuaderno', cantidad=3, precio=8, total=3*8)
    pedido4 = Pedido(nombre_de_pedido='Pedido 4', vendedor='María', fecha_de_pedido='2023-03-02', producto='Bolígrafos', cantidad=7, precio=3, total=7*3)
    pedido5 = Pedido(nombre_de_pedido='Pedido 5', vendedor='Carlos', fecha_de_pedido='2023-03-05', producto='Papel', cantidad=4, precio=5, total=4*5)
    pedido6 = Pedido(nombre_de_pedido='Pedido 6', vendedor='Laura', fecha_de_pedido='2023-03-12', producto='Tijeras', cantidad=2, precio=4, total=2*4)
    pedido7 = Pedido(nombre_de_pedido='Pedido 7', vendedor='Pedro', fecha_de_pedido='2023-04-03', producto='Reglas', cantidad=8, precio=1, total=8*1)
    pedido8 = Pedido(nombre_de_pedido='Pedido 8', vendedor='Sofía', fecha_de_pedido='2023-04-05', producto='Goma de borrar', cantidad=6, precio=2, total=6*2)
    pedido9 = Pedido(nombre_de_pedido='Pedido 9', vendedor='Luis', fecha_de_pedido='2023-04-10', producto='Libros', cantidad=5, precio=10, total=5*10)
    pedido10 = Pedido(nombre_de_pedido='Pedido 10', vendedor='Ana', fecha_de_pedido='2023-05-01', producto='Carpeta', cantidad=3, precio=7, total=3*7)
    pedido11 = Pedido(nombre_de_pedido='Pedido 11', vendedor='Juan', fecha_de_pedido='2023-05-05', producto='Pegamento', cantidad=4, precio=3, total=4*3)
    pedido12 = Pedido(nombre_de_pedido='Pedido 12', vendedor='María', fecha_de_pedido='2023-01-23', producto='Calculadora', cantidad=2, precio=15, total=2*15)
    pedido13 = Pedido(nombre_de_pedido='Pedido 13', vendedor='Carlos', fecha_de_pedido='2023-06-02', producto='Mochila', cantidad=1, precio=25, total=1*25)
    pedido14 = Pedido(nombre_de_pedido='Pedido 14', vendedor='Laura', fecha_de_pedido='2023-04-24', producto='Cinta adhesiva', cantidad=5, precio=2, total=5*2)
    pedido15 = Pedido(nombre_de_pedido='Pedido 15', vendedor='Pedro', fecha_de_pedido='2023-06-10', producto='Estuche', cantidad=2, precio=8, total=2*8)

    # Agrega más pedidos según sea necesario para cumplir con la condición

    # Agregar los registros a la sesión y confirmar los cambios
    session.add_all([cliente1, cliente2, cliente3, cliente4, cliente5,cliente6, cliente7,cliente8,cliente9,cliente10,cliente11,cliente12,cliente13,cliente14,cliente15])
    session.add_all([proveedor1, proveedor2, proveedor3, proveedor4, proveedor5,proveedor6, proveedor7, proveedor8, proveedor9, proveedor10,proveedor11, proveedor12, proveedor13, proveedor14,proveedor15])
    session.add_all([producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9,producto10,producto11,producto12, producto13, producto14, producto15])
    session.add_all([pedido1, pedido2, pedido3, pedido4, pedido5, pedido6, pedido7, pedido8, pedido9, pedido10,pedido11,pedido12,pedido13,pedido14,pedido15])
    session.commit()


    """
    Consultas
    """
def read():
    print("\n                                                          Consulta de datos")
    print("1. Buscar a todos los clientes cuyo nombre empiece con 'E'")
    print("2. Buscar los proveedores que su correo contenga al menos una letra 'a'")
    print("3. Buscar los productos que tengan existencia")
    print("4. Buscar los productos cuya marca empiece con 'D'")
    print("5. Buscar los pedidos cuya fecha esté entre 24/01/2023 y 24/04/2023")
    print("6. Consulta personalizada de proveedores (condición diferente a la del ejercicio 1)")

    opcion = input("Seleccione una opción:")

    if opcion == "1":
        # Realizar la consulta para buscar clientes cuyo nombre empiece con 'E'
        clientes = session.query(Cliente).filter(Cliente.nombre.like('E%')).all()
        for cliente in clientes:
            print(f"\nID: {cliente.id} cliente: {cliente.nombre}")

    elif opcion == "2":
        # Realizar la consulta para buscar proveedores cuyo correo contenga al menos una 'a'
        proveedores = session.query(Proveedor).filter(Proveedor.email.like('%a%')).all()
        for proveedor in proveedores:
            print(f"\nProveedor: {proveedor.id} {proveedor.empresa} - Correo: {proveedor.email}")

    elif opcion == "3":
        # Realizar la consulta para buscar productos con existencia
        productos = session.query(Producto).filter(Producto.existencia > 0).all()
        for producto in productos:
            print(f"\nDescripcion: {producto.descripcion} ({producto.existencia} en existencia)")

    elif opcion == "4":
        # Realizar la consulta para buscar productos cuya marca empiece con 'D'
        productos = session.query(Producto).filter(Producto.marca.like('D%')).all()
        for producto in productos:
            print(f"\nID: {producto.id} Descripcion: {producto.descripcion}  Marca: {producto.marca}")

    elif opcion == "5":
        # Realizar la consulta para buscar pedidos dentro del rango de fechas
        # Ajusta las fechas según tus necesidades
        pedidos = session.query(Pedido).filter(Pedido.fecha_de_pedido.between('2023-01-24', '2023-04-24')).all()
        for pedido in pedidos:
            print(f"\nPedido {pedido.id} - Fecha: {pedido.fecha_de_pedido}")
    elif opcion == "6":
        
        # Realizar la consulta para buscar proveedores cuyo nombre del contacto contenga al menos una 'a'
        proveedores = session.query(Proveedor).filter(Proveedor.nombre_del_contacto.like('%a%')).all()
        for proveedor in proveedores:
            print(f"\nID: {proveedor.id} Sociedad: {proveedor.empresa} Nombre: {proveedor.nombre_del_contacto}")
    
    else:
        print("Opción no válida")


def update():
    while True:
        print("\n                     Actualización de datos")
        print("1. Actualizar cliente")
        print("2. Actualizar proveedor")
        print("3. Actualizar producto")
        print("4. Actualizar pedido")
        print("\n5. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Actualizar un cliente por ID
            cliente_id = input("Ingrese el ID del cliente que desea actualizar: ")
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            
            if cliente:

                datos_cliente = {
                    "nombre": cliente.nombre,
                    "domicilio": cliente.domicilio,
                    "ciudad": cliente.ciudad,
                    "estado" : cliente.estado,
                    "codigopostal" : cliente.codigopostal,
                    "email" : cliente.email
                }

                # Modificar los datos del cliente
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_domicilio = input("Domicilio: ")
                n_ciudad = input ("Ciudad: ")
                n_estado = input ("Estado: ")
                n_codigopostal = input ("Codigo postal: ")
                n_email = input ("Email: ")

                cliente.nombre = nuevo_nombre
                cliente.domicilio = nuevo_domicilio
                cliente.ciudad = n_ciudad
                cliente.estado = n_estado
                cliente.codigopostal = n_codigopostal
                cliente.email = n_email
                
                session.commit()
                print("\nCliente actualizado correctamente.")

                # Mostrar los registros modificados
                print("\n                                  Datos anteriores:")
                for campo, valor in datos_cliente.items():
                    print(f"{campo.capitalize()}: {valor}")
                print("\n                                  Datos actualizados:")
                for campo, valor in datos_cliente.items():
                    print(f"{campo.capitalize()}: {getattr(cliente, campo)}")
            else:
                print("Cliente no encontrado.")
            
        elif opcion == "2":
            # Actualizar un proveedor por ID
            proveedor_id = input("Ingrese el ID del proveedor que desea actualizar: ")
            proveedor = session.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
            
            if proveedor:

                datos_proveedor = {
                    "empresa": proveedor.empresa,
                    "nombre_del_contacto": proveedor.nombre_del_contacto,
                    "direccion": proveedor.direccion,
                    "ciudad": proveedor.ciudad,
                    "estado" : proveedor.estado,
                    "codigopostal" : proveedor.codigopostal,
                    "email" : proveedor.email
                }

                # Modificar los datos del proveedor
                nuevo_empresa = input("Nueva empresa: ")
                n_nombre_del_contacto = input("Nombre del contacto: ")
                n_direccion = input("Direccion: ")
                n_ciudad = input ("Ciudad: ")
                n_estado = input("Estado: ")
                n_codigopostal = input("Codigo postal: ")
                n_email = input ("Email: ")

                proveedor.empresa = nuevo_empresa
                proveedor.nombre_del_contacto = n_nombre_del_contacto
                proveedor.direccion = n_direccion
                proveedor.ciudad = n_ciudad
                proveedor.estado = n_estado
                proveedor.codigopostal = n_codigopostal
                proveedor.email = n_email

                session.commit()
                print("\nProveedor actualizado correctamente.")

                # Mostrar los registros modificados
                print("\n                                     Datos originales:")
                for campo, valor in datos_proveedor.items():
                    print(f"{campo.capitalize()}: {valor}")
                print("\n                                     Datos actualizados:")
                for campo, valor in datos_proveedor.items():
                    print(f"{campo.capitalize()}: {getattr(proveedor, campo)}")

            else:
                print("Proveedor no encontrado.")
            
        elif opcion == "3":
            # Actualizar un producto por ID
            producto_id = input("Ingrese el ID del producto que desea actualizar: ")
            producto = session.query(Producto).filter(Producto.id == producto_id).first()
            
            if producto:

                datos_producto = {
                    "descripcion": producto.descripcion,
                    "precio": producto.precio,
                    "marca": producto.marca,
                    "existencia": producto.existencia
                }

                # Modificar los datos del producto
                nueva_descripcion = input("Descripción: ")
                n_precio = input("Precio: ")
                nueva_marca = input("Marca: ")
                nueva_existencia = input("Existencia: ")
                
                producto.descripcion = nueva_descripcion
                producto.precio = n_precio
                producto.marca = nueva_marca
                producto.existencia = nueva_existencia
                
                session.commit()
                print("\nProducto actualizado correctamente.")

                # Mostrar los registros modificados
                print("\n                                   Datos originales:")
                for campo, valor in datos_producto.items():
                    print(f"{campo.capitalize()}: {valor}")
                print("\n                                   Datos actualizados:")
                for campo, valor in datos_producto.items():
                    print(f"{campo.capitalize()}: {getattr(producto, campo)}")
            else:
                print("Producto no encontrado.")
            
        elif opcion == "4":
            # Actualizar un pedido por ID
            pedido_id = input("Ingrese el ID del pedido que desea actualizar: ")
            pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
            

            if pedido:
                # Modificar los datos del pedido
                datos_originales = {
                    "nombre_de_pedido": pedido.nombre_de_pedido,
                    "fecha_de_pedido": pedido.fecha_de_pedido,
                    "producto": pedido.producto,
                    "cantidad": pedido.cantidad,
                    "precio" : pedido.precio,
                    "total" : pedido.total
                }

                nuevo_nombre_pedido = input("Nuevo nombre de pedido: ")
                nueva_fecha_pedido = input("Nueva fecha de pedido (YYYY-MM-DD): ")
                nueva_cantidad = input("Nueva cantidad: ")
                n_producto = input ("Producto: ")
                n_precio = input ("Precio: ")
                n_total = input ("Total: ")
                
                pedido.nombre_de_pedido = nuevo_nombre_pedido
                pedido.fecha_de_pedido = nueva_fecha_pedido
                pedido.cantidad = nueva_cantidad
                pedido.producto = n_producto
                pedido.precio = n_precio
                pedido.total = n_total
                
                session.commit()
                print("\nPedido actualizado correctamente.")

                # Mostrar los registros modificados
                print("\n                                 Datos originales:")
                for campo, valor in datos_originales.items():
                    print(f"{campo.capitalize()}: {valor}")
                print("\n                                 Datos actualizados:")
                for campo, valor in datos_originales.items():
                    print(f"{campo.capitalize()}: {getattr(pedido, campo)}")

            else:
                print("Pedido no encontrado.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida")

def delete():
    while True:
        print("\n                   Eliminación de datos")
        print("1. Eliminar cliente")
        print("2. Eliminar proveedor")
        print("3. Eliminar producto")
        print("4. Eliminar pedido")
        print("\n5. Regresar al Menú Principal")

        opcion = input("Seleccione una opción:")
        
        if opcion == "1":
            # Eliminar un cliente por ID
            cliente_id = input("Ingrese el ID del cliente que desea eliminar: ")
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            
            if cliente:
                session.delete(cliente)
                session.commit()
                print("\nCliente eliminado correctamente.")
            else:
                print("Cliente no encontrado.")
            
        elif opcion == "2":
            # Eliminar un proveedor por ID
            proveedor_id = input("Ingrese el ID del proveedor que desea eliminar: ")
            proveedor = session.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
            
            if proveedor:
                session.delete(proveedor)
                session.commit()
                print("\nProveedor eliminado correctamente.")
            else:
                print("Proveedor no encontrado.")
            
        elif opcion == "3":
            # Eliminar un producto por ID
            producto_id = input("Ingrese el ID del producto que desea eliminar: ")
            producto = session.query(Producto).filter(Producto.id == producto_id).first()
            
            if producto:
                session.delete(producto)
                session.commit()
                print("\nProducto eliminado correctamente.")
            else:
                print("Producto no encontrado.")
            
        elif opcion == "4":
            pedido_id = input("Ingrese el ID del pedido que desea eliminar: ")
            pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
            
            if pedido:
                session.delete(pedido)
                session.commit()
                print("\nPedido eliminado correctamente.")
            else:
                print("Pedido no encontrado.")
        
        elif opcion == "5":
            break    
        else:
            print("\nOpción no válida")



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
        create()
        print("Llenamos los datos con exito.")
    elif opcion == "2":
        read()
    elif opcion == "3":
        update()
    elif opcion == "4":
        delete()
    elif opcion == "5":
        print("\nSaliendo del programa.")
        session.close()
        break
    else:
        print("\nOpción no válida. Por favor, selecciona una opción válida.")


#Recuerda cerrar la sesión cuando hayas terminado:
session.close()

