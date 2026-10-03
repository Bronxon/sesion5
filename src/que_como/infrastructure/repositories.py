class RepositorioTransaccion:

    def __init__(self):
        self.transacciones = []

    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def obtener_por_id(self, transaccion_id: int):
        for transaccion in self.transacciones:
            if transaccion.id == transaccion_id:
                return transaccion

        return None

    def obtener_por_usuario_y_restaurante(
        self,
        usuario_id: int,
        restaurante_id: int
    ):
        for transaccion in self.transacciones:
            if (
                transaccion.usuario_id == usuario_id
                and transaccion.restaurante_id == restaurante_id
            ):
                return transaccion

        return None


class RepositorioEvaluacion:

    def __init__(self):
        self.evaluaciones = []
        self.siguiente_id = 1

    def guardar(self, evaluacion):
        if evaluacion.id is None:
            evaluacion.id = self.siguiente_id
            self.siguiente_id += 1

        self.evaluaciones.append(evaluacion)

        return evaluacion

    def obtener_por_transaccion(self, transaccion_id: int):
        for evaluacion in self.evaluaciones:
            if evaluacion.transaccion_id == transaccion_id:
                return evaluacion

        return None


class RepositorioRestaurante:

    def __init__(self):
        self.restaurantes = []

    def agregar(self, restaurante):
        self.restaurantes.append(restaurante)

    def obtener_por_id(self, restaurante_id: int):
        for restaurante in self.restaurantes:
            if restaurante.id == restaurante_id:
                return restaurante

        return None
