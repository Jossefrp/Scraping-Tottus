from ast import arg
import json

class FormatJson:

    @staticmethod
    def output_file_json(nombre_archivo: str,  arg):
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            json.dump(arg, file, indent=4)

    @staticmethod
    def union_json(*args) -> dict:
        union_json = dict()
        for i in args:
            union_json |= i
        return union_json
