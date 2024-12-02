import string
import random

#Set the password length
longitud = int(input("Ingrese el tamaño de la contraseña:"))

#Generate the characters to use in the password
caracteres = string.ascii_letters + string.digits + string.punctuation

#Randomly generate the password with the specified length
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

#Print the password
print("La contraseña generada es: " + contrasena)
