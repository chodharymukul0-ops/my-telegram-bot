import asyncio
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

PHOTO_IDS = [
    "AgACAgQAAxkBAAMjap2-ULvbSovndg-MMrYPKNKW3KEAAmMOaxuD2elQRkCXMll3FzkBAAMCAAN5AAM9BA",
    "AgACAgQAAxkBAAMbap28ruh9F-YfIo_SeuZkHgu-ac4AAqsQaxs0QTBTxEsoywE5I3YBAAMCAAN5AAM9BA",
    "AgACAgQAAxkBAAMlap2-UIBTUun_JOKY6OFDZbdXIEEAAnMVaxuroPBQEMidYKgAATFTAQADAgADeQADPQQ",
    "AgACAgQAAxkBAAMmap2-UDDcBXZ_QywmJXnPMai4yY8AAnkNaxsimwlTDGGfut7dOEsBAAMCAAN5AAM9BA"
]

VIDEO_IDS = [
    "BAACAgQAAxkBAAMaap28rt3l89KvlgZ7SfHFg17w6pMAAkghAAKroPBQiPZ6D4pYx-c9BA",
    "BAACAgQAAxkBAAMnap2-UD8Qa9ErLgTyIgN9-rrm7WYAAk8hAAKroPBQ0xu8Datj9FQ9BA"
]

async def send_media_and_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    sent_messages = []
    try:
        for photo_id in PHOTO_IDS:
            msg = await context.bot.send_photo(chat_id=chat_id, photo=photo_id)
            sent_messages.append(msg.message_id)
        for video_id in VIDEO_IDS:
            msg = await context.bot.send_video(chat_id=chat_id, video=video_id)
            sent_messages.append(msg.message_id)
        text_msg = await context.bot.send_message(chat_id=chat_id, text="Demo will be deleted after 3 mins")
        sent_messages.append(text_msg.message_id)
        await asyncio.sleep(180)
        for msg_id in sent_messages:
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except:
                pass
    except Exception as e:
        print(f"Error: {e}")

def main():
    if not TOKEN:
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT | filters.COMMAND, send_media_and_timer))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
