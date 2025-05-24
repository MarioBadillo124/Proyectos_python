import os
import shutil

# Rutas de origen y destino
ruta_origen = "C:/ruta/a/tu/carpeta"  # Ruta de la carpeta que deseas organizar
ruta_destino = "C:/ruta/a/tu/carpeta_organizada"  # Ruta a donde se organizarán los archivos

# Extensiones categorizadas
categorias = {
    "Fotos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".avi", ".mkv", ".mov"],
    "Archivos comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Otros": []  # Archivos sin categoría específica
}

# Crear carpetas para cada categoría si no existen
for categoria in categorias:
    carpeta = os.path.join(ruta_destino, categoria)
    os.makedirs(carpeta, exist_ok=True)

# Función para mover archivos
def mover_archivos():
    for archivo in os.listdir(ruta_origen):
        ruta_archivo = os.path.join(ruta_origen, archivo)
        
        # Verificar si es un archivo
        if os.path.isfile(ruta_archivo):
            # Identificar la categoría según la extensión
            extension = os.path.splitext(archivo)[1].lower()
            movido = False
            
            for categoria, extensiones in categorias.items():
                if extension in extensiones:
                    destino = os.path.join(ruta_destino, categoria, archivo)
                    shutil.move(ruta_archivo, destino)
                    print(f"Movido: {archivo} -> {categoria}")
                    movido = True
                    break
            
            # Si no coincide con ninguna categoría, mover a "Otros"
            if not movido:
                destino = os.path.join(ruta_destino, "Otros", archivo)
                shutil.move(ruta_archivo, destino)
                print(f"Movido: {archivo} -> Otros")

# Ejecutar la organización
if __name__ == "__main__":
    mover_archivos()
    print("Organización completa.")
