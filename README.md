# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

The bot supports:

* BUY orders
* SELL orders
* MARKET orders
* LIMIT orders
* Input validation
* Logging
* Error handling
* Command Line Interface (CLI)

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env
├── cli.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### MARKET Order

```bash
py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
py cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

---

## Features

* Binance Futures Testnet Integration
* BUY and SELL Support
* MARKET and LIMIT Orders
* CLI-based Input
* Validation of User Inputs
* Logging of Requests and Responses
* Exception Handling

---

## Logging

Logs are stored in:

```text
logs/trading.log
```

The log file records:

* Order requests
* Order responses
* Errors and exceptions

---

## Assumptions

* User has valid Binance Demo/Testnet API credentials.
* Internet connection is available.
* Binance API service is accessible.

---

## Dependencies

* python-binance
* python-dotenv
