
from telethon import TelegramClient, sync, events

INPUT_CHANNEL = 'KHuro_nOuCK_bot'
OUTPUT_CHANNEL = 'imageToText_bot'
TAGS = ['']
# 1. Заходим на сайт https://my.telegram.org/apps
# 2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.


api_id = 7036266 
api_hash = '801b489bd8da3f43ea8fe164f0c0bc0a'


client = TelegramClient('session_name', api_id, api_hash)




@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):

    if tag in str(event.message):
        await client.send_message(OUTPUT_CHANNEL, event.message)

client.start()
client.run_until_disconnected()
