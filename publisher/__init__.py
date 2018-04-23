from publisher.Publisher import Publisher


if __name__ == "__main__":
    publisher = Publisher(100)
    publisher.get_mqtt_client().on_connect = publisher.on_connect
    publisher.get_mqtt_client().on_disconnect = publisher.on_disconnect
    publisher.get_mqtt_client().on_message = publisher.on_message
