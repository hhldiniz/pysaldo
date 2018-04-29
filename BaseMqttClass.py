import paho.mqtt.client as mqtt


class BaseMqtt:
    def __init__(self):
        self.__mqtt = mqtt.Client()
        self.__mqtt.username_pw_set(username="yhdytvpm", password="2nMy0rfV-hKE")
        self.__mqtt.connect(host="m11.cloudmqtt.com", port=18446)

    def get_mqtt_client(self):
        return self.__mqtt

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected")
        print(f"Client info: {client}. Connection status: {rc}")
        print(f"Userdata: {userdata}")
        print(f"Flags: {flags}")

    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print(f"Client info: {client}. Connection status: {rc}")
            print(f"Userdata: {userdata}")
            print("Disconectado abruptamente")

    def on_message(self, client, userdata, message):
        print(message)
