import string
from tokenize import String

def Encriptar(contraseña, clave):

    Encriptado = ""

    for c in contraseña:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            c_cambiada = (c_index + clave)  + ord('A')

            c_new = chr(c_cambiada)

            Encriptado += c_new

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_cambiada = (c_index + clave) + ord('a')

            c_new = chr(c_cambiada)

            Encriptado += c_new

        elif c.isdigit():

            c_new = (int(c) + clave)

            Encriptado += str(c_new)

        else:

            Encriptado += c
    
    print("Contraseña Encriptada: ",Encriptado)

    return Encriptado

def opcioncontraseña():
    contraseña = input()
    contraseña = list(contraseña)
    return contraseña

def menu():
	print ("\t1 - Encriptar")
	
 
while True:
	menu()
 
	opcionMenu = input("Opciones\n>")
 
	if opcionMenu=="1": 
		print("Elegiste Encriptar...\n Escribe tu contraseña: "), Encriptar(opcioncontraseña(), 4)
	