from Scrap_Tottus import Tottus
from FormatJson import FormatJson
from datetime import datetime


def extraccion_imagenes(frutas:Tottus, verduras:Tottus):
    json_frutas = frutas.extraccion_imagenes("frutas")
    json_verduras = verduras.extraccion_imagenes("verduras")

    json_final_imagenes = FormatJson.union_json(json_frutas, json_verduras)
    FormatJson.output_file_json("imagenes.json", json_final_imagenes)

def main():
    FECHA = datetime.today().strftime("%Y-%m-%d")
    LINK_FRUTAS = "https://www.tottus.com.pe/frutas-4010030/c/?sort=Recomendados"
    LINK_VERDURAS = "https://www.tottus.com.pe/verduras-4010032/c/?sort=Recomendados"
    frutas = Tottus(LINK_FRUTAS)
    verduras = Tottus(LINK_VERDURAS)

    # Extracción de características
    productos_frutas = frutas.extraccion_productos("frutas")
    productos_verduras = verduras.extraccion_productos("verduras")
    json_final_productos = FormatJson.union_json(productos_frutas, productos_verduras)
    FormatJson.output_file_json(FECHA + ".json", json_final_productos)

if __name__ == "__main__":
    main()
    print("Finalizado")
