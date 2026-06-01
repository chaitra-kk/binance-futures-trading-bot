from bot.client import BinanceClient

class OrderManager:

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )