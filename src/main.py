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










def menu_automatizaciones(dispositivos):
    """Menú de automatizaciones."""
    while True:
        limpiar_consola()
        print("\033[94m⏰ Automatizaciones\033[0m")
        print("\n\033[96m1. Ejecutar automatización nocturna\033[0m")
        print("\033[96m2. Ver estado de automatizaciones\033[0m")
        print("\033[96m3. Listar dispositivos automatizados\033[0m")
        print("\033[96m4. Desactivar automatización específica\033[0m")
        print("\033[96m5. Desactivar todas las automatizaciones\033[0m")
        print("\033[96m6. Volver\033[0m")
        
        opcion = input("\nSeleccionar opción: ").strip()

        if opcion == "1":
            limpiar_consola()
            ejecutar_automatizacion_nocturna(dispositivos)
            
        elif opcion == "2":
            limpiar_consola()
            mostrar_estado_automatizacion(dispositivos)
            
        elif opcion == "3":
            limpiar_consola()
            listar_dispositivos_automatizados(dispositivos)
            
        elif opcion == "4":
            # Primero mostrar dispositivos automatizados
            limpiar_consola()
            listar_dispositivos_automatizados(dispositivos)
            
            # Si hay dispositivos automatizados, permitir seleccionar uno
            dispositivos_auto = {k: v for k, v in dispositivos.items() if v.get("automatizado", False)}
            if dispositivos_auto:
                print("\n" + "="*50)
                dispositivo_id = input("\033[93mID del dispositivo para desactivar automatización: \033[0m").strip()
                limpiar_consola()
                ejecutar_automatizacion(dispositivos, dispositivo_id, "desactivar")
            
        elif opcion == "5":
            limpiar_consola()
            desactivar_todas_automatizaciones(dispositivos)
            
        elif opcion == "6":
            break
        else:
            limpiar_consola()
            print("\033[91m❌ Opción inválida.\033[0m")
        
        if opcion != "6":
            pausar()

if __name__ == "__main__":
    menu_principal()
