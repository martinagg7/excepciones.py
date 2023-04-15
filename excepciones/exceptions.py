import csv
import re

#corrreos que se encuentran en la base de datos
def correos_verificados():
    with open('base_datos/correos.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        lista_personas_base_datos = []
        # Itera sobre el objeto csv.reader y crea un diccionario para cada fila
        for fila in lector_csv:
            persona = {'correo': fila[0], 'nombre': fila[1]}
            lista_personas_base_datos.append(persona)
            
    print(lista_personas_base_datos)
    return lista_personas_base_datos
#ahora vamos a definir dos tipos de errores
class ErrorformatoCorreo(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
class Errorciberataque(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

#funcion para comprobar si el formato del correo es adecuado y esta en la base de datos
def main():
    lista_personas_base_datos = correos_verificados()
    print("Bienvenido,intruduzca su correo a continuacion...")
    correo=input("-->")
    try:
        if correo=="":
                print("es una entrada incorrecta.Introduzca una dirección de correo electrónico")
        elif  not re.search(".+@.+..+", correo):
                    raise ErrorformatoCorreo("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
        else:
            for persona in lista_personas_base_datos:
                if persona['correo']==correo:
                    print("Bienvenido",persona['nombre'])
                    break
    except ErrorformatoCorreo :
        print("Una dirección de correo electrónico debe tener el formato xxx@.xx")
    except Errorciberataque:
        print("Error de ciberataque")

if __name__ == "__main__":
    main()


        
    
