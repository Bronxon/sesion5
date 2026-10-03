from datetime import date


class Evaluacion:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        restaurante_id: int,
        transaccion_id: int,
        calificacion: int,
        comentario: str
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.restaurante_id = restaurante_id
        self.transaccion_id = transaccion_id
        self.calificacion = calificacion
        self.comentario = comentario
        self.fecha = date.today()

    def validar(self) -> bool:
        if not (1 <= self.calificacion <= 5):
            return False

        if (
            self.comentario is None
            or len(self.comentario.strip()) == 0
        ):
            return False

        return True

    def registrar(self):
        if not self.validar():
            raise ValueError(
                "Los datos de la evaluación son inválidos"
            )
