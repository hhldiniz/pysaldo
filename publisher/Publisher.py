from BaseMqttClass import BaseMqtt


class Publisher(BaseMqtt):
    def __init__(self, saldo_inicial):
        super().__init__()
        self.__saldo_inicial = saldo_inicial
