import _thread as thread

from Coordinator import Coordinator
from subscriber.Subscriber import Subscriber


def execute_withdraw(value):
    if coordinator.get_hash() is not "":
        subscriber.set_hash(coordinator.get_hash())
        coordinator.set_hash("")
        coordinator.proccess_request(subscriber.withdraw, value)
        coordinator.set_hash(subscriber.get_hash())
        subscriber.set_hash("")


def start_threads(value):
    for i in range(0, value):
        thread.start_new_thread(execute_withdraw, (10,))


if __name__ == "__main__":
    coordinator = Coordinator()
    subscriber = Subscriber()
    subscriber.get_mqtt_client().on_message = subscriber.on_message
    subscriber.get_mqtt_client().on_connect = subscriber.on_connect
    subscriber.get_mqtt_client().on_disconnect = subscriber.on_disconnect
    start_threads(3)
