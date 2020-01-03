from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("mnnn",bot_token="993042899:AAF3avHrytv1wU_g6wb46prD6W72ZQZKuVk",api_id=768402,api_hash="f6420bf67303614279049d48d3e670f6")
s = -1001428773103
d = -1001170925810
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
    return
 mes = client.send_message(d,"**" + Message.text.replace("🖲","🥌").replace("📟","🏆").replace("🇩🇪","🇾🇪").replace("🎾","⚾") + "**") 
 files = open("sure.txt" , "a")
 files.write(" " + str(Message.message_id) +  " " + str(mes.message_id))
 files.close()  
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client,Message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(Message.message_id)
  if id in x:
   try:
    client.edit_message_text(d,int(x[x.index(id)+1]),"**" + Message.text.replace("🖲","🥌").replace("📟","🏆").replace("🇩🇪","🇾🇪").replace("🎾","⚾") + "**") 
   except FloodWait as e:
    time.sleep(e.x)
@app.on_message(Filters.command("clear"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("")
  files.close()
  message.reply("Done") 


app.run()
