import json
import urllib.request
from bs4 import BeautifulSoup


class Tottus:
    def __init__(self, link_web):
        self._link = link_web

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link_web:str):
        self._link = link_web

    def descargar_web(self):
        consulta = urllib.request.Request(self._link, headers={"User-Agent": "Mozilla/5.0"})
        consulta = urllib.request.urlopen(consulta)
        return consulta.read()

    def obtener_json(self):
        archivo_html = self.descargar_web()
        soup = BeautifulSoup(archivo_html, "html5lib")
        encontrar_json = soup.find("script", id="__NEXT_DATA__")
        return encontrar_json.string

    def extraccion_productos(self, clase:str) -> dict:
        # Cargando el json donde se encuentran todos los productos
        archivo_prueba = self.obtener_json()
        data = json.loads(str(archivo_prueba))

        # Dirección de los productos
        direccion_productos = data["props"]["pageProps"]["products"]["results"]
        informacion_extraida = []

        for productos in direccion_productos:
            # Obteniendo los precios
            if productos["prices"]["unitPrice"] is None:
                precio = productos["prices"]["currentPrice"]
            else:
                precio = productos["prices"]["unitPrice"]
            # Obtención de la unidad de medida del producto o cantidad
            if "contenido" in productos["attributes"]:
                contenido = productos["attributes"]["contenido"]
            else:
                contenido = productos["attributes"]["unidad-de-medida"]
            # Llenado del json
            informacion_extraida.append({
                "nombre": productos["name"],
                "precio": precio,
                "contenido": contenido,
            })

        # Carga de la lista de diccionario en un archivo
        return {clase: informacion_extraida}
    
    def extraccion_imagenes(self, clase:str) -> dict:
        archivo_prueba = self.obtener_json()
        data  = json.loads(str(archivo_prueba))
        direccion_productos = data["props"]["pageProps"]["products"]["results"]
        link_imagenes = []
        for productos in direccion_productos:
            link_imagenes.append({
                "nombre": productos["name"],
                "imagenes": productos["images"][0]
            })
        return {clase: link_imagenes}
