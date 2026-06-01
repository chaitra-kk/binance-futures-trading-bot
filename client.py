import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceClient:

    def __init__(self):

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        self.client = Client(
            api_key,
            api_secret
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

        # sync local time with Binance server
        server_time = self.client.get_server_time()
        self.client.timestamp_offset = (
            server_time["serverTime"]
            - int(__import__("time").time() * 1000)
        )

    def get_client(self):
        return self.client