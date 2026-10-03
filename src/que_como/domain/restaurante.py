class Restaurante:
    def __init__(
        self,
        id: int,
        nombre: str,
        descripcion: str = "",
        calificacion_promedio: float = 0.0
    ):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.calificacion_promedio = calificacion_promedio
        self.evaluaciones = []

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)
        self._recalcular_promedio()

    def _recalcular_promedio(self):
        if not self.evaluaciones:
            self.calificacion_promedio = 0.0
            return

        total = sum(
            evaluacion.calificacion
            for evaluacion in self.evaluaciones
        )

        self.calificacion_promedio = (
            total / len(self.evaluaciones)
        )
