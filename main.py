from telethon import TelegramClient, events

api_id = xxxxxx
api_hash = 'xxxxxxx'

# Create the client instance.
client = TelegramClient('session_main', api_id, api_hash)
print('connection established')

# Define the target word to monitor in messages
target_word = 'student'

# Specify the target group by its group ID
group_identifier = -1001281025780 # jobs group
group_target = -4796607635 # bridge group

@client.on(events.NewMessage(chats=group_identifier))
async def my_event_handler(event):
    # Check if the target word is present in the message text, lower/upper-case insensitive.
    if target_word.lower() in event.raw_text.lower():
        # Send an alert message to yourself ('me' sends a message to your own account)
        await client.forward_messages(group_target, event.message)

print("ממתין להודעות...")
client.start()
client.run_until_disconnected()

