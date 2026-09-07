import asyncio
import os
from telegram import Update, InputMediaPhoto, InputMediaVideo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# टोकन हम बाद में सर्वर की सेटिंग्स में डालेंगे
TOKEN = os.environ.get("BOT_TOKEN")

async def delete_album_after_delay(context: ContextTypes.DEFAULT_TYPE, chat_id: int, message_ids: list, delay: int):
    await asyncio.sleep(delay)
    for msg_id in message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except Exception as e:
            print(f"Error: {e}")
    print("Album auto-deleted!")

async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text("⏳ मीडिया भेज रहा हूँ... यह 3 मिनट में डिलीट हो जाएगा।")
    
    # 4 इमेजेस और 2 वीडियो के लिंक्स
    media_group = [
        InputMediaPhoto("https://picsum.photos"),
        InputMediaPhoto("https://picsum.photos"),
        InputMediaPhoto("https://picsum.photos"),
        InputMediaPhoto("https://picsum.photos"),
        InputMediaVideo("https://w3schools.com"),
        InputMediaVideo("https://w3schools.com")
    ]
    
    messages = await context.bot.send_media_group(chat_id=chat_id, media=media_group)
    message_ids = [msg.message_id for msg in messages]
    asyncio.create_task(delete_album_after_delay(context, chat_id, message_ids, 180))

if __name__ == "__main__":
    if not TOKEN:
        print("Error: BOT_TOKEN missing!")
        exit(1)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("demo", demo))
    print("Bot is running...")
    app.run_polling()
    
