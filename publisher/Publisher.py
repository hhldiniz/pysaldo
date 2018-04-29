from BaseMqttClass import BaseMqtt


class Publisher(BaseMqtt):
    def __init__(self, saldo_inicial):
        super().__init__()
        self.__saldo = saldo_inicial
        self.publish_value("saldo/valor", self.__saldo)

    def publish_value(self, topic, payload):
        print(payload)
        self.get_mqtt_client().publish(topic, payload)

    def get_saldo(self):
        return self.__saldo

    def withdraw(self, value):
        self.__saldo -= value
        self.publish_value("saldo/valor", value)

    def deposit(self, value):
        self.__saldo += value
        self.publish_value("saldo/valor", value)

    def on_message(self, client, userdata, message):
        if message.topic == "saldo/retirada":
            self.withdraw(message.payload)
        elif message.topic == "saldo/deposito":
            self.deposit(message.payload)
