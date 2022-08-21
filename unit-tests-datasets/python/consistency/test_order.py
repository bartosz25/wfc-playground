from consistency.data_generators import OrderDataGenerator


def test_if_id_is_negative():
    order = OrderDataGenerator.generate_order(id=-1)

    assert order.id == -1, "Negative id should be allowed"


def test_if_id_is_positive():
    order = OrderDataGenerator.generate_order(id=1)

    assert order.id == 1, "Positive id should be allowed"