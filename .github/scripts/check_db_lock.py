#!/usr/bin/env python3
"""
Script para verificar bloqueos en la base de datos SQLite.
Útil para detectar transacciones abiertas o conexiones bloqueadas.
"""

import sqlite3
import sys
import os
from pathlib import Path

def check_db_lock(db_path: str) -> bool:
    """
    Verifica si la base de datos está bloqueada intentando una conexión de solo lectura.
    """
    try:
        # Intentar conexión con timeout corto
        conn = sqlite3.connect(db_path, timeout=1.0)
        cursor = conn.cursor()

        # Ejecutar una consulta simple para verificar acceso
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        conn.close()

        if result and result[0] == 1:
            print(f"✅ Base de datos {db_path} accesible, sin bloqueos detectados.")
            return False  # No bloqueada
        else:
            print(f"⚠️  Respuesta inesperada de la base de datos {db_path}.")
            return True

    except sqlite3.OperationalError as e:
        if "database is locked" in str(e).lower():
            print(f"🔒 Base de datos {db_path} está bloqueada: {e}")
            return True
        else:
            print(f"❌ Error operativo en {db_path}: {e}")
            return True
    except Exception as e:
        print(f"❌ Error al verificar {db_path}: {e}")
        return True

def main():
    # Buscar archivos .db en el directorio del proyecto
    project_root = Path(__file__).parent.parent.parent
    db_files = list(project_root.rglob("*.db"))

    if not db_files:
        print("ℹ️  No se encontraron archivos .db en el proyecto.")
        sys.exit(0)

    locked_dbs = []

    for db_file in db_files:
        if check_db_lock(str(db_file)):
            locked_dbs.append(db_file)

    if locked_dbs:
        print(f"\n🚨 {len(locked_dbs)} base(s) de datos bloqueada(s) encontrada(s):")
        for db in locked_dbs:
            print(f"  - {db}")
        sys.exit(1)
    else:
        print("\n✅ Todas las bases de datos están accesibles.")
        sys.exit(0)

if __name__ == "__main__":
    main()