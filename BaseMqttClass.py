import paho.mqtt.client as mqtt


class BaseMqtt:
    def __init__(self):
        self.__mqtt = mqtt.Client()

    def get_mqtt_client(self):
        return self.__mqtt

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Disconectado abruptamente")

    def on_message(self, client, userdata, message):
        print(message)