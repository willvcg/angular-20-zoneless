#!/usr/bin/env python3
"""
Script para validar la estructura y patrones de un proyecto Angular zoneless.
Verifica imports prohibidos, uso de signals, componentes standalone, etc.
"""

import os
import re
import sys
from pathlib import Path

def validate_angular_structure(project_root: Path) -> bool:
    """
    Valida la estructura del proyecto Angular zoneless.
    """
    issues = []

    # Buscar archivos TypeScript
    ts_files = list(project_root.rglob("*.ts"))
    ts_files = [f for f in ts_files if not f.name.endswith(".spec.ts") and not f.name.endswith(".d.ts")]

    for ts_file in ts_files:
        try:
            with open(ts_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Verificar imports prohibidos
            if 'import.*zone' in content.lower() or 'ngzone' in content.lower():
                issues.append(f"❌ {ts_file}: Importa Zone.js o NgZone, no permitido en zoneless.")

            # Verificar componentes standalone
            if '@Component' in content and 'standalone: true' not in content:
                issues.append(f"⚠️  {ts_file}: Componente no es standalone.")

            # Verificar uso de signals
            if 'signal(' not in content and 'computed(' not in content and '@Component' in content:
                issues.append(f"ℹ️  {ts_file}: Componente sin signals detectados.")

        except Exception as e:
            issues.append(f"❌ Error leyendo {ts_file}: {e}")

    # Verificar angular.json para zoneless
    angular_json = project_root / 'angular.json'
    if angular_json.exists():
        try:
            import json
            with open(angular_json, 'r') as f:
                config = json.load(f)
            # Verificar si está configurado para zoneless (esto es simplificado)
            if 'main.ts' in str(config):
                print("✅ angular.json encontrado.")
        except Exception as e:
            issues.append(f"❌ Error en angular.json: {e}")

    if issues:
        print("🚨 Problemas encontrados en la estructura Angular:")
        for issue in issues:
            print(f"  {issue}")
        return False
    else:
        print("✅ Estructura Angular zoneless validada correctamente.")
        return True

def main():
    project_root = Path(__file__).parent.parent.parent

    if not validate_angular_structure(project_root):
        print("\n❌ Validación fallida. Corrige los problemas antes de continuar.")
        sys.exit(1)
    else:
        print("\n✅ Proyecto listo para desarrollo zoneless.")
        sys.exit(0)

if __name__ == "__main__":
    main()