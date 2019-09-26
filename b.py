from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("i", 814511,"44462f0f278503255d5cc30941b617a9")
s = -1001262096355
d = -1001378725482
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = [" id","स",'dekho',"TRUST",'fix','😱','😳','👆','👇','pass','chase','link','loss','audio','open','paid','contact','baazigar','market','load','whatsapp','book','bhai',"🐴",'😂','member','only','chut",'lund','bhosdi','lavde','chutiya','☝️','bc','❓','kya','line',"https://",'🤔','LUND',"WICKET LU","?","loda","telegram","chor","join"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(d,message.text.replace("TRINBAGO","𝕋ℝ𝕀ℕ𝔹𝔸𝔾𝕆").replace("🖲","🧚‍♂️⛳️").replace("⛳️","",1).replace("🇩🇪","🇮🇩").replace("📟","🥁"))
  files = open("sure.txt" , "a")
  files.write(" " + str(message.message_id) +  " " + str(mes.message_id))
  files.close()  
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client, message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(message.message_id)
  if id in x:
   try:
    client.edit_message_text(d,int(x[x.index(id)+1]),message.text.replace("TRINBAGO","𝕋ℝ𝕀ℕ𝔹𝔸𝔾𝕆").replace("🖲","🧚‍♂️⛳️").replace("⛳️","",1).replace("🇩🇪","🇮🇩").replace("📟","🥁"))
   except FloodWait as e:
    time.sleep(e.x)
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.edit_message_text(d,int(x[x.index(id)+1]),".")
     time.sleep(3)
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("")
  files.close()
  message.reply("Done") 
app.run()
