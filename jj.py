import random, re
import time
from random import randint
import telegram
from telegram import Message, Update, Bot, User,ParseMode
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from tg_bot.modules.helper_funcs.chat_status import user_admin
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
@user_admin
def toss(bot: Bot, update: Update):
      x = random.choice(['💫 Result : Head', '💫 Result :Tail '])
      y = random.choice(['💫 Result : Head', '💫 Result :Tail ','💫 Result : Head','💫 Result :Tail '])
      z = random.choice(['💫 Result :Tail ','💫 Result : Head','💫 Result :Tail ', '💫 Result : Head'])
      r = random.choice([x,z,y])
      a = update.message.reply_text("*" + r  + "*",parse_mode=telegram.ParseMode.MARKDOWN)
@run_async
def show(bot: Bot, update: Update):
   if len(update.effective_message.text.split(' ')) > 1:
      a = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      b = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      c = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      update.message.reply_text("𝓟𝓵𝓪𝔂𝓮𝓻 " + update.message.text.split(" ")[1]+ """ 𝓒𝓪𝓻𝓭𝓼:
""" + "{ " + a + " }" + "  { "+ b + " }  { " + c + " }", parse_mode=ParseMode.MARKDOWN )
      a = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      b = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      c = random.choice(["1","2","3","4","5","6","7","8","9","10","🅐","🅠","🅚","🅙"]) + random.choice([ "♠️","♣️","♥️","♦️"])
      update.message.reply_text("𝓟𝓵𝓪𝔂𝓮𝓻 " + update.message.text.split(" ")[2] + """ 𝓒𝓪𝓻𝓭𝓼:
""" + "{ " + a + " }" + "  { "+ b + " }  { " + c + " }" , parse_mode=ParseMode.MARKDOWN )
   else:
        update.message.reply_text('Please write username {without @} after command!')
		
@run_async
@user_admin            
def ball(bot: Bot, update: Update):
    if len(update.effective_message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      update.message.reply_text("*Ball 0.{} 🎾: ".format(update.message.text.split(' ')[1]) + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣")  + "*" ,parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
@user_admin            
def over(bot: Bot, update: Update):
    if len(update.effective_message.text.split(' ')) > 1:
      q = float(0.1)
      p = float(0)
      s = float(0)
      while True:
        x = random.choice(["3","2","4","3","0","2","1","0","2","3","2","4","6"])
        y = random.choice(['7','8','9'])
        z = random.choice(['11','12','13'])
        r = random.choice([x,x,z,x,z,x,x,y,x,x,x,x])
        if r == z:
         v = random.choice(["🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
         update.message.reply_text("*Ball " + str(q)+ "🎾" + ": " + v + "*",parse_mode=ParseMode.MARKDOWN)
        if r == x:
         update.message.reply_text("*Ball " + str(q) + "🎾: " + x.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣").replace("0","🅾 Dot Ball 🅾")+ "*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
        if r == y:
         q = (float(q)*1000 + float(0.1)*1000)/1000
         l = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
         update.message.reply_text("*Ball " + str(q) + "🎾" + ": " + l + "*",parse_mode=ParseMode.MARKDOWN)
         p = float(p) + float(1)
         update.message.reply_text("*" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾*',parse_mode=ParseMode.MARKDOWN)
         if p == update.message.text.split(" ")[1]:
          break
        if ".6" in str(q):
         q = float(str(q).replace(".6","")) + float(1)
         update.message.reply_text('*' + str(q).replace('.0','') + ' OVER '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + " 🅾🅾*",parse_mode=ParseMode.MARKDOWN)  
        if q == update.message.text.split(" ")[2]:
           break
        time.sleep(2)
    else:
      update.message.reply_text('Please write over number after command!')
		
__help__ = """
♻️ This is Gamebot created by a wonderful person ✍️.
My commands :
👉 For show user cards
1. /show {username}
👉 for sps
2. /sps
👉 for even odd
3. /dice or /roll {range}
👉 for double roll
4. /droll {range} or /dice2
👉 for decision
5. /decide
👉 for roulette
6. /rolls
🤜Lucky 7
7. /luck
All command exist only Admins in Super groups ✍️.
"""

__mod_name__ = "Extras"

OVER_HANDLER = DisableAbleCommandHandler("over", over)
TOSS_HANDLER = DisableAbleCommandHandler("toss",toss)
BALL_HANDLER = DisableAbleCommandHandler("ball",ball)
SHOW_HANDLER = DisableAbleCommandHandler("sw",show)
dispatcher.add_handler(SHOW_HANDLER)
dispatcher.add_handler(OVER_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(BALL_HANDLER)
