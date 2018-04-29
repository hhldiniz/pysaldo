from publisher.Publisher import Publisher


class PublisherStarter:
    def __init__(self):
        self.publisher = Publisher(100)
        self.publisher.get_mqtt_client().on_connect = self.publisher.on_connect
        self.publisher.get_mqtt_client().on_disconnect = self.publisher.on_disconnect
        self.publisher.get_mqtt_client().on_message = self.publisher.on_message

    def start(self):
        self.publisher.get_mqtt_client().loop_forever()


if __name__ == "__main__":
    publisher_starter = PublisherStarter()
    publisher_starter.start()
