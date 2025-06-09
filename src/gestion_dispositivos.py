def agregar_dispositivo(dispositivos, dispositivo_id, nombre, tipo):
    """Agrega un nuevo dispositivo al sistema."""
    dispositivo_id = dispositivo_id.strip()
    nombre = nombre.strip()
    tipo = tipo.strip()

    if dispositivo_id in dispositivos:
        print("\033[91m⚠️ El ID ya está en uso.\033[0m")
        return
    
    if not dispositivo_id or not nombre or not tipo:
        print("\033[91m❌ Todos los campos son obligatorios.\033[0m")
        return
    
    dispositivos[dispositivo_id] = {
        "nombre": nombre,
        "tipo": tipo,
        "estado": "encendido",
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
    for device_id in sorted(dispositivos.keys()):
        device = dispositivos[device_id]
        estado_icono = "🟢" if device["estado"] == "encendido" else "🔴"
        
        print(f"\n{estado_icono} ID: {device_id}")
        print(f"   Nombre: {device['nombre']}")
        print(f"   Tipo: {device['tipo']}")
        print(f"   Estado: {device['estado']}")
        
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
    dispositivo_id = dispositivo_id.strip()
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return
    
    device = dispositivos[dispositivo_id]
    estado_icono = "🟢" if device["estado"] == "encendido" else "🔴"
    
    print(f"\033[93mDispositivo encontrado (ID: {dispositivo_id}):\033[0m\n")
    print(f"   {estado_icono} Nombre: {device['nombre']}")
    print(f"   🏷️  Tipo: {device['tipo']}")
    print(f"   ⚡ Estado: {device['estado']}")
    
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
    dispositivo_id = dispositivo_id.strip()
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return
    
    nombre_dispositivo = dispositivos[dispositivo_id]["nombre"]
    del dispositivos[dispositivo_id]
    print(f"\033[92m✅ Dispositivo '{nombre_dispositivo}' eliminado.\033[0m")
