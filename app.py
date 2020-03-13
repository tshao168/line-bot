from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('J8DONUwn81YR7dmp5T24tZ3tK7ZoejrLdRz/9dpLE0jYZ9xm0B4IOyJwiP+1keI5tPJH4Gj6Ub7nukx9QJqmkhVFgGlCL+Ke0de1eRE8RZk5/vi0yOU91/4W5mVKlNRe4dneb4GraGCPKfdrJ6WY6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6be22ac311c51ae0de5da1d61239d6dc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉,您說什麼'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎?'
        人= '還沒'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= s))


if __name__ == "__main__":
    app.run()