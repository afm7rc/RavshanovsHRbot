 
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import settings

# Loglarni yozish
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# /start komandasi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Salom! Men ishga tushdim! ✅")

# Asosiy funksiya
def main():
    app = Application.builder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    logging.info("Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
