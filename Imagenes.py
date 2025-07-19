from PIL import Image
import os

# Imagen original
input_image_path = 'imagen_base.jpg'  # Cambia esto por la ruta de tu imagen base

# Lista de tamaños y nombres deseados
output_specs = [
    ("128x128.png", (128, 128)),
    ("144x144.png", (144, 144)),
    ("152x152.png", (152, 152)),
    ("192x192.png", (192, 192)),
    ("256x256.png", (256, 256)),
    ("512x512.png", (512, 512)),
    ("apple-touch-icon.png", (180, 180)),
    ("favicon.png", (64, 64))  # puedes ajustarlo a 32x32 si prefieres
]

# Crear carpeta de salida
output_folder = "iconos_generados"
os.makedirs(output_folder, exist_ok=True)

# Cargar imagen base
with Image.open(input_image_path) as img:
    for filename, size in output_specs:
        resized = img.resize(size, Image.LANCZOS)
        resized.save(os.path.join(output_folder, filename))
        print(f"Generado: {filename} ({size[0]}x{size[1]})")

print("✅ Todas las imágenes han sido creadas.")
