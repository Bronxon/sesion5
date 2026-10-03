class Usuario:
    def __init__(self, id: int, nombre: str, contacto: str):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.transacciones = []
        self.evaluaciones = []

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)

    def puede_evaluar(self, transaccion) -> bool:
        return (
            transaccion.usuario_id == self.id
            and transaccion.puede_evaluarse()
        )
