import csv
import os

NOMBRE_ARCHIVO = "paises.csv"
archivo_existe = os.path.exists(NOMBRE_ARCHIVO)
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

def obtener_paises(archivo):
    """Obtengo los paises del archivo CSV y devuelvo una lista de diccionarios con los mismos."""
    try:
        with open(archivo, "r", encoding="utf-8") as archivo:
            #Genero la variable que va a contener la informacion del archivo
            lector = csv.DictReader(archivo, delimiter=",")

            #Inicializo la lista a retornar.
            lista_paises = []
            
            #Recorro la informacion del csv y le asigno los atributos dentro de un diccionario por pais.
            for pais in lector:
                dic_pais = {
                    "nombre": pais["nombre"],
                    "poblacion": int(pais["poblacion"]),
                    "superficie": int(pais["superficie"]),
                    "continente": pais["continente"]
                }
                #Añado el diccionario a la lista
                lista_paises.append(dic_pais)
            #Devuelvo la lista con los paises que se encuentran en el csv
            return lista_paises
    except FileNotFoundError:
        print("El archivo de paises no existe. Por favor primero agregar paises al archivo para que se cree.")
    except Exception as e:
        print(f"Ha ocurrido el siguiente error: {e}")

def añadir_pais(archivo, pais):
    """Añado el pais indicado a la lista"""
    try:
        with open(archivo, "a", newline="",encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(pais)
    except PermissionError:
        print("Error: No se puede acceder al archivo, este podria estar siendo utilizado por otro programa.")

        
def actualizar_archivo(archivo,lista_pais, columnas):
    """Sobreescribe el archivo csv con la lista de diccionarios de paises indicada"""
    try:
        with open(archivo, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            
            writer.writeheader()
            writer.writerows(lista_pais)
    except PermissionError:
        print("Error: No se puede acceder al archivo, este podria estar siendo utilizado por otro programa.")

paises = obtener_paises(NOMBRE_ARCHIVO)

paises[0]["nombre"] = "Brasil"
print(paises[0]["nombre"])
actualizar_archivo(NOMBRE_ARCHIVO, paises, CAMPOS)