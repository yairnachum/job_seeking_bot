from telethon.sync import TelegramClient

api_id = 10258662
api_hash = 'a5b47c7d32f215ac328a02fac9d4d091'


client = TelegramClient('session_name', api_id, api_hash)
client.start()

dialogs = client.get_dialogs()
for dialog in dialogs:
    print(f"Name: {dialog.name}, ID: {dialog.id}")
