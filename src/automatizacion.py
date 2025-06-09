from utilidades import pausar

def cargar_automatizacion_predefinida():
    """
    Devuelve una automatización predefinida como lista con un único diccionario.
    """
    automatizacion = {
        "nombre": "Encender luces del patio a las 19hs",
        "hora": "19:00",
        "dispositivo": "luces_patio",
        "accion": 0  # Inicialmente apagada
    }
    return [automatizacion]


def activar_automatizacion(automatizaciones, dispositivos):
    automatizacion = automatizaciones[0]
    estado = "Encendida" if automatizacion["accion"] == 1 else "Apagada"

    print("\n--- Automatización Predefinida ---")
    print(f"Nombre: {automatizacion['nombre']}")
    print(f"Hora programada: {automatizacion['hora']}")
    print(f"Estado actual: {estado}")

    print("\n1. Encender automatización")
    print("0. Regresar")

    opcion = input("Seleccioná una opción: ")
    if opcion == "1":
        automatizacion["accion"] = 1
        dispositivo = automatizacion["dispositivo"]
        if dispositivo in dispositivos:
            dispositivos[dispositivo]["estado"] = "encendido"
            print(f"✅ Automatización activada. '{dispositivo}' encendido.")
        else:
            print(f"⚠️ El dispositivo '{dispositivo}' no está registrado. Se activó la automatización, pero no se pudo encender el dispositivo.")
            pausar()
    elif opcion == "0":
        print("Volviendo al menú...")
        pausar()
    else:
        print("❌ Opción inválida.")
        pausar()
