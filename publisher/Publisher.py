from BaseMqttClass import BaseMqtt


class Publisher(BaseMqtt):
    def __init__(self, saldo_inicial):
        super().__init__()
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo

    def retirada(self, valor):
        self.__saldo -= valor

    def deposito(self, valor):
        self.__saldo += valor

    def on_message(self, client, userdata, message):
        if message.topic == "saldo/retirada":
            self.retirada(message.payload)
        elif message.topic == "saldo/deposito":
            self.deposito(message.payload)
