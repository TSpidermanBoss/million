from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
import asyncio
async def main():
 msg_ids = {}
 app = Client("ssn",950979,"e3135b7af1cd3681d5e9bad56591ff65") 
 d = -1001421693753
 s = -1001100924541
 @app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
 def forward(client,Message):
  words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
  for word in words:
   if word.casefold() in Message.text.casefold():
     return 
  z = client.send_message(d, "<b> " + Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶") + " </b>",parse_mode="html").message_id
  msg_ids[Message.message_id] = z
 @app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
 def forward(client,Message):
  if not Message.message_id in msg_ids:
   return
  try:
   client.edit_message_text(d,msg_ids[Message.message_id],"<b>" + Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶") + " </b>",parse_mode = "html") 
  except FloodWait as e:
   time.sleep(e.x)
 @app.on_deleted_messages(Filters.chat(s))
 def main(client, messages):
   for Message in messages:
    if not Message.message_id in msg_ids:
     return
    client.delete_messages(d,msg_ids[Message.message_id])
 app.run()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
