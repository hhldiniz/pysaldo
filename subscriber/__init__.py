from threading import Thread
from time import sleep

from Coordinator import Coordinator
from subscriber.Subscriber import Subscriber


class SubscriberStarter(Thread):
    def __init__(self):
        super().__init__()
        self.coordinator = Coordinator()
        self.subscriber = Subscriber()
        self.subscriber.get_mqtt_client().on_message = self.subscriber.on_message
        self.subscriber.get_mqtt_client().on_connect = self.subscriber.on_connect
        self.subscriber.get_mqtt_client().on_disconnect = self.subscriber.on_disconnect

    def execute_withdraw(self, value):
        if self.coordinator.get_hash() is not "":
            self.subscriber.set_hash(self.coordinator.get_hash())
            self.coordinator.set_hash("")
            self.coordinator.proccess_request(self.subscriber.withdraw, value)
            self.coordinator.set_hash(self.subscriber.get_hash())
            self.subscriber.set_hash("")

    def run(self):
        self.subscriber.get_mqtt_client().loop_start()
        while True:
            self.execute_withdraw(10)
            sleep(1)


if __name__ == "__main__":
    starter = SubscriberStarter()
    starter.run()
