def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    today_day = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f"{today_day}\n Sell BTC price: {sell_price}\n")
    return f"{today_day}\n Sell BTC price: {round(sell_price)}\n"