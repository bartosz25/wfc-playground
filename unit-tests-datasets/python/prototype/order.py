import time
from random import random, randint
from typing import Optional


class Order:

    def __init__(self, id: int = randint(0, 100000), amount: float = 33.33,
                 user: str = f"user{int(time.time())}", coupon: Optional[str] = None) -> None:
        self.id = id
        self.amount = amount
        self.user = user
        self.coupon = coupon


order1 = Order(id=1, amount=33.99)
order2 = Order(id=2, coupon="promo60")