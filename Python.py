
#!/usr/bin/env Python
# -*- coding: utf-8 -*-

texto = raw_input("Introduzca su texto: ")
x=0 #Cambiar valor dependiendo del subcriptograma deseado
cadena = ""
dirFichero = raw_input("Introduzca la ubicacion de su fichero: ")
longitudclave = raw_input("Introduzca la longitud de la clave: ")
fichero = open(dirFichero,'w')

while x<= len(texto):
    cadena = cadena + texto[x]
    x = x + longitudclave

fichero.write(cadena)
