import csv
import re

NOMBRE_ARCHIVO = "paises.csv"
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
            valor_busqueda = input("Ingrese el valor del continente a buscar: ").title()
            while not validar_inputs(valor_busqueda):
                print("Valor de continente invalido, por favor ingrese un valor correcto.")
                valor_busqueda = input("Ingrese el valor del continente a buscar: ").title()
              
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
    
def promedios(opcion):
    """Devuelve el promedio de la poblacion o superficie entre paises."""
    global paises
    acu = 0
    count = 0
    
    #Si la opcion es 1, busca el promedio de la superficie, si es 2 busca el promedio de la poblacion
    if opcion == 1:
        for pais in paises:
            acu += pais["superficie"]
            count += 1
    elif opcion == 2:
        for pais in paises:
            acu += pais["poblacion"]
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

def paises_max_min():
    global paises
    
    max = 0
    nombre_max = ""
    min = 999999999
    nombre_min = ""
    
    
    #Hago los for por separado para que no se pisen en la primera iteracion
    
    #Recorro la lista de paises en busqueda del pais con mayor poblacion
    for pais in paises: 
        if pais["poblacion"] > max:
            max = pais["poblacion"]
            nombre_max = pais["nombre"]
            
    #Recorro la lista de paises en busqueda del pais con menor poblacion
    for pais in paises:
        if pais["poblacion"] < min:
            min = pais["poblacion"]
            nombre_min = pais["nombre"]
       
    #devuelvo los resultados     
    return nombre_max, nombre_min

    
            
def estadisticas():
    """Submenu de estadisticas"""
    try:
        global paises
        print("------------ Estadisticas ------------")
        print(f"Que estadistica desea consultar?")
        print("1. Pais con mayor y Pais con menor poblacion\n2. Promedio de poblacion entre paises\n3. Promedio de superficie entre paises\n4. Cantidad de paises por continente")
        opcion = int(input("Seleccione una opcion: "))
    
        if opcion == 1:
            pais_max, pais_min = paises_max_min()
            print(f"El pais con mayor poblacion es: {pais_max}")
            print(f"El pais con menor poblacion es: {pais_min}")
                
        elif opcion == 2:
            pobl_promedio = promedios(2)
            print(f"El promedio de la superficie entre paises es de: {pobl_promedio}")
            

        elif opcion == 3:
            sup_promedio = promedios(1)
            print(f"El promedio de la superficie entre paises es de: {sup_promedio} kms")
            


        elif opcion == 4:
            keys_continente, cant_paises = paises_continentes()
            for i in range(len(cant_paises)):
                print(f"Continente: {keys_continente[i]} | Cantidad Paises: {cant_paises[i]}")
              
        else:
            print("Valor de opcion incorrecta, intente nuevamente")
        
    except ValueError:
        print("Valor de opcion incorrecto, por favor intenta nuevamente.")
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    

def alta_pais():
    global paises
    
    nombre_nuevo = input("Ingrese el nombre del pais a ingresar: ").title()
    
    while not validar_inputs(nombre_nuevo) or buscar_pais(nombre_nuevo,1)[0]:
        print("Valor de nombre ingresado invalido o duplicado, por favor ingrese un valor valido")
        nombre_nuevo = input("Ingrese el nombre del pais a ingresar: ").title()
    
    poblacion = input(f"Ingrese la poblacion del pais {nombre_nuevo}: ")
    
    while not validar_inputs(poblacion,1) or int(poblacion) <= 0:
        print("Valor de poblacion incorrecto, por favor ingrese un numero entero positivo mayor a 3 digitos.")
        poblacion = input(f"Ingrese la poblacion del pais {nombre_nuevo}: ")
        
    superficie = input(f"Ingrese la superficie del pais {nombre_nuevo}: ")
    
    while not validar_inputs(superficie,1) or int(superficie) <= 0:
        print("Valor de poblacion incorrecto, por favor ingrese un numero entero positivo mayor a 3 digitos.")
        superficie = input(f"Ingrese la superficie del pais {nombre_nuevo}: ")
        
    continente = input(f"Ingrese el continente del pais {nombre_nuevo}: ").title()
    
    while not validar_inputs(continente):
        print("Valor de nombre ingresado invalido, por favor ingrese un valor valido")
        continente = input(f"Ingrese el continente del pais {nombre_nuevo}: ").title()
        
    poblacion, superficie = int(poblacion), int(superficie)
    
    mi_dict = {
        "nombre": nombre_nuevo,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(mi_dict)
    
    actualizar_archivo(NOMBRE_ARCHIVO, paises, CAMPOS)
    
    
        


while True:
    paises = obtener_paises(NOMBRE_ARCHIVO)
    try:
        #Muestro por pantalla las opciones del menu
        print("1) Agregar pais a la lista \n2) Actualizar info de pais \n3) Informacion de paises \n4) Estadisticas \n5) Salir")
        
        #Le pido al usuario que ingrese la opcion deseada y lo parseo como
        opcion = int(input("Ingrese la opcion deseada: "))
            
        
        if opcion == 1:
            alta_pais()
        
        elif opcion == 2:
            #Si el inventario no esta vacio, ejecuto la funcion. Si lo esta, le indico al usuario que use la opcion 1.
            if len(paises) > 0:
                print()
                actualizar_pais()
                print()
            else:
                print("La lista de paises esta vacia, debe usar la opcion 1 para agregar un pais.")
        
        elif opcion == 3:
            if len(paises) > 0:
                print()
                busqueda()
                print()
            else:
                print("La lista de paises esta vacia, debe usar la opcion 1 para agregar un pais.")


        elif opcion == 4:
            if len(paises) > 0:
                print()
                estadisticas()
                print()
            else:
                print("La lista de paises esta vacia, debe usar la opcion 1 para agregar un pais.")
            
        elif opcion == 5:
            break
        
        #Si el usuario pone una opcion menor o igual a 0 o mayor a 7, levanta un ValueError
        elif opcion <= 0 or opcion > 5:
            raise ValueError
        
    except ValueError:
        print(f"Por favor ingrese una opcion valida entre 1 y 7.")