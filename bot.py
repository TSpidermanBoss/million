from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
import asyncio
async def main():
 msg_ids = {}
 app = Client("mnnn",768402,"f6420bf67303614279049d48d3e670f6")
 d = int(input("Destination Chat : "))
 s = int(input("Source Chat : "))
 @app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
 def forward(client,Message):
  words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
  for word in words:
   if word.casefold() in Message.text.casefold():
     return 
  z = client.send_message(d, Message.text.markdown).message_id
  msg_ids[Message.message_id] = z
 @app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
 def forward(client,Message):
  print(msg_ids)
  if not Message.message_id in msg_ids:
   return
  try:
   if Message.text == ".":
    Message.delete(msg_ids[Message.message_id])
   else:
    client.edit_message_text(d,msg_ids[Message.message_id],Message.text.markdown)
  except FloodWait as e:
   time.sleep(e.x)
  @app.on_deleted_messages(Filters.chat(s))
  def main(client, messages):
   if not Message.message_id in msg_ids:
    return
   Message.delete(d,msg_ids[Message.message_id])
 app.run()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
