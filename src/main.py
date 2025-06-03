from utilidades import limpiar_consola, pausar
from gestion_dispositivos import (
    agregar_dispositivo,
    listar_dispositivos,
    buscar_dispositivo,
    eliminar_dispositivo,
    cambiar_estado_dispositivo
)
from automatizaciones import (
    ejecutar_automatizacion_nocturna,
    ejecutar_automatizacion,
    mostrar_estado_automatizacion,
    listar_dispositivos_automatizados,
    desactivar_todas_automatizaciones
)

def menu_principal():
    """Menú principal del sistema."""
    dispositivos = {}
    
    while True:
        limpiar_consola()
        print("\033[94m🏠 Sistema SmartHome\033[0m")
        print("\n\033[96m1. Gestionar Dispositivos\033[0m")
        print("\033[96m2. Automatizaciones\033[0m")
        print("\033[96m3. Salir\033[0m")
        
        opcion = input("\nSeleccionar opción: ").strip()

        if opcion == "1":
            menu_dispositivos(dispositivos)
        elif opcion == "2":
            menu_automatizaciones(dispositivos)
        elif opcion == "3":
            limpiar_consola()
            print("\n\033[92m¡Hasta luego! 👋\033[0m\n")
            break
        else:
            limpiar_consola()
            print("\033[91m❌ Opción inválida.\033[0m")
            pausar()

def menu_dispositivos(dispositivos):
    """Menú de gestión de dispositivos."""
    while True:
        limpiar_consola()
        print("\033[94m📱 Gestión de Dispositivos\033[0m")
        print("\n\033[96m1. Agregar dispositivo\033[0m")
        print("\033[96m2. Listar dispositivos\033[0m")
        print("\033[96m3. Buscar dispositivo\033[0m")
        print("\033[96m4. Eliminar dispositivo\033[0m")
        print("\033[96m5. Cambiar estado de un dispositivo\033[0m")
        print("\033[96m6. Volver\033[0m")
        
        opcion = input("\nSeleccionar opción: ").strip()
        
        if opcion == "1":
            dispositivo_id = input("\033[93mID del dispositivo: \033[0m").strip()
            nombre = input("\033[93mNombre: \033[0m").strip()
            tipo = input("\033[93mTipo (luz, cámara, etc.): \033[0m").strip()
            limpiar_consola()
            agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo)
            
        elif opcion == "2":
            limpiar_consola()
            listar_dispositivos(dispositivos)
            
        elif opcion == "3":
            dispositivo_id = input("\033[93mID del dispositivo a buscar: \033[0m").strip()
            limpiar_consola()
            buscar_dispositivo(dispositivos, dispositivo_id)
            
        elif opcion == "4":
            dispositivo_id = input("\033[93mID del dispositivo a eliminar: \033[0m").strip()
            limpiar_consola()
            eliminar_dispositivo(dispositivos, dispositivo_id)
            
        elif opcion == "5":
            dispositivo_id = input("\033[93mID del dispositivo: \033[0m").strip()
            
            if dispositivo_id in dispositivos:
                estado_actual = dispositivos[dispositivo_id]["estado"]
                nuevo_estado = input(f"\033[93mEstado actual: {estado_actual}. Nuevo estado (encender/apagar): \033[0m").strip().lower()
                limpiar_consola()
                cambiar_estado_dispositivo(dispositivos, dispositivo_id, nuevo_estado)
            else:
                limpiar_consola()
                print("\033[91m❌ Dispositivo no encontrado.\033[0m")
                
        elif opcion == "6":
            break
        else:
            limpiar_consola()
            print("\033[91m❌ Opción inválida.\033[0m")
        
        if opcion != "6":
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