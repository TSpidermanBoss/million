import logging
import asyncio
from telethon import TelegramClient, events
import config
logging.basicConfig(level=logging.INFO)
async def main():
 client = TelegramClient("i", 814511,"44462f0f278503255d5cc30941b617a9")
 msg_ids = {}
 @client.on(events.NewMessage(-1001262096355))
 async def from_fwd(e):
  f = False
  words = [' id','स','dekho','TRUST','fix','😱','😳','👆','👇','pass','chase','link','suno','loss','audio','open','paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','🥺','member','only','chut','lund','tennis','teen','lavde','chutiya','☝️','bc','❓','kya','line','https://','😂','🤔','LUND','WICKET LU','?','loda','telegram','chor','join',"kama","lakh","report","kitna"]
  for word in words:
   if word.casefold() in e.message.text.casefold():
    f = True
  if not f:
   z = await e.client.send_message(-1001378725482,e.message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶"))
   msg_ids[e.id] = z
 @client.on(events.MessageEdited(-1001262096355))
 async def fwd_edit(e):
  if e.id not in msg_ids:
   return
  await msg_ids[e.id].edit(e.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶"), file=e.media)
 await client.start()
 await client.run_until_disconnected()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
