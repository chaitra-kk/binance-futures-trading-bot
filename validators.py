def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "\n❌ Invalid Side\n"
            "Allowed values: BUY, SELL"
        )

def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in [
        "MARKET",
        "LIMIT"
    ]:
        raise ValueError(
            "\n❌ Invalid Order Type\n"
            "Allowed values: MARKET, LIMIT"
        )

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError(
            "\n❌ Invalid Quantity\n"
            "Quantity must be greater than 0"
        )

def validate_price(price):
    if price is not None and price <= 0:
        raise ValueError(
            "\n❌ Invalid Price\n"
            "Price must be greater than 0"
        )