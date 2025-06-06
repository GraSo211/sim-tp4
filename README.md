# 🚴‍♂️ Simulación - Taller de Bicicletas Urbanas

> Este proyecto simula la atención en un taller de bicicletas urbanas, modelando la llegada de clientes, el trabajo de un asistente y un mecánico, y las distintas tareas involucradas.

---

## 📋 Requisitos de Visualización

Para una mejor experiencia visual, se recomienda instalar la fuente **Montserrat**:

1. [Descargar la fuente desde Google Fonts](https://fonts.google.com/specimen/Montserrat)
2. Descomprimir el archivo ZIP.
3. Ubicar los archivos `.ttf`.
4. Hacer clic derecho sobre ellos y seleccionar **"Instalar"**.

---

## 📘 Enunciado del Problema

### “Taller de Bicicletas Urbanas”

En un taller especializado en bicicletas urbanas trabajan dos personas: un **mecánico** y su **asistente**.

El **asistente** tiene la tarea de atender a los clientes que llegan al local, con una distribución de llegada **uniforme entre 13 y 17 minutos**. Los clientes pueden:

- 🛒 Comprar accesorios (45%)
- 🔧 Entregar bicicletas para reparación (25%)
- 🚲 Retirar bicicletas previamente reparadas (30%)

#### Tiempos de atención:

- **Comprar accesorios:** entre **6 y 10 minutos** (distribución uniforme).
- **Entregar/retirar bicicleta:** exactamente **3 minutos**.

---

El **mecánico** se dedica exclusivamente a reparar bicicletas:

- La reparación toma entre **18 y 22 minutos** (distribución uniforme).
- Luego, dedica **5 minutos** a limpiar herramientas y reorganizar su espacio antes de la siguiente reparación.

🔧 Inicialmente, hay **3 bicicletas reparadas** listas para ser retiradas.

---

## 🎯 Objetivos de la Simulación

- Calcular la **probabilidad de que un cliente llegue a retirar una bicicleta que aún no esté reparada**.
- Determinar el **porcentaje de ocupación del asistente**.
- Determinar el **porcentaje de ocupación del mecánico**.
