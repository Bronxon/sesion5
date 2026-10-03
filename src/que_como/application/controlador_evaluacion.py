from que_como.domain.evaluacion import Evaluacion


class ControladorEvaluacion:

    def __init__(
        self,
        repo_transaccion,
        repo_evaluacion,
        repo_restaurante
    ):
        self.repo_transaccion = repo_transaccion
        self.repo_evaluacion = repo_evaluacion
        self.repo_restaurante = repo_restaurante

    def evaluar_restaurante(
        self,
        usuario_id: int,
        restaurante_id: int,
        transaccion_id: int,
        calificacion: int,
        comentario: str
    ) -> Evaluacion:

        transaccion = self.repo_transaccion.obtener_por_id(
            transaccion_id
        )

        if transaccion is None:
            raise ValueError("No existe la transacción")

        if not transaccion.es_del_usuario(usuario_id):
            raise ValueError(
                "La transacción no pertenece al usuario"
            )

        if not transaccion.es_del_restaurante(restaurante_id):
            raise ValueError(
                "La transacción no pertenece al restaurante"
            )

        if not transaccion.puede_evaluarse():
            raise ValueError(
                "La transacción no puede utilizarse para evaluar"
            )

        evaluacion = Evaluacion(
            id=None,
            usuario_id=usuario_id,
            restaurante_id=restaurante_id,
            transaccion_id=transaccion_id,
            calificacion=calificacion,
            comentario=comentario
        )

        if not evaluacion.validar():
            raise ValueError(
                "Datos de evaluación inválidos"
            )

        evaluacion_guardada = self.repo_evaluacion.guardar(
            evaluacion
        )

        transaccion.registrar_evaluacion(
            evaluacion_guardada
        )

        restaurante = self.repo_restaurante.obtener_por_id(
            restaurante_id
        )

        if restaurante is not None:
            restaurante.agregar_evaluacion(
                evaluacion_guardada
            )

        return evaluacion_guardada
