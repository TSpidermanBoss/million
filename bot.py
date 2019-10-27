from pyrogram import Client, Filters
import time
import asyncio
async def main():
 msg_ids = {}
 app = Client("baaz",869912,"a7b049e08df35464047d57e5134327e5")
 d = -1001270940954
 s = -1001262096355
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
  client.edit_message_text(d,msg_ids[Message.message_id],Message.text.markdown)
  @app.on_deleted_messages(Filters.chat(s))
  def main(client, messages):
   if not Message.message_id in msg_ids:
    return
   client.delete_messages(d,msg_ids[Message.message_id])
 app.run()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
