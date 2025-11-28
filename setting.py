APP_NAME = "MiAplicacion"
DEBUG = True
TIMEZONE = "America/Bogota"

# Las credenciales se leen desde variables de entorno
import os
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
