import logging
import asyncio
from telethon import TelegramClient, events
import config
logging.basicConfig(level=logging.INFO)
async def main():
 client = TelegramClient("m",488556,"c722b7aadbf8b72109b2f96f30974c6d")
 msg_ids = {}
 @client.on(events.NewMessage(-1001203491308))
 async def from_fwd(e):
  f = False
  words = ["kab","mani"," id","स",'dekho',"TRUST",'fix','😱','😳','👆','👇','match','pass','chase','defend','Surendra','karva','link','loss','audio','varna','open','paid','contact','baazigar','market','load','whatsapp','book','teen','diya','bhai',"🐴",'🥺','🖕','member','only','chut','lund','gand','ma ','maa ','bhosdi','bahan','loude','lode','lavde','chutiya','☝️','mkc','bc','madarchod','bahanchod','gandu','❓','kya','line',"https://",'bullet','🤔','LUND'," LU","?","loda","lode","lodu","telegram","chor","join"]
  for word in words:
   if word.casefold() in e.message.casefold():
    f = True
  if not f:
   z = await e.client.send_message(-1001315425757, e.message)
   msg_ids[e.id] = z
 @client.on(events.MessageEdited(-1001203491308))
 async def fwd_edit(e):
  if e.id not in msg_ids:
   return
  await msg_ids[e.id].edit(e.text, file=e.media)
 await client.start()
 await client.run_until_disconnected()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
