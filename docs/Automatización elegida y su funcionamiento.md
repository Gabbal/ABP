# 🏠 Sistema SmartHome

Un sistema de gestión domótica desarrollado en Python que permite controlar dispositivos inteligentes y configurar automatizaciones para el hogar.

### Sistema de Automatización
- 🌙 **Automatización nocturna**: Configuración automática para la noche
- 🤖 **Control de automatizaciones**: Activa/desactiva automatizaciones específicas
- 📊 **Estado de automatizaciones**: Visualiza qué dispositivos están automatizados
- 🔄 **Gestión masiva**: Desactiva todas las automatizaciones de una vez

## 📖 Guía de Uso

### 1. Gestión de Dispositivos

#### Agregar un Dispositivo
1. Selecciona "Gestionar Dispositivos" → "Agregar dispositivo"
2. Proporciona:
   - **ID único** (ej: `luz1`, `cam01`)
   - **Nombre descriptivo** (ej: "Luz Sala", "Cámara Entrada")
   - **Tipo** (ej: "luz", "cámara", "sensor")

#### Estados de Dispositivos
- 🟢 **Encendido**: Dispositivo activo
- 🔴 **Apagado**: Dispositivo inactivo
- 🤖 **Automatizado**: Controlado por automatización
- 👤 **Manual**: Control manual del usuario

### 2. Sistema de Automatización

#### Automatización Nocturna
La automatización nocturna ejecuta las siguientes acciones:

**Para Luces/Iluminación:**
- ✅ Se apagan automáticamente
- 🏷️ Tipos reconocidos: `luz`, `luces`, `lampara`, `iluminacion`
- 📋 Regla aplicada: "Modo Nocturno"
- ⏰ Descripción: "Luces apagadas automáticamente (22:00-06:00)"

**Para Cámaras/Seguridad:**
- ✅ Se encienden automáticamente
- 🏷️ Tipos reconocidos: `camara`, `seguridad`, `vigilancia`
- 📋 Regla aplicada: "Vigilancia Nocturna"
- ⏰ Descripción: "Cámara activada para seguridad nocturna"

#### Control de Automatizaciones

##### Ver Estado de Automatizaciones
Muestra información detallada de todos los dispositivos:
```
📱 Luz Principal (ID: luz1)
   Estado: apagado
   Automatización: 🟢 Activa
   Control: 🤖 Automatizado
   📋 Regla: Modo Nocturno
   ⏰ Luces apagadas automáticamente (22:00-06:00)
```

##### Desactivar Automatización Específica
- Permite desactivar la automatización de un dispositivo individual
- **Importante**: El dispositivo mantiene su estado actual
- Solo se elimina el control automático, pasando a control manual

##### Desactivar Todas las Automatizaciones
- Desactiva todas las automatizaciones activas del sistema
- Solicita confirmación antes de ejecutar
- Todos los dispositivos mantienen su estado actual

## 🎯 Ejemplos de Uso

### Escenario 1: Configuración Nocturna
```
1. Agregar dispositivos:
   - ID: luz1, Nombre: "Luz Sala", Tipo: "luz"
   - ID: cam1, Nombre: "Cámara Entrada", Tipo: "camara"

2. Ejecutar automatización nocturna:
   - luz1 → Se apaga automáticamente
   - cam1 → Se enciende para vigilancia

3. Resultado:
   🔴 Luz Sala - Apagada (Modo Nocturno)
   🟢 Cámara Entrada - Activada (Vigilancia Nocturna)
```

### Escenario 2: Control Manual Override
```
1. Dispositivo con automatización activa
2. Cambiar estado manualmente:
   - La automatización se desactiva automáticamente
   - El dispositivo pasa a control manual
3. Para reactivar automatización:
   - Usar menú de automatizaciones específicas
```

### Escenario 3: Gestión de Automatizaciones
```
1. Ver dispositivos automatizados:
   - Lista solo dispositivos con automatización activa
   
2. Desactivar automatización específica:
   - Seleccionar dispositivo por ID
   - Mantiene estado actual, elimina control automático
   
3. Desactivar todas:
   - Confirma acción (s/N)
   - Desactiva todas las automatizaciones masivamente
```

## 🔧 Tipos de Dispositivos Soportados

### Iluminación
- **Tipos reconocidos**: `luz`, `luces`, `lampara`, `iluminacion`
- **Automatización nocturna**: Se apagan
- **Estados**: encendido/apagado

### Seguridad
- **Tipos reconocidos**: `camara`, `seguridad`, `vigilancia`
- **Automatización nocturna**: Se encienden
- **Estados**: encendido/apagado

### Otros Dispositivos
- Cualquier otro tipo de dispositivo puede ser agregado
- Control manual de encendido/apagado
- No afectados por automatización nocturna (actualmente)

## 🐛 Resolución de Problemas

### El sistema no muestra colores
- Verifica que tu terminal soporte códigos ANSI
- En Windows, usa Windows Terminal o actualiza a Windows 10+

### Dispositivo no se encuentra
- Verifica que el ID sea exacto (sensible a mayúsculas/minúsculas)
- Usa "Listar dispositivos" para ver IDs disponibles

### Automatización no funciona
- Verifica que el tipo de dispositivo sea reconocido
- Los tipos deben coincidir exactamente: `luz`, `camara`, etc.

