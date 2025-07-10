# 🚕 Urban Routes – Automatización de Pedido de Taxi

Este proyecto forma parte del Sprint 8 del programa de QA y tiene como objetivo automatizar el flujo completo de pedir un taxi en la aplicación **Urban Routes**, utilizando Selenium WebDriver con el patrón Page Object Model (POM).

---

## 👤 Autor

**Nombre completo:** Luis Manco  
**Cohort:** qa-cohort-23

---

## 📌 Descripción del proyecto

Se automatizan los siguientes pasos de usuario:

1. Ingresar dirección de salida y destino.
2. Seleccionar la tarifa "Comfort".
3. Ingresar un número de teléfono.
4. Solicitar y capturar el código de confirmación.
5. Agregar una tarjeta bancaria.
6. Escribir un mensaje para el conductor.
7. Pedir una manta, pañuelos y dos helados 🍦.
8. Confirmar el pedido.
9. Verificar que se muestra el modal de búsqueda de conductor.
10. (Opcional) Verificar que se muestra la información del conductor.

---

## 🛠 Tecnologías y herramientas utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub
- Google Chrome + ChromeDriver

---

## 📁 Estructura del proyecto

```
📦qa-project-Urban-Routes-es
├── data.py          # Variables con datos del test (teléfono, direcciones, etc.)
├── main.py          # Automatización del flujo de pedido de taxi
├── README.md        # Este archivo
```

---

## ▶️ Cómo ejecutar las pruebas

### 1. Clona este repositorio

```bash
git clone https://github.com/tuusuario/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

### 2. Instala las dependencias

```bash
pip install selenium pytest
```

### 3. Ejecuta las pruebas

```bash
pytest main.py
```

Si tus pruebas están dentro de una carpeta (por ejemplo, `tests/`), el comando sería:

```bash
pytest tests/main.py
```

---

## ✅ Notas adicionales

- El código intercepta el código de verificación del teléfono utilizando los logs de red de Chrome (CDP).
- Recuerda verificar los IDs o selectores si la página cambia.
- Se recomienda probar con al menos 4 tipos de selectores: `ID`, `ClassName`, `XPath`, `CSS Selector`.

---

## 📬 Contacto

Si tienes dudas o sugerencias, puedes contactarme por Discord o vía GitHub issues.
