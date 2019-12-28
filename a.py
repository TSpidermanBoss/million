from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client("122",1160852,"9e5b4b20c3d25f7027b183cb57f917ca")  
d = -1001333049532
s = -1001262096355
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   return 
 mes = client.send_message(d,Message.text.markdown.replace("🖲","🇨🇭").replace("📟","🏝").replace("🇩🇪","🇭🇳")).message_id
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
    client.edit_message_text(d,msg_ids[Message.message_id],Message.text.markdown.replace("🖲","🇨🇭").replace("📟","🏝").replace("🇩🇪","🇭🇳").markdown) 
   except FloodWait as e:
    time.sleep(e.x)
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for Message in messages:
  if not Message.message_id in msg_ids:
   return
  client.delete_messages(d,msg_ids[Message.message_id])
app.run()
