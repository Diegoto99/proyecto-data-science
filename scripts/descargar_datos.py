from pathlib import Path
import gdown

# Directorio raíz del proyecto
ROOT = Path(__file__).resolve().parent.parent

# Carpeta donde se guardan los datos originales
RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Archivo de Google Drive
FILE_ID = "1sZY1KPagTFuCoYQHEe8doL2DsJJLYZYC"

# Destino
OUTPUT_FILE = RAW_DIR / "ventas.csv"

URL = f"https://drive.google.com/uc?id={FILE_ID}"

print("Descargando dataset de ventas...")
print(f"Destino: {OUTPUT_FILE}")

gdown.download(
    URL,
    str(OUTPUT_FILE),
    quiet=False
)

print("Descarga finalizada.")
print(f"Archivo generado: {OUTPUT_FILE}")
print(f"Existe: {OUTPUT_FILE.exists()}")