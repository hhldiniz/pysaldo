from subscriber.Subscriber import Subscriber

if __name__ == "__main__":
    subscriber = Subscriber()
    subscriber.get_mqtt_client().on_message = subscriber.on_message
    subscriber.get_mqtt_client().on_connect = subscriber.on_connect
    subscriber.get_mqtt_client().on_disconnect = subscriber.on_disconnect
