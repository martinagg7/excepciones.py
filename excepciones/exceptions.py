import re
import csv

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
class ciber_ataque(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
class FormatoCorreroInvalido(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje

def verificar_correo(correo):
    if not re.search(".+@.+\..+", correo):
        mensaje= "El correo no tiene el formato correcto"
        raise FormatoCorreroInvalido(mensaje)
    else:
        print("Verificando si esta en la base de datos")
        lista_personas_base_datos = correos_verificados()
        for persona in lista_personas_base_datos:
            if persona['correo'] == correo:
                print("Bienvenido"+persona['nombre'])
            else:
                mensaje_2="Alerta de ciber ataque"
                raise ciber_ataque(mensaje_2)

def main ():
    print("Bienvenido al sistema de verificacion de correo")
    correo=input("-->")
    verificar_correo(correo)

