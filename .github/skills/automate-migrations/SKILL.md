---
name: alembic-manager
description: 'Use when updating the database schema, adding or removing model fields, creating or applying Alembic migrations for this FastAPI + SQLite project. Triggers on: "migrate", "update schema", "add column", "alembic", "revision", "upgrade head".'
argument-hint: "Describe the schema change, e.g. 'add bio field to User model'"
---

# Skill: Automate Migrations

## Nombre
automate-migrations

## Descripción
Automatiza el ciclo de vida de las migraciones de base de datos en proyectos Python basados en SQLAlchemy/Alembic.

## Funcionalidades
- Detectar cambios en los modelos de datos.
- Generar scripts de migración con `alembic revision --autogenerate`.
- Aplicar migraciones en entornos de desarrollo y staging.
- Validar el estado del esquema y la sincronización con los modelos.

## Uso recomendado
- Ejecutar en pipelines de CI para asegurar que los cambios de esquema estén definidos.
- Revisar los scripts generados antes de aplicarlos en producción.
- Mantener un entorno aislado al crear y probar migraciones.
