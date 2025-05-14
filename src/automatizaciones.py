def agregar_automatizacion(automatizaciones, dispositivo_id, accion, hora):
    automatizacion = {
        "dispositivo_id": dispositivo_id,
        "accion": accion,
        "hora": hora
    }
    automatizaciones.append(automatizacion)
    print("\033[92m✅ Automatización registrada correctamente.\033[0m")


def listar_automatizaciones(automatizaciones):
    if not automatizaciones:
        print("\033[91mNo hay automatizaciones registradas.\033[0m")
        return
    for idx, auto in enumerate(automatizaciones, start=1):
        print(f"\033[93mAutomatización {idx}:\033[0m")
        print(f"\n  \033[93mDispositivo ID:\033[0m {auto['dispositivo_id']}")
        print(f"  \033[93mAcción:\033[0m {auto['accion']}")
        print(f"  \033[93mHora:\033[0m {auto['hora']}")


def eliminar_automatizacion(automatizaciones, indice):
    if 0 <= indice < len(automatizaciones):
        eliminada = automatizaciones.pop(indice)
        print(f"\033[92m✅ Automatización para dispositivo '{eliminada['dispositivo_id']}' eliminada.\033[0m")
    else:
        print("\033[91m❌ Índice inválido.\033[0m")
