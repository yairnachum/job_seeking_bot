from telethon.sync import TelegramClient

api_id = xxxxx
api_hash = 'xxxxxx'


client = TelegramClient('session_name', api_id, api_hash)
client.start()

dialogs = client.get_dialogs()
for dialog in dialogs:
    print(f"Name: {dialog.name}, ID: {dialog.id}")
