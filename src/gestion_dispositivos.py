def agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo, estado):
    if dispositivo_id in dispositivos:
        print("\033[91m⚠️ El ID ya está en uso.\033[0m")
        return
    dispositivos[dispositivo_id] = {
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado
    }
    print("\n\033[92m✅ Dispositivo agregado correctamente.\033[0m")


def listar_dispositivos(dispositivos):
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    for id_dispositivo, datos in dispositivos.items():
        print(f"\n\033[93mID:\033[0m {id_dispositivo}\n")
        for clave, valor in datos.items():
            print(f"  \033[93m{clave.capitalize()}:\033[0m {valor}")


def buscar_dispositivo(dispositivos, dispositivo_id):
    dispositivo = dispositivos.get(dispositivo_id)
    if dispositivo:
        print(f"\033[93mDispositivo encontrado ({dispositivo_id}):\033[0m\n")
        for clave, valor in dispositivo.items():
            print(f"  \033[93m{clave.capitalize()}:\033[0m {valor}")
    else:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")


def eliminar_dispositivo(dispositivos, dispositivo_id):
    if dispositivo_id in dispositivos:
        del dispositivos[dispositivo_id]
        print("\033[92m✅ Dispositivo eliminado.\033[0m")
    else:
        print("\033[91m❌ No se encontró el dispositivo.\033[0m")
