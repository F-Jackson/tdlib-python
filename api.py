from telegram.client import Telegram
from telegram.text import Spoiler

print("HIIIIIIIII")

tg = Telegram(
    api_id='18018658',
    api_hash='85d8e89157145ed33a4029df2b302be6',
    phone='+5511949097973',  # you can pass 'bot_token' instead
    database_encryption_key='changekey123',
    files_directory='/tmp/.tdlib_files/',
)
tg.login()

# If this is the first run, the library needs to preload all chats.
# Otherwise, the message will not be sent.
result = tg.get_chats()
result.wait()

chat_id: int
result = tg.send_message(chat_id, Spoiler('Hello world!'))

# `tdlib` is asynchronous, so `python-telegram` always returns an `AsyncResult` object.
# You can receive a result with the `wait` method of this object.
result.wait()
print(result.update)

tg.stop()  # You must call `stop` at the end of the script.
