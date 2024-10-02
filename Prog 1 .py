#Escriba un programa para verificar si un caracter es una letra del alfabeto o no.
def es_letra(caracter):
    # Verificar si el caracter es una letra
    return caracter.isalpha()

# Solicitar al usuario que ingrese un carácter
caracter = input("Ingrese un carácter: ")

# Asegurarse de que el usuario ingresó solo un carácter
if len(caracter) != 1:
    print("Por favor, ingrese solo un carácter.")
else:
    # Verificar si el carácter es una letra
    if es_letra(caracter):
        print(f"'{caracter}' es una letra del alfabeto.")
    else:
        print(f"'{caracter}' no es una letra del alfabeto.")
