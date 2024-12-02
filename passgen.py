import string
import random

#Establece la longitud de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña:"))

#Genera los caracteres para usar en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

#Genera aleatoriamente la contraseña con la logitud especificada
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

#Imprime la contraseña
print("La contraseña generada es: " + contrasena)