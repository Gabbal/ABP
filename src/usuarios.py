from utilidades import limpiar_consola, pausar

#validador de ingreso de datos 
def pedir_dato(mensaje):
    while True:
        valor = input(mensaje)
        if not valor:
            print("❌ Error: el dato no puede estar vacío")
        else:
            return valor

def registrar_usuario(usuarios):
    limpiar_consola()
    print("--- Registro de Usuario ---\n")

    nombre = pedir_dato("👤 Ingresá tu nombre completo: ")
    apellido = pedir_dato("👤 Ingresá tu apellido: ")
    #registro mail y valido que este bien escrito
    while True:
            mail = input(" Ingresá tu correo electronico: ").strip()
            if not mail:
                print("Error: el correo no puede estar vacío")
            elif "@" not in mail or "." not in mail:
                print("Error: el correo debe contener '@' y '.' ejemplo: algo@mail.com")
            else:
                print("Correo válido:", mail)
                break

    contraseña = pedir_dato("🔐 Ingresá tu contraseña: ")
         
    #se valida que el usuario no este registrado anteriormente.
    if mail in usuarios:
        print(f"\n⚠️ El usuario '{mail}' ya existe. Intenta con otro.")
        pausar()
        return None

    # Si no hay usuarios aún, el primero será admin
    rol = "admin" if not usuarios else "estandar"

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "mail": mail,
        "contraseña": contraseña,
        "rol": rol
    }


    usuarios[mail] = nuevo_usuario
    limpiar_consola()
    print(f"✅ Usuario '{mail}' registrado exitosamente como '{rol}'.")
    return nuevo_usuario

def iniciar_sesion(usuarios):
    limpiar_consola()
    print("--- Iniciar Sesión ---\n")
    #se inicia sesion con correo electronico y contraseña para cumplir la coherencia con la DB
    mail = pedir_dato("correo electronico: ").strip()
    contraseña = pedir_dato("Contraseña: ").strip()

    if mail in usuarios and usuarios[mail]["contraseña"] == contraseña:
        print("\nInicio de sesión exitoso.")
        pausar()
        return { "usuario": mail, **usuarios[mail] }
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
        print(f"Apellido: {datos.get('apellido', 'No disponible')}")
        print(f"Mail: {datos.get('mail', 'No disponible')}")
        print(f"Rol: {datos.get('rol', 'No disponible')}")
    else:
        print("Usuario no encontrado.")

def modificar_rol_usuario(usuarios):
    usuario_a_modificar = pedir_dato("🔄 Ingresá el mail de usuario cuyo rol querés cambiar: ").strip()
    if usuario_a_modificar not in usuarios:
        print("❌ Usuario no encontrado.")
        return

    nuevo_rol = pedir_dato("📝 Ingresá el nuevo rol (admin/estandar): ").lower()
    if nuevo_rol in ["admin", "estandar"]:
        usuarios[usuario_a_modificar]["rol"] = nuevo_rol
        print(f"✅ Rol de '{usuario_a_modificar}' actualizado a '{nuevo_rol}'.")
    else:
        print("❌ Rol inválido. Solo se permite 'admin' o 'estandar'.")
