import os
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import *

from weather import WeatherGet

from Getmeme import MemeSend

from flask import current_app as app1

from twd import get_exchange_rate

from random import choice

from music import music_Leaderboard

import luis


app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi(
    'SJSoAEGKK4nj58UHAluyb6y18wAdeOUn/F163A1BEHGjI7BLUaFz/2rnRhskf2k9w/7XzOpwsCnZTcztjxjOEv/c2J0GuUd0RPcyQIfNLMzPt6WWxJ5XnMoYp4uBCsNJ7iG95AIAursQ/5xbpyq7aQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1a3c17ab604b6365246d4d6fe5f4c7e8')

# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app1.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


what_can_i_do = ("我目前只有3個按鈕\n"
                 "找廢圖點擊或輸入@meme\n"
                 "你可以問我天氣或是匯率\n"
                 "詢問xx縣orxx市天氣\n"
                 "詢問匯率ex:美國匯率\n"
                 "或是多少外幣可以換多少台幣\n"
                 "西洋，華語，日韓音樂排行榜\n"
                 "我寫的Chrome擴充:\n"
                 "我的網站:https://my-first-web-1.herokuapp.com/"
                 "請求資料複雜所以需要稍等一下")

angry = ['你以為我不再嗎= =?', '欸欸欸~注意言詞', '我就笨.jpg', '夠瞜夠瞜~', '你最聰明拉', 'zzzzzz']
hello = ['hi', 'hello', '你好阿', 'meow~', "你好", '安安']


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input = event.message.text

    if input == "@自我介紹":
        reply_text = "哈摟我叫yichengBOT\n建於2020/7/7\n問我:@你會幹嘛"
    elif input == "@你會幹嘛":
        reply_text = what_can_i_do
    elif input == "@meme":
        meme_jpg = MemeSend()
        reply_picture = ImageSendMessage(
            original_content_url=meme_jpg, preview_image_url=meme_jpg)
        line_bot_api.reply_message(event.reply_token, reply_picture)
    elif input in hello:
        reply_text = choice(hello)
    else:
        luis_report = luis.get_report(input)
        if luis.user_mind == "詢問天氣":
            reply_text = WeatherGet(luis_report)
        if luis.user_mind == "被罵":
            reply_text = choice(angry)
        if luis.user_mind == "查詢匯率":
            reply_text = get_exchange_rate(luis_report)
        if luis.user_mind == "音樂排行榜":
            reply_text = music_Leaderboard(luis_report)
    luis.user_mind = ''
    message = TextSendMessage(text=reply_text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
