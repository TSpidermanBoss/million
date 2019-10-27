from pyrogram import Client, Filters
import time
import asyncio
async def main():
 msg_ids = {}
 app = Client(session_name="llx",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token ="765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc")
 d = -1001315425757
 s = -1001203491308
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
  if not Message.message_id in msg_ids:
   return
  try:
   if Message.text == ".":
    Message.delete(msg_ids[Message.message_id])
   else:
    client.edit_text(d,msg_ids[Message.message_id],Message.text.markdown)
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
