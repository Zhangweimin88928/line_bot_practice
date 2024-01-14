import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e7909763174540cd8adbc95dc2d7f3a9',
}

user_mind = None
params = {
    # Query parameter
    'q': 'init',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'true',
}


def get_report(user_input):
    try:
        query = user_input
        params['q'] = query
        r = requests.get(
            'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/445b8090-2457-4d6a-b2d5-7f88b85b5806', headers=headers, params=params)
        ret = r.json()
    except Exception as e:
        print(e)
    return report_parser(ret)


def report_parser(ret):
    global user_mind
    if ret['topScoringIntent']['intent'] == '詢問天氣':
        user_mind = '詢問天氣'
        for en in ret['entities']:
            if en['type'] == '地點':
                city = en["entity"]
                return city

    if ret['topScoringIntent']['intent'] == '被罵':
        user_mind = '被罵'

    if ret['topScoringIntent']['intent'] == '查詢匯率':
        user_mind = '查詢匯率'
        coin = []
        for en in ret['entities']:
            if en['type'] == '幣種':
                coin.append(en["entity"])
            elif en['type'] == '數量':
                coin.append(en["entity"])
        return coin

    if ret['topScoringIntent']['intent'] == '音樂排行榜':
        user_mind = '音樂排行榜'
        for en in ret['entities']:
            if en['type'] == "語言":
                lang = en['entity']
        return lang
#
