from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("mnnnnnnn",488556,"c722b7aadbf8b72109b2f96f30974c6d")
s = -1001146486274
d = -1001378725482
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   f = True
 if not f:
  if "🎾" in Message.text:
   mes = client.send_message(d,"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "🎾" + "</b>",parse_mode= "html")
  else:
   mes = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
  with open("sure.txt", "r") as f:
   x = f.readlines()
  y = [j for j in x[0].split(" ")]
  del y[:2]
  y = " ".join(str(x) for x in y)
  o = open("sure.txt","w")
  o.write(y + " " +str(Message.message_id) + " " + str(mes.message_id))
  o.close() 
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
    if "🎾" in Message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "</b>" + "🎾",parse_mode="html")
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
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
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done") 
app.run()
