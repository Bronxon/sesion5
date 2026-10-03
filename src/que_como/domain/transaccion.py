from enum import Enum


class EstadoTransaccion(Enum):
    INICIADA = "INICIADA"
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    COMPLETADA = "COMPLETADA"
    CANCELADA = "CANCELADA"


class Transaccion:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        restaurante_id: int,
        fecha,
        importe: float,
        estado: EstadoTransaccion
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.restaurante_id = restaurante_id
        self.fecha = fecha
        self.importe = importe
        self.estado = estado
        self.evaluacion = None

    def es_del_usuario(self, usuario_id: int) -> bool:
        return self.usuario_id == usuario_id

    def es_del_restaurante(self, restaurante_id: int) -> bool:
        return self.restaurante_id == restaurante_id

    def puede_evaluarse(self) -> bool:
        if self.estado != EstadoTransaccion.COMPLETADA:
            return False

        if self.evaluacion is not None:
            return False

        return True

    def registrar_evaluacion(self, evaluacion):
        if not self.puede_evaluarse():
            raise ValueError(
                "La transacción no puede utilizarse para evaluar"
            )

        self.evaluacion = evaluacion
