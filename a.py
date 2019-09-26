from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client ("a",930967,"f3dc75e1800f83326194f5d9195c2455")
s = -1001262096355
d = -1001492008965
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client, message):
 f = False
 words = [' id','स','dekho','TRUST','fix','😱','😳','👆','👇','pass','chase','link','suno','loss','audio','open','paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','🥺','member','only','chut','lund','tennis','teen','lavde','chutiya','☝️','bc','❓','kya','line','https://','😂','🤔','LUND','WICKET LU','?','loda','telegram','chor','join',"kama","lakh","report","kitna"]
 for word in words:
  if word.casefold() in message.text.casefold():
   f = True
 if not f:
  mes = client.send_message(d,message.text)
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
    client.edit_message_text(d,int(x[x.index(id)+1]),message.text)
   except FloodWait as e:
    time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("001 002")
  files.close()
  message.reply("Cleared") 
app.run()
