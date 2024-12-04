from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Function to handle all messages
async def handle_message(update: Update, context):
    await update.message.reply_text("Bot under maintenance")

def main():
    # Replace with your bot token
    TOKEN = "6776169673:AAHs1H4YWJ1HdtpWNaTZE4QkKlA9rbvILzI"

    # Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()

    # Add a message handler for all text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
