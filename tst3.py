from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client(session_name="llx",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token ="765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc")
d = -1001315425757
s = -1001203491308
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 mes = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
 with open("sure txt", "r") as f:
  x = f.readlines()
 y = [j for j in x[0].split(" ")]
 del y[:2]
 print(y)
 y = " ".join(str(x) for x in y)
 open("sure.txt","w").write(y + " " +str(Message.message_id) + " " + str(mes.message_id)).close()
  
  
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
    client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
   except FloodWait as e:
    time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done") 
app.run()
