import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

##caracteres = "+-/[]*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(caracteres)
    return password

print("Bienvenido al generador de contraseñas.")
print("Esta aplicación generará una contraseña aleatoria para usted.")

print("  ")
length_buscar = int(input("Ingrese la longitud de la contraseña que desea generar: "))

if length_buscar <= 7:
    print("La contraseña debe tener al menos 8 caracteres para hcerla injakeable!. Intenta denuevo.")
    exit(0)

print(generate_password(length_buscar))