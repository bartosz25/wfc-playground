from typing import Optional


class Order:

    def __init__(self, id: int, amount: float, user: str, coupon: Optional[str]) -> None:
        self.id = id
        self.amount = amount
        self.user = user
        self.coupon = coupon
