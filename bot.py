import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_API_TOKEN = "xxxxxxxxx"
SOURCE_CHAT_ID = -4796607635
DESTINATION_CHAT_ID = -4666534022

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message.chat_id == SOURCE_CHAT_ID:

        await context.bot.send_message(
            chat_id=DESTINATION_CHAT_ID,
            text="נמצאה משרת סטודנט:"
        )
        await context.bot.forward_message(
            chat_id=DESTINATION_CHAT_ID,
            from_chat_id=update.effective_message.chat_id,
            message_id=update.effective_message.message_id
        )


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    application = Application.builder().token(BOT_API_TOKEN).build()

    application.add_handler(
        MessageHandler(filters.Chat(SOURCE_CHAT_ID) & filters.ALL, forward_message)
    )

    application.run_polling()


if __name__ == '__main__':
    main()

