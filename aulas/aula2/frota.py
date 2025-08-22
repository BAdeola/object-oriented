class Carro:
    modelo: str
    odometro: float
    motor: bool
    cor: str
    marca: str
    tanque: float
    consumo_medio: float

    def __init__(self, modelo: str, cor: str, marca: str, consumo_medio: float, tanque: float):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.odometro = 0.0
        self.motor = False
        self.consumo_medio = consumo_medio
        self.tanque = tanque

    def ligar(self):
        if not self.motor:
            self.motor = True
        else:
            raise Exception("Motor já ligado.")

    def desligar(self):
        if self.motor:
            self.motor = False
        else:
            raise Exception("Motor já desligado.")

    def acelerar(self, velocidade: float, tempo: float):
        if not self.motor:
            raise Exception("Motor desligado.")

        km = velocidade * tempo
        litros_necessarios = km / self.consumo_medio

        if self.tanque >= litros_necessarios:
            self.odometro += km
            self.tanque -= litros_necessarios
        else:
            distancia_possivel = self.tanque * self.consumo_medio
            self.odometro += distancia_possivel
            self.tanque = 0.0
            self.desligar()
            raise Exception(f"O {self.modelo} ficou sem combustível!")

    def __str__(self):
        status_motor = "ligado" if self.motor else "desligado"
        return (f"{self.modelo} ({self.marca}, {self.cor}) - "
                f"{status_motor} | {self.odometro:.1f} km rodados | "
                f"{self.tanque:.1f} L no tanque")
