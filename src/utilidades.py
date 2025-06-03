import os
from datetime import datetime

def limpiar_consola():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")

def obtener_hora_actual():
    """Obtiene la hora actual del usuario con validación."""
    while True:
        hora = input("\033[93mIngrese la hora actual (HH:MM): \033[0m")
        try:
            return datetime.strptime(hora, "%H:%M")
        except ValueError:
            print("\033[91m❌ Formato inválido. Use HH:MM (ejemplo: 20:30)\033[0m")