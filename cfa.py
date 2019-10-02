import logging
import asyncio
from telethon import TelegramClient, events
logging.basicConfig(level=logging.INFO)
async def main():
 client = TelegramClient("sn",771202,"28eed966b0cd4238a4f4f8f0ab4c9c72")
 msg_ids = {}
 @client.on(events.NewMessage(-1001492008965))
 async def from_fwd(e):
  z = await e.client.send_message(-1001330100294,e.message.text)
  msg_ids[e.id] = z
 @client.on(events.MessageEdited(-1001492008965))
 async def fwd_edit(e):
  if e.id not in msg_ids:
   return
  await msg_ids[e.id].edit(e.text,file=e.media)
 await client.start()
 await client.run_until_disconnected()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
