# Serpino_Trabajo_Pracito_Integrador
Trabajo Practico Integrador Gonzalo Serpino 

# Gestor de Países en Python 🌎

Este es un programa simple de consola (terminal) que permite gestionar una lista de países, guardando la información de forma automática en un archivo CSV (`paises.csv`).

## 🚀 Cómo ejecutar el programa

Para correr este programa en tu computadora, sigue estos sencillos pasos:

1. Asegúrate de tener Python instalado en tu computadora.
2. Descarga o clona este repositorio en tu equipo.
3. Abre una terminal (o la consola de tu editor de código, como VS Code) y navega hasta la carpeta donde guardaste los archivos.
4. Ejecuta el siguiente comando en la terminal: python main.py

## 📖 Cómo usar el menú (Inputs y Salidas esperadas)
Al ejecutar el programa, verás un menú con 5 opciones. Solo debes ingresar el número de la opción y presionar Enter.

1) Agregar país a la lista

Inputs aceptados: * Nombre y Continente: Solo letras (ej. Argentina, America). Tiene que ser de un minimo de 3 caracteres hasta 50 caracteres.

Población y Superficie: Solo números enteros, sin puntos ni comas (ej. 45376763). Tiene que ser de un minimo de 3 digitos hasta 50 digitos.

Salida esperada: El programa guarda el país en el archivo paises.csv y vuelve al menú principal. Si ingresas un dato inválido o un país que ya existe, te pedirá que lo ingreses de nuevo.

2) Actualizar info de país

Inputs aceptados: El nombre exacto de un país que ya esté guardado. Luego, te preguntará qué dato específico quieres cambiar (1 a 4) y te pedirá el nuevo valor.

Salida esperada: Se sobrescribe la información de ese país en el archivo paises.csv.

3) Información de países (Búsqueda)

Inputs aceptados: Puedes buscar por Nombre, Población, Superficie o Continente.

Salida esperada: El programa imprimirá en la pantalla los datos del país (o los países) que coincidan con tu búsqueda.

4) Estadísticas

Salida esperada: Mostrará cálculos automáticos basados en los datos guardados (como el promedio de superficie o la cantidad de países por continente).

5) Salir

Cierra el programa de forma segura.