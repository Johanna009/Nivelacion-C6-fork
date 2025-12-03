
def validar_contrasena(contrasena_usuario):
    contrasena_sistema = "admin123"
    
    if contrasena_usuario == contrasena_sistema:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta"

# Pedimos la contraseña al usuario
contrasena_usuario = input("Ingrese contraseña: ")

# Llamamos la función y mostramos el resultado
print(validar_contrasena(contrasena_usuario))  