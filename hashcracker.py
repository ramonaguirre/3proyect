import hashlib

hash_file = "3dff73672811dcd9f93f3dd86ce4e04960b46e10827a55418c7cc35d596e9662"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, 'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:
            print("La contraseña original es: " + password)
            break
        else:
            print("La contraseña no se encuentra en el diccionario: ")
