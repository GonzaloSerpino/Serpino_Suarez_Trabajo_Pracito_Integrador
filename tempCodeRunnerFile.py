import csv
import os
import re

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
        
def validar_inputs(valor, flag=0):
    """Devuelve True o False dependiendo si lo ingresado en los inputs es valido"""
    
    #Utilizo Regex para validar los entries
    
    #Indico que para que el input sea valido tiene que tener solo valores alfabeticos y tiene que ser de un largo de minimo 3 caracteres hasta maximo 50
    patron_alpha = re.compile(r"^[a-zA-ZáéíóúñÁÉÍÓÚÑ ]{3,50}$")
    # El \d indica dígitos, y ^ $ aseguran que sea TODA la cadena
    patron_num = re.compile(r"^\d{3,50}$")

    
    #Creo variables flags para indicar si cumple con las condiciones o no
    if not flag:
        flag_valor = patron_alpha.match(valor)
    else:
        flag_valor = patron_num.match(valor)
    
    #Si todos los inputs cumplen con las condiciones devuelvo True, sino devuelvo False.
    return bool(flag_valor)

def buscar_pais(nombre_pais):
    """Busco el nombre del pais, si esta dentro de la lista, retorno True, sino False"""
    global paises
    for pais in paises:
        if pais["nombre"] == nombre_pais:
            return True, pais
    return False, None

def modificacion_pais(pais):
    """Menu y modificacion de pais"""
    try:
        print("------------ Modificacion Pais ------------")
        print(f"Que desea modificar del pais {pais["nombre"]}?")
        print("1. Nombre\n2. Poblacion\n3. Superficie\n4. Continente")
        opcion = int(input("Seleccione una opcion: "))
    
        if opcion == 1:
            nombre_nuevo = input("Ingrese el nuevo nombre del pais: ").title()
            while not validar_inputs(nombre_nuevo):
                print("Valor de nombre invalido, por favor ingrese un valor correcto.")
                nombre_nuevo = input("Ingrese el nombre del pais a actualizar: ").title()
            
            pais["nombre"] = nombre_nuevo
                
        elif opcion == 2:
            poblacion_nueva = input("Ingrese el valor nuevo de la poblacion: ")
            while not validar_inputs(poblacion_nueva,1):
                print("Valor de poblacion invalido, por favor ingrese un valor correcto.")
                poblacion_nueva = input("Ingrese el valor nuevo de la poblacion: ")
            
            pais["poblacion"] = int(poblacion_nueva)
            
        elif opcion == 3:
            superficie_nueva = input("Ingrese el nuevo valor de la superficie: ")
            while not validar_inputs(superficie_nueva,1):
                print("Valor de superficie invalido, por favor ingrese un valor correcto.")
                superficie_nueva = input("Ingrese el nuevo valor de la superficie: ")
            
            pais["superficie"] = int(superficie_nueva)
            
        elif opcion == 4:
            continente_nuevo = input("Ingrese el nuevo valor del continente: ")
            while not validar_inputs(continente_nuevo):
                print("Valor de continente invalido, por favor ingrese un valor correcto.")
                continente_nuevo = input("Ingrese el nuevo valor del continente: ")
            
            pais["continente"] = int(continente_nuevo)
            
        else:
            print("Valor de opcion incorrecta, intente nuevamente")
        return pais
    except ValueError:
        print("Valor de opcion incorrecto, por favor intenta nuevamente.")
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    

def actualizar_pais():
    """Validador de nombre pais y actualizacion en csv"""
    #Traigo la lista global de paises
    try:
        global paises
        nombre = input("Ingrese el nombre del pais a actualizar: ").title()
        #Valido si el input ingresado es correcto
        while not validar_inputs(nombre):
            print("Valor de nombre invalido, por favor ingrese un valor correcto.")
            nombre = input("Ingrese el nombre del pais a actualizar: ").title()
        #me traigo la flag si el pais esta dentro de la lista o no
        flag, pais = buscar_pais(nombre)
        #si esta dentro de la lista, reemplazo el pais existente con los datos modificados.
        if flag:
            pais_modificado = modificacion_pais(pais)
            #Recorro la lista de paises global para encontrar el pais a reemplazar.
            for i in range(len(paises)):
                if paises[i]["nombre"] == nombre:
                    paises[i] = pais_modificado        
            actualizar_archivo(NOMBRE_ARCHIVO, paises, CAMPOS)
            
        else:
            print("El pais no se encuentra en la lista. Por favor intente nuevamente o ingreselo en la opcion 1.")
    except Exception as e:
        print(f"Se encontro el siguiente error: {e}")

paises = obtener_paises(NOMBRE_ARCHIVO)
actualizar_pais()

#paises[0]["nombre"] = "Brasil"
#print(paises[0]["nombre"])
#actualizar_archivo(NOMBRE_ARCHIVO, paises, CAMPOS)
