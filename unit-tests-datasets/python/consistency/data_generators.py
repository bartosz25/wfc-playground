from typing import Any

from consistency.data_models import Order

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DataGeneratorWrapper(metaclass=Singleton):
    def __init__(self):
        self.container = []

    def add_item(self, item: Any):
        print(f'adding {item}')
        self.container.append(item)
        print(self.container)

    def get_items(self):
        return self.container



class OrderDataGenerator:

    @staticmethod
    def generate_order(id: int, amount: float = 100.55, user: str = "user 1", coupon=None) -> Order:
        generated_order = Order(
            id=id, amount=amount, user=user, coupon=coupon
        )
        DataGeneratorWrapper().add_item(generated_order)
        return generated_order
