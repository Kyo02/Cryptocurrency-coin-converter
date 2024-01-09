import requests
import pytest
from project import (
    convert_USDT,
    split_coin,
    convert_amount,
    is_USDT,
    csv_filter,
    is_number,
)


def test_convert_USDT():
    assert convert_USDT("ETC") == float(
        requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=ETCUSDT"
        ).json()["price"]
    )


def test_convert_USDT_invalid_coin():
    with pytest.raises(KeyError):
        convert_USDT("BTSS")


def test_split_coin():
    assert split_coin("22.3BTC") == ("BTC", 22.3)
    assert split_coin("DOGE3.25") == ("DOGE", 3.25)


def test_convert_amount():
    assert convert_amount("2.52") == 2.52
    assert convert_amount("3") == 3.0


def test_convert_None_amount():
    assert convert_amount(None) == 1.0


def test_is_USDT():
    assert is_USDT("USDT") == True
    assert is_USDT("BTC") == False


def test_csv_filter():
    assert csv_filter("something") == "something.csv"
    assert csv_filter("something....CsV") == "something.csv"


def test_csv_filter_error():
    with pytest.raises(ValueError):
        csv_filter(".csv")


def test_is_number():
    assert is_number("2.") == "2"
    assert is_number("3") == "3"
    assert is_number("cat") == "cat"
