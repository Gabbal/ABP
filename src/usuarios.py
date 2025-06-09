from utilidades import limpiar_consola, pausar

def registrar_usuario(usuarios):
    limpiar_consola()
    print("--- Registro de Usuario ---\n")

    nombre = input("👤 Ingresá tu nombre completo: ").strip()
    usuario = input("🆔 Ingresá tu nombre de usuario: ").strip()
    contraseña = input("🔐 Ingresá tu contraseña: ").strip()

    if usuario in usuarios:
        print(f"\n⚠️ El usuario '{usuario}' ya existe. Intenta con otro.")
        pausar()
        return None

    # Si no hay usuarios aún, el primero será admin
    rol = "admin" if not usuarios else "estandar"

    nuevo_usuario = {
        "nombre": nombre,
        "contraseña": contraseña,
        "rol": rol
    }

    usuarios[usuario] = nuevo_usuario
    limpiar_consola()
    print(f"✅ Usuario '{usuario}' registrado exitosamente como '{rol}'.")
    return nuevo_usuario

def iniciar_sesion(usuarios):
    limpiar_consola()
    print("--- Iniciar Sesión ---\n")

    usuario = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print("\nInicio de sesión exitoso.")
        pausar()
        return { "usuario": usuario, **usuarios[usuario] }
    else:
        print("\n❌ Usuario o contraseña incorrectos.")
        pausar()
        return None
    
def consultar_datos_personales(usuario_actual):
    print("\n--- Datos Personales ---")
    # usuario_actual es un dict con clave "usuario" y datos
    nombre_usuario = usuario_actual.get("usuario")
    if not nombre_usuario:
        print("No se pudo determinar el usuario actual.")
        return
    # Se asume que el dict usuario_actual ya tiene los datos, pero si querés usar usuarios global:
    # datos = usuarios.get(nombre_usuario)
    datos = usuario_actual
    if datos:
        print(f"Nombre: {datos.get('nombre', 'No disponible')}")
        print(f"Rol: {datos.get('rol', 'No disponible')}")
    else:
        print("Usuario no encontrado.")

def modificar_rol_usuario(usuarios):
    usuario_a_modificar = input("🔄 Ingresá el nombre de usuario cuyo rol querés cambiar: ").strip()
    if usuario_a_modificar not in usuarios:
        print("❌ Usuario no encontrado.")
        return

    nuevo_rol = input("📝 Ingresá el nuevo rol (admin/estandar): ").lower()
    if nuevo_rol in ["admin", "estandar"]:
        usuarios[usuario_a_modificar]["rol"] = nuevo_rol
        print(f"✅ Rol de '{usuario_a_modificar}' actualizado a '{nuevo_rol}'.")
    else:
        print("❌ Rol inválido. Solo se permite 'admin' o 'estandar'.")
