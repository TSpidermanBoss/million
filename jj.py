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
      f = float(0)
      while True:
        x = random.choice(["2","1","3","2","1","3","1","2","6","1","4","3","1","6","2","4","3","2","1","2"])
        y = random.choice(['7','8','9'])
        z = random.choice(['11','12','13'])
        r = random.choice([x,x,z,x,z,x,x,y,x,x,x,x])
        if r == z:
         v = random.choice(["wd"])
         if v == "wd":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 🙆‍♂ Wide Ball 🙆‍♂*",parse_mode=ParseMode.MARKDOWN)
         f = float(f) + float(1)
         s = float(s) + float(1)
        if r == x:
         if x == "0":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 🅾 Dot Ball 🅾*",parse_mode=ParseMode.MARKDOWN)
         if x == "1":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 1⃣ Single 1⃣*",parse_mode=ParseMode.MARKDOWN)
         if x == "2":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 2⃣ Double 2⃣*",parse_mode=ParseMode.MARKDOWN)
         if x == "3":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 3⃣ Three 3⃣*",parse_mode=ParseMode.MARKDOWN)
         if x == "4":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 4⃣ Four 4⃣*",parse_mode=ParseMode.MARKDOWN)
         if x == "6":
          update.message.reply_video(media='',caption = "*Ball " + str(q)+ "🎾: 6⃣ Six Gya Six 6⃣*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
         f = float(f) + float(r)
        if r == y:
         l = random.choice(["lbw","cth"])
         if l == "lbw":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 🚾 Wicket 🚾*",parse_mode=ParseMode.MARKDOWN)
         if l == "cth":
          update.message.reply_video(media='wwwsffff',caption = "*Ball " + str(q)+ "🎾: 🚾 Catch out 🚾*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         p = float(p) + float(1)
         time.sleep(2)
         update.message.reply_video("**" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾**')
        if ".7" in str(q):
         q = (float(str(q).replace(".7",""))*1000 + float(1.1)*1000)/1000
         time.sleep(2)
         update.message.reply_video('**' + str(q).replace('.1','') + ' 𝕆𝕍𝔼ℝ '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 🅾🅾
	 
 𝕊𝕔𝕠𝕣𝕖 𝕥𝕙𝕚𝕤 𝕠𝕧𝕖𝕣 : """ + str(f).replace('.0','') +  """ 🏏🏏
	 
 𝕊𝕥𝕣𝕚𝕜𝕖 ℝ𝕒𝕥𝕖 : """ + str(round((s/(float(str(q).replace('.1',''))*6))*100,2)) + "**")  
         f = float(0)
        if str(p).replace('.0','') == update.message.text.split(" ")[2]:
           time.sleep(2)
           update.message.reply_video("🚩🚩 𝕋𝔼𝔸𝕄 𝔸𝕃𝕃 𝕆𝕌𝕋 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
           break
        if str(q).replace('.1','') == update.message.text.split(" ")[1]:
          time.sleep(2)
          update.message.reply_video("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        time.sleep(3) 
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
