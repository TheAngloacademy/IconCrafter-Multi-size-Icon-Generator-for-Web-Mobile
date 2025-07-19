# 🖼️ Icon Generator Python Tool

Crea automáticamente múltiples versiones redimensionadas de una imagen base para usar como iconos en aplicaciones web o móviles.

---

## 📌 Características

* Selección de imagen desde explorador de archivos (ventana emergente)
* Generación de:

  * Iconos de distintos tamaños (`128x128`, `256x256`, `512x512`, etc.)
  * Archivos especiales como `favicon.png` y `apple-touch-icon.png`
* Guardado automático en una carpeta `icon` junto a la imagen seleccionada

---

## 🚀 ¿Cómo usarlo?

1. Instala las dependencias (necesitas Python):

```bash
pip install pillow
```

2. Ejecuta el script:

```bash
python generar_iconos.py
```

3. Selecciona una imagen (`.jpg`, `.png`, `.jpeg`, `.webp`)

4. ¡Listo! Tus iconos estarán en la carpeta `icon` al lado de tu imagen.

---

## 📁 Estructura de salida

```
icon/
├── 128x128.png
├── 144x144.png
├── 152x152.png
├── 180x180.png
├── 192x192.png
├── 256x256.png
├── 512x512.png
├── apple-touch-icon.png
└── favicon.png
```

---

## 🧠 Ideal para

* Favicons para sitios web
* Iconos de apps móviles (iOS / Android)
* PWA (Progressive Web Apps)

---

## 📎 Nombre del proyecto sugerido

**IconCrafter: Multi-size Icon Generator for Web & Mobile**

---

## 📜 Licencia

MIT License
