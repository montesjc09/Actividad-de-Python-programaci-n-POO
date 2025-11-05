# ------------------ Clase SERVIDOR ------------------
class Servidor:
    def __init__(self):
        pass

    def muestra_pagina(self):
        return "Página mostrada correctamente."

    def envia_sugerencia(self):
        return "Sugerencia enviada al servidor."

    def envia_datos_de_compra(self):
        return "Datos de compra enviados."

    def envia_datos_de_venta(self):
        return "Datos de venta enviados."


# ------------------ Clase PROCESADOR ------------------
class Procesador:
    def __init__(self):
        pass

    def mandar_datos_de_venta(self):
        return "Datos de venta mandados."

    def mandar_articulo_online(self):
        return "Artículo online mandado."

    def envia_sugerencia_administrador(self):
        return "Sugerencia enviada al administrador."

    def modificar_stock(self):
        return "Stock modificado."

    def realizar_cobro(self):
        return "Cobro realizado."

    def realizar_pago(self):
        return "Pago realizado."

    def actualiza_catalogo(self):
        return "Catálogo actualizado."

    def realiza_busqueda(self):
        return "Búsqueda realizada."


# ------------------ Clase RECOLECTOR ------------------
class Recolector:
    def __init__(self):
        pass

    def envia_novedades(self):
        return "Novedades enviadas."


# ------------------ Clase INDEXADOR ------------------
class Indexador:
    def __init__(self):
        pass

    def actualiza_almacen(self):
        return "Almacén actualizado."

    def envia_resultado_busqueda(self):
        return "Resultado de búsqueda enviado."


# ------------------ Clase EDITORIAL ------------------
class Editorial:
    def __init__(self, nombre="", direccion="", telefono=""):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        return f"Editorial {self.nombre} ha realizado una venta."


# ------------------ Clase HILO ------------------
class Hilo:
    def __init__(self):
        pass

    def busca_novedades(self):
        return "Buscando novedades..."


# ------------------ Clase USUARIO ------------------
class Usuario:
    def __init__(self, nombre="", apellido="", cuenta="", direccion="", login="", password=""):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        return f"{self.nombre} ha enviado una sugerencia."

    def leer(self):
        return f"{self.nombre} está leyendo un artículo."

    def comprar(self):
        return f"{self.nombre} ha realizado una compra."

    def vender(self):
        return f"{self.nombre} ha realizado una venta."

    def realizar_reclamacion(self):
        return f"{self.nombre} ha realizado una reclamación."


# ------------------ Clase PRODUCTO ------------------
class Producto:
    def __init__(self, precio=0, autor="", editorial="", anio_edicion=0, preferencias=""):
        self.precio = precio
        self.autor = autor
        self.editorial = editorial
        self.anio_edicion = anio_edicion
        self.preferencias = preferencias

    def vender(self):
        return "Producto vendido."

    def comprar(self):
        return "Producto comprado."

    def ver_catalogo(self):
        return "Catálogo de productos disponible."


# ------------------ Clase LIBRO ------------------
class Libro:
    def __init__(self, genero=""):
        self.genero = genero


# ------------------ Clase REVISTA ------------------
class Revista:
    def __init__(self, categoria=""):
        self.categoria = categoria


# ------------------ Clase ARTICULO_DE_SEGUNDA_MANO ------------------
class ArticuloSegundaMano:
    def __init__(self, clasificacion="", tema="", vendedor=""):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor


# ------------------ Clase NOVEDADES ------------------
class Novedades:
    def __init__(self, clasificacion="", tema=""):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva_clasificacion):
        self.clasificacion = nueva_clasificacion
        return f"Nueva clasificación: {self.clasificacion}"


# ------------------ Clase ARTICULO_ONLINE ------------------
class ArticuloOnline:
    def __init__(self, tema=""):
        self.tema = tema

    def publicar(self):
        return f"Artículo sobre {self.tema} publicado correctamente."
