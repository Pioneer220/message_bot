from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Store user IDs in a set to avoid duplicates
user_ids = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_ids.add(user_id)  # Add the user's ID to the set
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You have been registered!")

async def send_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"  # Message to send
    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
            print(f"Sent message to {user_id}")
        except Exception as e:
            print(f"Error sending message to {user_id}: {e}")

def main() -> None:
    application = ApplicationBuilder().token("7714002659:AAESisWUra5T93uAcLRcqp3shJWPhcA3SnQ").build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sendmessages", send_messages))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()