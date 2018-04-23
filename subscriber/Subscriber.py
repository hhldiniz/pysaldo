import paho.mqtt.client as mqtt


class Subscriber:
    def __init__(self):
        self.__mqtt = mqtt.Client()

    def get_mqtt_client(self):
        return self.__mqtt

    def on_connect(self, client, userdata, flags, rc):
        print(rc)

    def on_disconnect(self, client, userdata, rc):
        print(rc)

    def on_message(self, client, userdata, message):
        print(message)
