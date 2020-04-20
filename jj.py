from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  


@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(update.effective_message.text.split(' ')) > 2:
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
         update.message.reply_text(str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾*',parse_mode=ParseMode.MARKDOWN)
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


@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 312525402:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. command('cnnn'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")
app.run()
