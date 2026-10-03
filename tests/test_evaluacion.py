import pytest
from datetime import date

from que_como.domain.usuario import Usuario
from que_como.domain.restaurante import Restaurante
from que_como.domain.transaccion import (
    Transaccion,
    EstadoTransaccion
)
from que_como.application.controlador_evaluacion import (
    ControladorEvaluacion
)
from que_como.infrastructure.repositories import (
    RepositorioTransaccion,
    RepositorioEvaluacion,
    RepositorioRestaurante
)


class TestEvaluacionRestaurante:

    def setup_method(self):
        self.repo_transaccion = RepositorioTransaccion()
        self.repo_evaluacion = RepositorioEvaluacion()
        self.repo_restaurante = RepositorioRestaurante()

        self.controlador = ControladorEvaluacion(
            self.repo_transaccion,
            self.repo_evaluacion,
            self.repo_restaurante
        )

        self.usuario = Usuario(
            1,
            "Ana",
            "ana@email.com"
        )

        self.restaurante = Restaurante(
            10,
            "Sabor Local",
            "Comida mexicana"
        )

        self.repo_restaurante.agregar(self.restaurante)

    def crear_transaccion(
        self,
        estado=EstadoTransaccion.COMPLETADA
    ):
        transaccion = Transaccion(
            id=100,
            usuario_id=self.usuario.id,
            restaurante_id=self.restaurante.id,
            fecha=date.today(),
            importe=250.00,
            estado=estado
        )

        self.repo_transaccion.agregar(transaccion)
        return transaccion

    def test_transaccion_completada_permite_evaluacion(self):
        self.crear_transaccion()

        evaluacion = self.controlador.evaluar_restaurante(
            usuario_id=1,
            restaurante_id=10,
            transaccion_id=100,
            calificacion=5,
            comentario="Excelente lugar"
        )

        assert evaluacion.calificacion == 5
        assert evaluacion.usuario_id == 1
        assert evaluacion.restaurante_id == 10
        assert evaluacion.transaccion_id == 100

    def test_transaccion_pendiente_rechaza_evaluacion(self):
        self.crear_transaccion(EstadoTransaccion.PENDIENTE)

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=5,
                comentario="Muy bueno"
            )

    def test_transaccion_inexistente_rechaza_evaluacion(self):
        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=999,
                calificacion=5,
                comentario="Muy bueno"
            )

    def test_usuario_incorrecto_rechaza_evaluacion(self):
        self.crear_transaccion()

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=99,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=5,
                comentario="Muy bueno"
            )

    def test_restaurante_incorrecto_rechaza_evaluacion(self):
        self.crear_transaccion()

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=99,
                transaccion_id=100,
                calificacion=5,
                comentario="Muy bueno"
            )

    def test_calificacion_menor_que_uno_rechaza_evaluacion(self):
        self.crear_transaccion()

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=0,
                comentario="Muy bueno"
            )

    def test_calificacion_mayor_que_cinco_rechaza_evaluacion(self):
        self.crear_transaccion()

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=6,
                comentario="Muy bueno"
            )

    def test_comentario_vacio_rechaza_evaluacion(self):
        self.crear_transaccion()

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=5,
                comentario="   "
            )

    def test_transaccion_ya_evaluada_rechaza_segunda_evaluacion(self):
        self.crear_transaccion()

        self.controlador.evaluar_restaurante(
            usuario_id=1,
            restaurante_id=10,
            transaccion_id=100,
            calificacion=5,
            comentario="Excelente"
        )

        with pytest.raises(ValueError):
            self.controlador.evaluar_restaurante(
                usuario_id=1,
                restaurante_id=10,
                transaccion_id=100,
                calificacion=4,
                comentario="Segunda evaluación"
            )

    def test_evaluacion_valida_se_registra_correctamente(self):
        transaccion = self.crear_transaccion()

        evaluacion = self.controlador.evaluar_restaurante(
            usuario_id=1,
            restaurante_id=10,
            transaccion_id=100,
            calificacion=4,
            comentario="Buena experiencia"
        )

        assert len(self.repo_evaluacion.evaluaciones) == 1
        assert transaccion.evaluacion == evaluacion
        assert len(self.restaurante.evaluaciones) == 1
