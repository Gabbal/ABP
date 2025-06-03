def ejecutar_automatizacion_nocturna(dispositivos):
    """Ejecuta automatización nocturna - apaga luces y activa cámaras de seguridad."""
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    
    print("\033[94m🌙 Ejecutando automatización nocturna...\033[0m\n")
    
    dispositivos_afectados = 0
    
    for device_id, device in dispositivos.items():
        if device["tipo"].lower() in ["luz", "luces", "lampara", "iluminacion"]:
            # Apagar luces
            device["estado"] = "apagado"
            device["automatizado"] = True
            device["automatizacion_activa"] = {
                "nombre": "Modo Nocturno",
                "descripcion": "Luces apagadas automáticamente (22:00-06:00)"
            }
            print(f"🔴 {device['nombre']} - Apagada (Modo Nocturno)")
            dispositivos_afectados += 1
            
        elif device["tipo"].lower() in ["camara", "seguridad", "vigilancia"]:
            # Encender cámaras de seguridad
            device["estado"] = "encendido"
            device["automatizado"] = True
            device["automatizacion_activa"] = {
                "nombre": "Vigilancia Nocturna",
                "descripcion": "Cámara activada para seguridad nocturna"
            }
            print(f"🟢 {device['nombre']} - Activada (Vigilancia Nocturna)")
            dispositivos_afectados += 1
    
    if dispositivos_afectados > 0:
        print(f"\n\033[92m✅ Automatización nocturna completada.\033[0m")
        print(f"   {dispositivos_afectados} dispositivos configurados")
    else:
        print("\033[93m⚠️ No se encontraron dispositivos compatibles (luces/cámaras).\033[0m")

def ejecutar_automatizacion(dispositivos, dispositivo_id, accion):
    """Controla la automatización de un dispositivo específico."""
    if dispositivo_id not in dispositivos:
        print("\033[91m❌ Dispositivo no encontrado.\033[0m")
        return False
    
    device = dispositivos[dispositivo_id]
    nombre_dispositivo = device["nombre"]
    
    if accion == "desactivar":
        if not device.get("automatizado", False):
            print(f"\033[93m⚠️ {nombre_dispositivo} no tiene automatización activa.\033[0m")
            return False
        
        # Guardar info de automatización antes de desactivar
        automatizacion_previa = device.get("automatizacion_activa", {})
        
        device["automatizado"] = False
        device["automatizacion_activa"] = {}
        
        print(f"\033[92m✅ Automatización desactivada para {nombre_dispositivo}.\033[0m")
        print(f"   El dispositivo mantiene su estado actual: {device['estado']}")
        
        # Mostrar qué automatización se desactivó
        if automatizacion_previa:
            nombre_auto = automatizacion_previa.get("nombre", "Desconocida")
            print(f"   🤖 Se desactivó: {nombre_auto}")
        
        return True
    
    elif accion == "activar":
        if device.get("automatizado", False):
            print(f"\033[93m⚠️ {nombre_dispositivo} ya tiene automatización activa.\033[0m")
            return False
        
        print(f"\033[93m⚠️ Para activar automatización en {nombre_dispositivo}, use el menú de automatización.\033[0m")
        return False
    
    else:
        print("\033[91m❌ Acción no válida. Use 'activar' o 'desactivar'.\033[0m")
        return False

def mostrar_estado_automatizacion(dispositivos):
    """Muestra el estado de automatización de todos los dispositivos."""
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    
    print("\033[96m🤖 Estado de automatización:\033[0m")
    dispositivos_automatizados = 0
    
    for device_id, device in dispositivos.items():
        estado_auto = "🟢 Activa" if device.get("automatizado", False) else "🔴 Inactiva"
        control_tipo = "🤖 Automatizado" if device.get("automatizado", False) else "👤 Manual"
        
        print(f"\n📱 {device['nombre']} (ID: {device_id})")
        print(f"   Estado: {device['estado']}")
        print(f"   Automatización: {estado_auto}")
        print(f"   Control: {control_tipo}")
        
        # Si tiene automatización activa, mostrar detalles
        if device.get("automatizado", False):
            automatizacion = device.get("automatizacion_activa", {})
            if automatizacion:
                nombre_auto = automatizacion.get("nombre", "Desconocida")
                descripcion = automatizacion.get("descripcion", "")
                print(f"   📋 Regla: {nombre_auto}")
                if descripcion:
                    print(f"   ⏰ {descripcion}")
            dispositivos_automatizados += 1
    
    print(f"\n📊 Resumen: {dispositivos_automatizados}/{len(dispositivos)} dispositivos automatizados")

def listar_dispositivos_automatizados(dispositivos):
    """Muestra solo los dispositivos que tienen automatización activa."""
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    
    dispositivos_auto = {k: v for k, v in dispositivos.items() if v.get("automatizado", False)}
    
    if not dispositivos_auto:
        print("\033[93m⚠️ No hay dispositivos con automatización activa.\033[0m")
        return
    
    print("\033[96m🤖 Dispositivos automatizados:\033[0m")
    
    for device_id, device in dispositivos_auto.items():
        estado_icono = "🟢" if device["estado"] == "encendido" else "🔴"
        automatizacion = device.get("automatizacion_activa", {})
        
        print(f"\n{estado_icono} {device['nombre']} (ID: {device_id})")
        print(f"   Tipo: {device['tipo']}")
        print(f"   Estado: {device['estado']}")
        
        if automatizacion:
            nombre_auto = automatizacion.get("nombre", "Desconocida")
            descripcion = automatizacion.get("descripcion", "")
            print(f"   🤖 Automatización: {nombre_auto}")
            if descripcion:
                print(f"   ⏰ {descripcion}")

def desactivar_todas_automatizaciones(dispositivos):
    """Desactiva todas las automatizaciones activas."""
    if not dispositivos:
        print("\033[91mNo hay dispositivos registrados.\033[0m")
        return
    
    dispositivos_automatizados = [k for k, v in dispositivos.items() if v.get("automatizado", False)]
    
    if not dispositivos_automatizados:
        print("\033[93m⚠️ No hay automatizaciones activas para desactivar.\033[0m")
        return
    
    # Confirmar acción
    print(f"\033[93m⚠️ Se desactivarán {len(dispositivos_automatizados)} automatizaciones.\033[0m")
    confirmacion = input("¿Está seguro? (s/N): ").lower().strip()
    
    if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
        contador = 0
        for device_id in dispositivos_automatizados:
            device = dispositivos[device_id]
            device["automatizado"] = False
            device["automatizacion_activa"] = {}
            contador += 1
        
        print(f"\033[92m✅ Se desactivaron {contador} automatizaciones.\033[0m")
        print("   Todos los dispositivos mantienen su estado actual.")
    else:
        print("\033[94mOperación cancelada.\033[0m")