# Cryptocurrency converter
import requests
import sys
import re
import argparse
import csv
from datetime import datetime
from tabulate import tabulate


def main():
    # Declaring variables
    number = 0
    history = []
    take_input = False
    show_table = True
    table = [
        [1, "Cryptocurrency coin converter"],
        [2, "Show history"],
        [3, "Save history (as csv)"],
        [4, "Read history (csv)"],
        [5, "Exit the program"],
    ]

    # argparse
    parser = argparse.ArgumentParser(description="Cryptocurrency converter")
    parser.add_argument(
        "-n",
        default="",
        help="amount of the coin you have (Please provide in float number)",
    )
    parser.add_argument("-a", help="name of the coin you have")
    parser.add_argument("-b", help="name of the coin you want to convert")
    args = parser.parse_args()

    if args.a and args.b:
        A = (args.n + args.a).upper().strip()
        coinB = args.b.upper().strip()
    else:
        take_input = True

    # Program starts here
    while True:
        if take_input:
            # Show Menu
            if show_table:
                print(tabulate(table, tablefmt="rounded_grid"))
            show_table = True
            number = is_number(input("Please type number: ").strip())

        # 1. Use cryptocurrency coin converter
        if number == "1" or take_input == False:
            break_loop = False
            while True:
                if take_input:
                    A = input("Amount and name of the coin you have? ").upper().strip()
                    coinB = (
                        input("Name of the coin you want to convert? ").upper().strip()
                    )

                try:
                    coinA, coinA_amount = split_coin(A)
                    if is_USDT(coinA) and not is_USDT(coinB):
                        coinA_in_coinB = coinA_amount / convert_USDT(coinB)
                    elif is_USDT(coinB) and not is_USDT(coinA):
                        coinA_in_coinB = convert_USDT(coinA) * coinA_amount
                    elif is_USDT(coinA) and is_USDT(coinB):
                        coinA_in_coinB = coinA_amount
                    else:
                        coinA_in_USDT = convert_USDT(coinA) * coinA_amount
                        coinB_in_USDT = convert_USDT(coinB)
                        coinA_in_coinB = coinA_in_USDT / coinB_in_USDT
                except ValueError:
                    print("Please provide float number.")
                except KeyError:
                    print("Please provide correct coin name valid in Binance.")
                else:
                    history.append(
                        f"{datetime.today()}, {coinA_amount} {coinA} is {coinA_in_coinB:.8f} {coinB}"
                    )
                    print(history[-1])
                    if take_input == True:
                        # Continue using coin converter
                        while True:
                            answer = input(
                                "Continue using coin converter? (y/n) "
                            ).strip()
                            if re.search(r"^(?:y|yes)$", answer, re.IGNORECASE):
                                break
                            elif re.search(r"^(?:n|no)$", answer, re.IGNORECASE):
                                # To break (1) coin converter loop
                                break_loop = True
                                break
                            else:
                                continue

                if take_input == False:
                    sys.exit()
                if break_loop:
                    break

        # 2. Show history
        elif number == "2":
            for sentence in history:
                print(sentence)
            input("Type anything to continue ")

        # 3. Save history
        elif number == "3":
            while True:
                try:
                    csv_name = csv_filter(input("Name of csv: ").strip())
                except ValueError:
                    pass
                else:
                    with open(csv_name, "a") as file:
                        writer = csv.DictWriter(
                            file, fieldnames=["Time", "Coin A", "Coin B"]
                        )
                        # To add header if the file doesn't have any header.
                        with open(csv_name) as f:
                            reader = csv.reader(f)
                            lines = [row for row in reader]
                            if not lines:
                                writer.writeheader()
                        for sentence in history:
                            if matches := re.search(r"^(.+), (.+) is (.+)$", sentence):
                                writer.writerow(
                                    {
                                        "Time": matches.group(1),
                                        "Coin A": matches.group(2),
                                        "Coin B": matches.group(3),
                                    }
                                )
                    input("Type anything to continue ")
                    break

        # 4. Read history
        elif number == "4":
            sentences = []

            try:
                file_name = csv_filter(input("Name of csv: ").strip())
                with open(file_name) as file:
                    dictreader = csv.DictReader(file)
                    for row in dictreader:
                        sentences.append(
                            {
                                "Time": row["Time"],
                                "Coin A": row["Coin A"],
                                "Coin B": row["Coin B"],
                            }
                        )
            except FileNotFoundError:
                print("File doesn't exit.")
            except ValueError:
                print("Please type in correct format.")
            else:
                for sentence in sentences:
                    print(
                        f'{sentence["Time"]}, {sentence["Coin A"]} is {sentence["Coin B"]}'
                    )
            input("Type anything to continue ")

        # 5. Exit the program
        elif number == "5":
            sys.exit("Goodbye")

        else:
            show_table = False
            continue


def convert_USDT(coin):
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    url = key + coin + "USDT"
    data = requests.get(url)
    data = data.json()
    return float(data["price"])


def split_coin(coin):
    if matches := re.search(
        r"^(?:(\d*\.?\d+)? *([a-z]+)|([a-z]+) *(\d*\.?\d+)?)$", coin, re.IGNORECASE
    ):
        if matches.group(2) and matches.group(2).isalpha():
            name = matches.group(2)
            coin_amount = convert_amount(matches.group(1))
        else:
            name = matches.group(3)
            coin_amount = convert_amount(matches.group(4))
        return (name, coin_amount)
    else:
        raise ValueError


def convert_amount(amount):
    if amount:
        return float(amount)
    else:
        return float("1")


def is_USDT(coin):
    if re.search(r"^USDT$", coin, re.IGNORECASE):
        return True
    else:
        return False


def csv_filter(file_name):
    if matches := re.search(r"^(\w+)(?:\.*csv)*$", file_name, re.IGNORECASE):
        return matches.group(1) + ".csv"
    else:
        raise ValueError


def is_number(n):
    if matches := re.search(r"^(\d+)\.*$", n):
        return matches.group(1)
    else:
        return n


if __name__ == "__main__":
    main()
