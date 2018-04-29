from BaseMqttClass import BaseMqtt


class Subscriber(BaseMqtt):
    def __init__(self):
        super().__init__()
        self.__hash = ""

    def withdraw(self, valor):
        self.get_mqtt_client().publish("saldo/retirada", valor)

    def set_hash(self, value):
        self.__hash = value

    def get_hash(self):
        return self.__hash
