#!/bin/bash
set -e

wait-for-it db:5432

alembic upgrade head

uvicorn app.main:app --reload --host=0.0.0.0
