
import telebot
import os
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# Bot Token aur Telegram ID
TOKEN = '8802874837:AAHCwEn-lUzx0mHpot5Y04fM58HRZNTqcaE'
bot = telebot.TeleBot(TOKEN)

# 24/7 active rakhne ke liye chhota sa web server (Flask)
app = Flask('')

@app.route('/')
def home():
    return "Jack Sarvar Bot is Alive and Running 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# Game Data Generation Logic
def generate_game_data():
    now = datetime.now()
    period_number = now.strftime("%Y%m%d%H%M")
    
    last_digit_str = period_number[-1]
    lucky_number = int(last_digit_str)
    
    if lucky_number >= 5:
        size = "ＢＩＧ 🔵"
    else:
        size = "ＳＭＡＬＬ 🟡"
        
    if lucky_number == 0:
        color = "Red & Violet 🔴🟣"
    elif lucky_number == 5:
        color = "Green & Violet 🟢🟣"
    elif lucky_number in [1, 3, 7, 9]:
        color = "Green 🟢"
    else:
        color = "Red 🔴"
        
    telegram_id = "@Lion3dx"
    
    text = (
        f"┏━━━ 𝙅𝙖𝙘𝙠 𝙎𝙖𝙧𝙫𝙖𝙧 ━━━┓\n\n"
        f"⏳ **WinGo 1 Min**\n"
        f"⏱ 𝗣𝗲𝗿𝗶𝗼𝗱 ➾ `{period_number}`\n"
        f"🔢 𝗡𝘂𝗺𝗯𝗲𝗿 ➾ **{lucky_number}**\n"
        f"📊 𝗦𝗶𝘇𝗲 ➾ {size}\n"
        f"🎨 𝗖𝗼𝗹𝗼𝗿 ➾ {color}\n"
        f"👤 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 ➾ {telegram_id}\n\n"
        f"┗━━━━━━━━━━━━━━┛"
    )
    return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✨ Namaste! Jack Sarvar bot active hai. Signal ke liye /game likhein.")

@bot.message_handler(commands=['game'])
def send_game_result(message):
    text = generate_game_data()
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⏭ Next Prediction", callback_data="next_pred"))
    markup.add(InlineKeyboardButton("🔗 Click Here to Play", url="https://www.lottery7cc.com/#/register?invitationCode=3426419172014"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "next_pred")
def callback_query(call):
    text = generate_game_data()
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⏭ Next Prediction", callback_data="next_pred"))
    markup.add(InlineKeyboardButton("🔗 Click Here to Play", url="https://example.com"))
    
    bot.send_message(call.message.chat.id, text, reply_markup=markup, parse_mode="Markdown")
    bot.answer_callback_query(call.id)

if __name__ == "__main__":
    # Web server aur bot dono ko ek sath start karna
    keep_alive()
    print("24/7 Cloud Ready Bot Started...")
    bot.infinity_polling()
