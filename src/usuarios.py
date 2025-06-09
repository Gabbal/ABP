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
