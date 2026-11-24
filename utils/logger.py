import pathlib
from datetime import datetime
import logging

# Creación de carpeta para los logs
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

# Se genera la fecha para definir el nombre del archivo en formato str
timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

# Se define la configuración para el log
logging.basicConfig(
    # Ruta y nombre del archivo
    filename= logs_dir / f"log_{timestamp}.log",
    # Niveles de importacia del registro, registra desde nivel INFO a superiores
    level=logging.INFO,
    # Formato de como se van a generar las lineas del mensaje con fecha, hora y nivel.
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s",
    # Obliga a remplazar las capturas de logs a este tipo de estructura.
    force=True
)
# Nombre de cada creación de logs
logger = logging.getLogger("talento_tech")