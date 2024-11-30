import os
from dotenv import load_dotenv
from telegram.client import Telegram
from telegram.text import Spoiler

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Recuperar as variáveis de ambiente
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
database_encryption_key = os.getenv('DATABASE_ENCRYPTION_KEY')
files_directory = os.getenv('FILES_DIRECTORY')

# Configuração do Telegram usando as variáveis de ambiente
tg = Telegram(
    api_id=api_id,
    api_hash=api_hash,
    phone=phone_number,  # Ou use 'bot_token' se estiver usando um bot
    database_encryption_key=database_encryption_key,
    files_directory=files_directory,
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
