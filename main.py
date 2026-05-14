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

def buscar_pais(valor,tipo_busqueda):
    """Busco el nombre del pais, si esta dentro de la lista, retorno True, sino False"""
    global paises
    #seteo por default el valor de la bandera
    flag = 0
    #Genero una lista temporal ya que las busquedas por poblacion, superficie y continente pueden tener mas de un resultado
    lista_paises_temp = []
    #Si el tipo de busqueda es 1, busco el pais por nombre
    if tipo_busqueda == 1:
        for pais in paises:
            if pais["nombre"] == valor:
                return True, pais
    #Si es 2, lo busco por poblacion
    elif tipo_busqueda == 2:
        for pais in paises:
            if pais["poblacion"] == valor:
                lista_paises_temp.append(pais)
                flag = 1
    #Si es 3, lo busco por superficie
    elif tipo_busqueda == 3:
        for pais in paises:
            if pais["superficie"] == valor:
                lista_paises_temp.append(pais)
                flag = 1
    #Si es 4, lo busco por continente
    elif tipo_busqueda == 4:
        for pais in paises:
            if pais["continente"] == valor:
                lista_paises_temp.append(pais)
                flag = 1
    
    if flag: 
        return True, lista_paises_temp
    else:
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
        flag, pais = buscar_pais(nombre,1)
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

def busqueda():
    """Menu y busqueda de paises"""
    try:
        global paises
        match_paises = []
        print("------------ Busqueda Pais ------------")
        print(f"Como desea realizar la busqueda?")
        print("1. Por Nombre\n2. Por Poblacion\n3. Por Superficie\n4. Por Continente")
        opcion = int(input("Seleccione una opcion: "))
    
        #Si la opcion es 1, busco por nombre
        if opcion == 1:
            valor_busqueda = input("Ingrese el nombre del pais a buscar: ").title()
            while not validar_inputs(valor_busqueda):
                print("Valor de nombre invalido, por favor ingrese un valor correcto.")
                valor_busqueda = input("Ingrese el nombre del pais a buscar: ").title()
            
            #Traigo el flag que me va a indicar si encontro el pais y el contenido de ese pais
            flag, match_paises = buscar_pais(valor_busqueda,opcion)
            if flag: 
                print(f"Pais: {match_paises["nombre"]} | Poblacion: {match_paises["poblacion"]} | Superficie: {match_paises["superficie"]} | Continente: {match_paises["continente"]}")
            else:
                print("No existe un pais con ese nombre, agregelo a la lista.")
                
        #Me guardo el input de la poblacion a buscar
        elif opcion == 2:
            valor_busqueda = input("Ingrese el valor de la poblacion a buscar: ")
            while not validar_inputs(valor_busqueda,1):
                print("Valor de poblacion invalido, por favor ingrese un valor correcto.")
                valor_busqueda = input("Ingrese el valor de la poblacion a buscar: ")
            valor_busqueda = int(valor_busqueda)
            
        #Me guardo el input de la superficie a buscar
        elif opcion == 3:
            valor_busqueda = input("Ingrese el valor de la superficie a buscar: ")
            while not validar_inputs(valor_busqueda,1):
                print("Valor de superficie invalido, por favor ingrese un valor correcto.")
                valor_busqueda = input("Ingrese el valor de la superficie a buscar: ")
            valor_busqueda = int(valor_busqueda)
            

        #Me guardo el input del continente a buscar
        elif opcion == 4:
            valor_busqueda = input("Ingrese el valor del continente a buscar: ")
            while not validar_inputs(valor_busqueda):
                print("Valor de continente invalido, por favor ingrese un valor correcto.")
                valor_busqueda = input("Ingrese el valor del continente a buscar: ")
              
        else:
            print("Valor de opcion incorrecta, intente nuevamente")
        
        #Como pueden ser mas de un pais que puede compartir el mismo valor en poblacion, contiente y superficie, los englobo en un solo if
        if opcion >= 2 and opcion <= 4:
            flag, match_paises = buscar_pais(valor_busqueda,opcion)
            if flag:
                for pais in match_paises:
                    print(f"Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
            else:
                print("No existen paises con ese numero de poblacion/superficie/continente indicado.")
    except ValueError:
        print("Valor de opcion incorrecto, por favor intenta nuevamente.")
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    
def promedio_superficie():
    global paises
    acu = 0
    count = 0
    for pais in paises:
        acu += pais["superficie"]
        count += 1
    
    promedio = float(acu / count)
    
    return promedio
    
def paises_continentes():
    
    global paises
    # Diccionario con relacion Continente - Cantidad de paises
    conteo = {} 

    #Recorro la lista global de paises
    for pais in paises:
        #Almaceno en una variable los nombres de los continentes
        nombre_continente = pais["continente"]
        
        #Si ya esta dentro del diccionario conteo, le suma 1
        if nombre_continente in conteo:
            conteo[nombre_continente] += 1
        else:
            #Si no esta en el diccionario, lo inicializa con 1
            conteo[nombre_continente] = 1
            
    
    #Los devuelvo en forma de lista para despues poder mostrarlos por pantalla con un for
    continentes_unicos = list(conteo.keys())
    cantidades = list(conteo.values())
    
    return continentes_unicos, cantidades
    
    
paises = obtener_paises(NOMBRE_ARCHIVO)
#actualizar_pais()
#busqueda()

promedio = promedio_superficie()
print(f"El promedio de la superficie entre los paises es de: {promedio}")

continentes, cantidad = paises_continentes()
for i in range(len(continentes)):
    print(f"Continente: {continentes[i]} | Cantidad de paises: {cantidad[i]}")
#paises[0]["nombre"] = "Brasil"
#print(paises[0]["nombre"])
#actualizar_archivo(NOMBRE_ARCHIVO, paises, CAMPOS)
