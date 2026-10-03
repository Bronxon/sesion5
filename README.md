# ¿QUÉ COMO?

Plataforma para búsqueda, comparación y evaluación de restaurantes basada en transacciones reales.

**Vertical slice (Taller 5):** evaluar un restaurante después de una transacción.

## Reglas de negocio cubiertas
Una evaluación solo se permite si la transacción existe, pertenece al usuario y al restaurante indicados, está `COMPLETADA`, no ha sido evaluada, la calificación está entre 1 y 5 y el comentario no está vacío.

## Estructura
```
src/que_como/
├── domain/          # Usuario, Restaurante, Transaccion, Evaluacion
├── application/     # ControladorEvaluacion
└── infrastructure/  # Repositorios en memoria
tests/               # Pruebas T01-T10 (patrón AAA)
```

## Ejecución
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest -v
pytest --cov=que_como --cov-report=term-missing
```

## Resultados
- 10 pruebas, todas en verde.
- Cobertura total: 88 % (el flujo del controlador, 100 %).

## Flujo de Git
Rama de trabajo: `feature/evaluar-restaurante-transaccion` (commits: `test:` → `feat:` → `docs:`), lista para Pull Request hacia `main`.
