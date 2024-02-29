class Circulo():
    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontos = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1

    @classmethod
    def get(cls):
        return cls._total_circulos
