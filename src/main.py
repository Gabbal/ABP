from utilidades import limpiar_consola, pausar

from gestion_dispositivos import (
    agregar_dispositivo,
    listar_dispositivos,
    buscar_dispositivo,
    eliminar_dispositivo
)
from automatizaciones import (
    agregar_automatizacion,
    listar_automatizaciones,
    eliminar_automatizacion
)

dispositivos = {}
automatizaciones = []

def menu_principal():
    while True:
        limpiar_consola()
        print("\033[94m🏠 Menú Principal - SmartHome\033[0m")
        print("\n\033[96m1. Gestionar Dispositivos\033[0m")
        print("\033[96m2. Gestionar Automatizaciones\033[0m")
        print("\033[96m3. Salir\033[0m")
        opcion = input("\nSeleccionar opción: ")

        if opcion == "1":
            menu_dispositivos()
        elif opcion == "2":
            menu_automatizaciones()
        elif opcion == "3":
            limpiar_consola()
            print("\n\033[92m¡Hasta luego!\033[0m\n")
            break
        else:
            print("\033[91mOpción inválida.\033[0m")


def menu_dispositivos():
    while True:
        limpiar_consola()
        print("\033[94m📱 Gestión de Dispositivos\033[0m")
        print("\n\033[96m1. Agregar dispositivo\033[0m")
        print("\033[96m2. Listar dispositivos\033[0m")
        print("\033[96m3. Buscar dispositivo\033[0m")
        print("\033[96m4. Eliminar dispositivo\033[0m")
        print("\033[96m5. Volver\033[0m")
        opcion = input("\nSeleccionar opción: ")
        limpiar_consola()

        if opcion == "1":
            dispositivo_id = input("\033[93mID del dispositivo: \033[0m")
            nombre = input("\033[93mNombre: \033[0m")
            tipo = input("\033[93mTipo (luz, cámara, etc.): \033[0m")
            estado = input("\033[93mEstado (encendido/apagado): \033[0m")
            limpiar_consola()
            agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo, estado)
        elif opcion == "2":
            listar_dispositivos(dispositivos)
        elif opcion == "3":
            dispositivo_id = input("\033[93mID del dispositivo a buscar: \033[0m")
            limpiar_consola()
            buscar_dispositivo(dispositivos, dispositivo_id)
        elif opcion == "4":
            dispositivo_id = input("\033[93mID del dispositivo a eliminar: \033[0m")
            limpiar_consola()
            eliminar_dispositivo(dispositivos, dispositivo_id)
        elif opcion == "5":
            break
        else:
            print("\033[91mOpción inválida.\033[0m")
        pausar()


def menu_automatizaciones():
    while True:
        limpiar_consola()
        print("\033[94m⏰ Gestión de Automatizaciones\033[0m")
        print("\n\033[96m1. Agregar automatización\033[0m")
        print("\033[96m2. Listar automatizaciones\033[0m")
        print("\033[96m3. Eliminar automatización\033[0m")
        print("\033[96m4. Volver\033[0m")
        opcion = input("\nSeleccionar opción: ")
        limpiar_consola()

        if opcion == "1":
            dispositivo_id = input("\033[93mID del dispositivo a automatizar: \033[0m")
            accion = input("\033[93mAcción (encender/apagar): \033[0m")
            hora = input("\033[93mHora programada (HH:MM): \033[0m")
            limpiar_consola()
            agregar_automatizacion(automatizaciones, dispositivo_id, accion, hora)
        elif opcion == "2":
            listar_automatizaciones(automatizaciones)
        elif opcion == "3":
            listar_automatizaciones(automatizaciones)
            try:
                indice = int(input("\n\033[93mNúmero de automatización a eliminar (empezando desde 1): \033[0m")) - 1
                limpiar_consola()
                eliminar_automatizacion(automatizaciones, indice)
            except ValueError:
                print("\033[91m❌ Ingrese un número válido.\033[0m")
        elif opcion == "4":
            break
        else:
            print("\033[91mOpción inválida.\033[0m")
        pausar()


if __name__ == "__main__":
    menu_principal()
