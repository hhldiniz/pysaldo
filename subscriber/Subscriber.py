from BaseMqttClass import BaseMqtt


class Subscriber(BaseMqtt):
    def __init__(self):
        super().__init__()
        self.__hash = ""
        self.__value_available = 0

    def withdraw(self, valor):
        self.get_mqtt_client().publish("saldo/retirada", valor)

    def set_hash(self, value):
        self.__hash = value

    def get_hash(self):
        return self.__hash

    def on_message(self, client, userdata, message):
        if message.topic == "saldo/valor":
            self.__value_available = message.payload
