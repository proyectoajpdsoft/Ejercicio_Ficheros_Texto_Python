# Nombre del fichero donde se almacenará la información
rutaFichero = "clientes.txt"
# Nombre de los campos
caNombre = "Nombre:"
caApellido1 = "Apellido1:"
caApellido2 = "Apellido2:"
caEdad = "Edad:"

# Pedimos los datos al usuario
nombre = input("Introduzca el nombre: ")
apellido1 = input("Introduzca el primer apellido: ")
apellido2 = input("Introduzca el segundo apellido: ")
edad = input("Introduzca la edad: ")

# Guardamos los datos formateados (con tabulador) en una variable
valorGuardar = f"{caNombre:18}{nombre}\n{caApellido1:18}{apellido1}\n{caApellido2:18}{apellido2}\n{caEdad:18}{edad}"
# Guardamos los datos formateados en fichero, con apertura "a" para añadir al final del fichero
# Usamos la codificación utf-8 que nos permitirá usar tildes, eñes y demás
try:
    with open(rutaFichero, "a", encoding="utf-8") as fichero:    
        fichero.write(valorGuardar)
        # Agregamos un salto de línea final
        fichero.write("\n")
except Exception as e:
    print(f"Error al abrir el fichero: {e}")
finally:
    # Cerramos el fichero
    fichero.close

# Abrimos el fichero en modo lectura
# Y mostramos su contenido
try:
    # Método de lectura con readlines()
    # with open(rutaFichero, "r", encoding="utf-8") as fichero:        
    #    contenidoFichero = fichero.readlines()
    
    # Método de lectura recorriendo cada línea
    fichero = open(rutaFichero, mode="r", encoding="utf-8")
    # Recorremos cada línea del fichero y la vamos mostrando en consola
    print(f"El contenido del fichero {rutaFichero} es:")
    for linea in fichero:
        print(linea, end="")
except Exception as e:
    print(f"Error al abrir el fichero: {e}")
finally:
    # Cerramos el fichero
    fichero.close