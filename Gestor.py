import argparse

# Diccionario de gestor de contraseñas
gestor_contraseñas = {
    "Outlook": ["alejandrorubiofranco@hotmail.com", "12345678"],
    "Facebook": ["Alejandro Rubio", "87654321"],
    "Twitter": ["AlejandroRubio", "87654321"],
    "Github": ["Alex-RubioDev", "45677898765"],
    "Linkedin": ["Alejandrorubiofranco@hotmail.com", "123456789"]
}

# Funciones del gestor de contraseñas
def ver_todas(diccionario):
    for cuenta, detalles in diccionario.items():
        usuario, contraseña = detalles
        print(f"Cuenta: {cuenta}")
        print(f"  Usuario: {usuario}")
        print(f"  Contraseña: {contraseña}")

def obtener_contraseña(diccionario, cuenta):
    detalles = diccionario.get(cuenta)
    if detalles:
        usuario, contraseña = detalles
        print(f"Cuenta: {cuenta}  Usuario: {usuario}  Contraseña: {contraseña}")
    else:
        print("No se ha encontrado")

def actualizar_contraseña(diccionario, cuenta):
    detalles = diccionario.get(cuenta)
    if detalles:
        nuevaContraseña = input(f"Dime la nueva contraseña para {cuenta}: ")
        diccionario[cuenta][1] = nuevaContraseña
        print("Has actualizado la contraseña")
    else:
        print("No se ha encontrado la cuenta")

def agregar_contraseña(diccionario, cuenta, usuario, contraseña):
    if cuenta not in diccionario:
        diccionario[cuenta] = [usuario, contraseña]
        print(f"Se ha agregado la cuenta {cuenta} correctamente.")
    else:
        print(f"La cuenta {cuenta} ya existe en el gestor de contraseñas.")

def eliminar_contraseña(diccionario, cuenta):
    if cuenta in diccionario:
        del diccionario[cuenta]
        print(f"Se ha eliminado {cuenta}")
    else:
        print(f"No se ha encontrado la cuenta")

# Función principal para manejar los comandos desde el cmd
def main():
    parser = argparse.ArgumentParser(description="Gestor de Contraseñas")
    parser.add_argument("accion", choices=["ver_todas", "obtener_contraseña", "actualizar_contraseña",
                                           "agregar_contraseña", "eliminar_contraseña"],
                        help="Acción a realizar")
    parser.add_argument("--cuenta", help="Nombre de la cuenta")
    parser.add_argument("--usuario", help="Nombre de usuario")
    parser.add_argument("--contraseña", help="Contraseña")

    args = parser.parse_args()

    if args.accion == "ver_todas":
        ver_todas(gestor_contraseñas)
    elif args.accion == "obtener_contraseña" and args.cuenta:
        obtener_contraseña(gestor_contraseñas, args.cuenta)
    elif args.accion == "actualizar_contraseña" and args.cuenta:
        actualizar_contraseña(gestor_contraseñas, args.cuenta)
    elif args.accion == "agregar_contraseña" and args.cuenta and args.usuario and args.contraseña:
        agregar_contraseña(gestor_contraseñas, args.cuenta, args.usuario, args.contraseña)
    elif args.accion == "eliminar_contraseña" and args.cuenta:
        eliminar_contraseña(gestor_contraseñas, args.cuenta)
    else:
        print("Acción no reconocida o faltan argumentos")

if __name__ == "__main__":
    main()
