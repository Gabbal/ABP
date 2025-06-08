from usuarios import registrar_usuario, iniciar_sesion, modificar_rol_usuario, consultar_datos_personales
from gestion_dispositivos import agregar_dispositivo, listar_dispositivos, buscar_dispositivo, eliminar_dispositivo
from automatizacion import cargar_automatizacion_predefinida, activar_automatizacion
from utilidades import limpiar_consola, pausar

usuarios = {}
dispositivos = {}
automatizaciones = cargar_automatizacion_predefinida()

def menu_principal():
    limpiar_consola()
    print("\033[93m==== SMART HOME SOLUTIONS ====\033[0m")
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("0. Salir")
    return input("\nSeleccioná una opción: ")

def menu_estandar(usuario):
    while True:
        limpiar_consola()
        print(f"\033[93m=== MENÚ ESTÁNDAR - Bienvenido {usuario['usuario']} ===\033[0m")
        print("\n1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("3. Automatización personalizada")
        print("0. Cerrar sesión")
        opcion = input("\nSeleccioná una opción: ")

        if opcion == "1":
            limpiar_consola()
            consultar_datos_personales(usuario)
            pausar()
        elif opcion == "2":
            limpiar_consola()
            listar_dispositivos(dispositivos)
            pausar()
        elif opcion == "3":
            limpiar_consola()
            activar_automatizacion(automatizaciones, dispositivos)
            pausar()
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción inválida.")
            pausar()

def menu_admin(usuario):
    while True:
        limpiar_consola()
        print(f"\033[93m=== MENÚ ADMIN - Bienvenido {usuario['usuario']} ===\033[0m")
        print("\n1. Consultar automatización predefinida")
        print("2. Gestionar dispositivos")
        print("3. Modificar rol de usuario")
        print("0. Cerrar sesión")
        opcion = input("\nSeleccioná una opción: ")

        if opcion == "1":
            limpiar_consola()
            print("\033[93m=== AUTOMATIZACIÓN PREDEFINIDA ===\033[0m\n")
            for a in automatizaciones:
                print(f"Dispositivo: {a['dispositivo']}")
                print(f"Hora: {a['hora']}")
                print(f"Estado: {'Encendida' if a['accion'] == 1 else 'Apagada'}\n")
            pausar()

        elif opcion == "2":
            while True:
                limpiar_consola()
                print("\033[93m=== GESTIÓN DE DISPOSITIVOS ===\033[0m")
                print("\n1. Agregar dispositivo")
                print("2. Listar dispositivos")
                print("3. Buscar dispositivo por ID")
                print("4. Eliminar dispositivo")
                print("0. Volver")
                subopcion = input("\nSeleccioná una opción: ")

                if subopcion == "1":
                    limpiar_consola()
                    dispositivo_id = input("ID del dispositivo: ").strip()
                    nombre = input("Nombre del dispositivo: ").strip()
                    tipo = input("Tipo de dispositivo: ").strip()
                    agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo)
                    pausar()

                elif subopcion == "2":
                    limpiar_consola()
                    listar_dispositivos(dispositivos)
                    pausar()

                elif subopcion == "3":
                    limpiar_consola()
                    dispositivo_id = input("ID del dispositivo a buscar: ").strip()
                    buscar_dispositivo(dispositivos, dispositivo_id)
                    pausar()

                elif subopcion == "4":
                    limpiar_consola()
                    dispositivo_id = input("ID del dispositivo a eliminar: ").strip()
                    eliminar_dispositivo(dispositivos, dispositivo_id)
                    pausar()

                elif subopcion == "0":
                    break

                else:
                    print("\n❌ Opción inválida.")
                    pausar()

        elif opcion == "3":
            limpiar_consola()
            modificar_rol_usuario(usuarios)
            pausar()

        elif opcion == "0":
            break

        else:
            print("\n❌ Opción inválida.")
            pausar()

def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":
            limpiar_consola()
            registrar_usuario(usuarios)
            pausar()
        elif opcion == "2":
            limpiar_consola()
            usuario = iniciar_sesion(usuarios)
            if usuario:
                if usuario["rol"] == "admin":
                    menu_admin(usuario)
                else:
                    menu_estandar(usuario)
        elif opcion == "0":
            print("\n👋 Gracias por usar Smart Home Solutions. ¡Hasta pronto!\n")
            break
        else:
            print("\n❌ Opción inválida.")
            pausar()

if __name__ == "__main__":
    main()
