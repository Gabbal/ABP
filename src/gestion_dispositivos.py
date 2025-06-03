def agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo):
    """Agrega un nuevo dispositivo al sistema."""
    if dispositivo_id in dispositivos:
        print("\033[91m⚠️ El ID ya está en uso.\033[0m")
        return
    
    if not dispositivo_id.strip() or not nombre.strip() or not tipo.strip():
        print("\033[91m❌ Todos los campos son obligatorios.\033[0m")
        return
    
    dispositivos[dispositivo_id] = {
        "nombre": nombre.strip(),
        "tipo": tipo.strip(),
        "estado": "apagado",
        "automatizado": False,
        "automatizacion_activa": {}
    }
    print("\n\033[92m✅ Dispositivo agregado correctamente.\033[0m")

def listar_dispositivos(dispositivos):
    """Muestra todos los dispositivos registrados."""
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    
    print("\033[96m📋 Lista de dispositivos:\033[0m")
    for device_id, device in dispositivos.items():
        estado_icono = "🟢" if device["estado"] == "encendido" else "🔴"
        
        print(f"\n{estado_icono} ID: {device_id}")
        print(f"   Nombre: {device['nombre']}")
        print(f"   Tipo: {device['tipo']}")
        print(f"   Estado: {device['estado']}")
        
        # Mostrar información de automatización
        if device.get("automatizado", False):
            automatizacion = device.get("automatizacion_activa", {})
            if automatizacion:
                nombre_auto = automatizacion.get("nombre", "Desconocida")
                descripcion = automatizacion.get("descripcion", "")
                print(f"   🤖 Automatización: {nombre_auto}")
                if descripcion:
                    print(f"   ⏰ {descripcion}")
        else:
            print(f"   👤 Control: Manual")

def buscar_dispositivo(dispositivos, dispositivo_id):
    """Busca y muestra un dispositivo específico."""
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return
    
    device = dispositivos[dispositivo_id]
    estado_icono = "🟢" if device["estado"] == "encendido" else "🔴"
    
    print(f"\033[93mDispositivo encontrado (ID: {dispositivo_id}):\033[0m\n")
    print(f"   {estado_icono} Nombre: {device['nombre']}")
    print(f"   🏷️  Tipo: {device['tipo']}")
    print(f"   ⚡ Estado: {device['estado']}")
    
    # Mostrar información de automatización
    if device.get("automatizado", False):
        automatizacion = device.get("automatizacion_activa", {})
        if automatizacion:
            nombre_auto = automatizacion.get("nombre", "Desconocida")
            descripcion = automatizacion.get("descripcion", "")
            print(f"   🤖 Automatización: {nombre_auto}")
            if descripcion:
                print(f"   ⏰ {descripcion}")
    else:
        print(f"   👤 Control: Manual")

def eliminar_dispositivo(dispositivos, dispositivo_id):
    """Elimina un dispositivo del sistema."""
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return
    
    nombre_dispositivo = dispositivos[dispositivo_id]["nombre"]
    del dispositivos[dispositivo_id]
    print(f"\033[92m✅ Dispositivo '{nombre_dispositivo}' eliminado.\033[0m")

def cambiar_estado_dispositivo(dispositivos, dispositivo_id, nuevo_estado):
    """Cambia el estado de un dispositivo específico."""
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return False
    
    if nuevo_estado == "encender":
        dispositivos[dispositivo_id]["estado"] = "encendido"
        dispositivos[dispositivo_id]["automatizado"] = False  # Control manual
        dispositivos[dispositivo_id]["automatizacion_activa"] = {}  # Limpiar automatización
        print(f"\033[92m✅ {dispositivos[dispositivo_id]['nombre']} encendido manualmente.\033[0m")
        return True
    elif nuevo_estado == "apagar":
        dispositivos[dispositivo_id]["estado"] = "apagado"
        dispositivos[dispositivo_id]["automatizado"] = False  # Control manual
        dispositivos[dispositivo_id]["automatizacion_activa"] = {}  # Limpiar automatización
        print(f"\033[94m✅ {dispositivos[dispositivo_id]['nombre']} apagado manualmente.\033[0m")
        return True
    else:
        print("\033[91m❌ Estado no válido. Use 'encender' o 'apagar'.\033[0m")
        return False