# Cryptocurrency converter
#### Video Demo:  https://youtu.be/9yynkfRC_V8
#### Description: Convert cryptocurrency coin to another crypto coin
## About
My project is a [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency) converter which can be used to convert from one crypto coin to another crypto coin. First, it uses [Binance](https://www.binance.com/en)'s API to convert your own coin and your desired coin to USDT. And, multiply your coin in USDT with your coin amount. Then, by dividing your coin in USDT by your desired coin in USDT, your coin has been converted to your desired coin.

You can convert any cryptocurrency available in [Binance](https://www.binance.com/en/markets/overview) because the program uses Binance's API. However, you **cannot** change or convert from your cryptocurrency coin to [traditional currency](https://en.wikipedia.org/wiki/Fiat_money) or vice versa because the program is only designed for converting crypto coin to crypto coin.

In this program, you can

+ convert crypto coins,
+ view your converted history in which each history expressed in your local timezone,
+ save your history as csv file,
+ read your saved file.
## Usage
Once you start the program, the menu with numbers will be displayed, and you can use it by typing the exact number you want to use. If you start the program,

1. Cryptocurrency coin converter
1. Show history
1. Save history (as csv)
1. Read history (csv)
1. Exit the program

that menu will be displayed.

If you type in,

1. you will be able to use cryptocurrency coin converter. First, it will ask you the amount and the name of the coin you have. (Example: 2.3 BTC). You can type in int type or float type number or no number. For coin name, please note that you can **ONLY** type in **ABBREVIATION** of the coin name (e.g. BTC, ETH, USDT, ...), and **not** an actual coin name like "Bitcoin", "Ethereum", etc. Second, you will be asked the name of the coin you want to convert. (Example: USDT). Then, the answer will be displayed. I won't show the answer here because the answer may vary according to time. The prices of the crypto coins are changing over time. Note that ValueError will occur if you type in characters other than numbers and alphabet or if you type in incorrectly that doesn't follow the rule. KeyError will occur if you type in incorrect coin name or coin that is not available in Binance.
1. your converted history according to your local timezone will be displayed. If you haven't used coin converter yet, nothing will be displayed. Once you exit the program, your converted history will be deleted if you don't save it as a csv file.
1. you can save your converted history as a csv file with a custom name. The custom name can only be word characters.
1. you can read your saved history from your saved csv file. But, you have to type in the file name correctly. **Note** that you can only read the csv files that are saved with this program. FileNotFoundError will occur if the file you search is not in the path or doesn't exist. ValueError will occur if you type in incorrect file name.
1. you can quit the program.
## Command Line Usage
You can also use coin converter with the command line. It is convenient for users who would like to use the coin converter casually without needing to access the program normally and get stuck in a loop. To use, please type "project.py -n (your coin amount) -a (your coin name) -b (name of coin you want to convert)" at your command line interface. (Example: "project.py -n 2.3 -a BTC -b USDT"). It will exit the program once it has done converting the crypto coin. You can use like that without "-n". The program will automatically assume the amount as "1" as a default value. But "-a" and "-b" is essential.
## Top 50 Coins
Here are the names of top 50 coins to use coin converter.

1. Bitcoin (BTC)
1. Ethereum (ETH)
1. Binance Coin (BNB)
1. Tether (USDT)
1. Cardano (ADA)
1. XRP (XRP)
1. Dogecoin (DOGE)
1. Polkadot (DOT)
1. Bitcoin Cash (BCH)
1. Litecoin (LTC)
1. Chainlink (LINK)
1. Stellar (XLM)
1. Uniswap (UNI)
1. USD Coin (USDC)
1. Wrapped Bitcoin (WBTC)
1. Polygon (MATIC)
1. VeChain (VET)
1. Solana (SOL)
1. Theta Token (THETA)
1. Ethereum Classic (ETC)
1. Filecoin (FIL)
1. TRON (TRX)
1. Dai (DAI)
1. Aave (AAVE)
1. Cosmos (ATOM)
1. Neo (NEO)
1. Monero (XMR)
1. PancakeSwap (CAKE)
1. Bitcoin SV (BSV)
1. IOTA (MIOTA)
1. Terra (LUNA)
1. Avalanche (AVAX)
1. Tezos (XTZ)
1. EOS (EOS)
1. FTX Token (FTT)
1. Maker (MKR)
1. Huobi Token (HT)
1. Compound (COMP)
1. Kusama (KSM)
1. Algorand (ALGO)
1. BitTorrent (BTT)
1. The Graph (GRT)
1. Neo (NEO)
1. Synthetix (SNX)
1. Revain (REV)
1. Celsius (CEL)
1. Holo (HOT)
1. SushiSwap (SUSHI)
1. Waves (WAVES)
1. Elrond (EGLD)

There are several other coins available in Binance. If you want to find out the names of the other coins, you can search [_here_](https://www.binance.com/en/markets/overview).

I hope this project is useful for you. Thank you and this is CS50.
