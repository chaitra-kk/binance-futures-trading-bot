import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import setup_logger

logger = setup_logger()

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

print("\n" + "=" * 50)
print(" Binance Futures Testnet Trading Bot ")
print("=" * 50)

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "LIMIT":
        if args.price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        validate_price(args.price)

    print("\n===== ORDER REQUEST =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.price:
        print(f"Price: {args.price}")

    logger.info(
        f"Order Request: "
        f"symbol={args.symbol}, "
        f"side={args.side}, "
        f"type={args.type}, "
        f"quantity={args.quantity}, "
        f"price={args.price}"
    )

    manager = OrderManager()

    if args.type == "MARKET":

        response = manager.place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        response = manager.place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\n===== ORDER RESPONSE =====")
    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))
    print("Avg Price:", response.get("avgPrice"))

    print("\n✅ Order placed successfully")

    logger.info(f"Order Response: {response}")

except Exception as e:

    logger.error(str(e))

    print("\n❌ Order failed")
    print("Reason:", str(e))