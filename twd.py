import twder

currencies = {"美元": "USD", "美金": "USD", "美國": "USD",
              "港幣": "HKD", "香港": "HKD",
              "英鎊": "GBP", "英國": "GBP",
              "澳幣": "AUD", "澳洲": "AUD",
              "加拿大幣": "CAD", "加幣": "CAD", "加拿大": "CAD",
              "新加坡幣": "SGD", "新加坡": "SGD",
              "瑞士法郎": "CHF", "瑞士": "CHF",
              "日幣": "JPY", "日圓": "JPY", "日本": "JPY",
              "南非幣": "ZAR", "南非": "ZAR",
              "瑞典幣": "SEK", "瑞典": "SEK",
              "紐幣": "NZD", "紐西蘭幣": "NZD", "紐西蘭": "NZD",
              "泰幣": "THB", "泰銖": "THB", "泰國": "THB",
              "菲律賓幣": "PHP", "菲律賓": "PHP",
              "印尼盾": "IDR", "印尼幣": "IDR", "印尼": "IDR",
              "歐元": "EUR", "歐洲": "EUR",
              "韓元": "KRW", "韓國": "KRW",
              "越南幣": "VND", "越南": "VND",
              "馬來幣": "MYR", "馬來西亞": "MYR",
              "人民幣": "CNY", "中國": "CNY", "肺炎國": "CNY",
              "台幣": "TWD"}


def get_exchange_rate(city):
    global currencies
    keys = currencies.keys()
    tlist = ['現金買入', '現金賣出', '即期買入', '即期賣出']
    currency = city[0]
    try:
        if currency == '台幣':
            currency = city[1]
    except Exception:
        return "台幣匯率??好吧~ 1台幣=1台幣"

    show = currency+"匯率:\n"
    if currency in keys:
        if len(city) == 3:  # 如果資料中含有數字就轉跳到幣值換算
            citys_coin = [currencies[city[0]], currencies[city[1]]]
            return countingRate(citys_coin, city[2])
        for i in range(4):
            try:
                exchange = float(twder.now(currencies[currency])[i+1])
                show = show+tlist[i]+":"+str(exchange)+"\n"
            except Exception:
                show = show+'-\n'
        return show
    else:
        return "無此貨幣資料"


def countingRate(citys_info, number):  # 幣值換算
    result = ''
    if citys_info[0] == "TWD":
        result = float(number)/float(twder.now(citys_info[1])[1])
        return '%.2f' % result
    else:
        result = float(number)*float(twder.now(citys_info[0])[2])
        return '%.2f' % result


coin = ["日本"]
print(get_exchange_rate(coin))
