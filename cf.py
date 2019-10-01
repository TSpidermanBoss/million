import logging
import asyncio
from telethon import TelegramClient, events
import config
logging.basicConfig(level=logging.INFO)
async def main():
 client = TelegramClientClient("m",488556,"c722b7aadbf8b72109b2f96f30974c6d")
 msg_ids = {}
 @client.on(events.NewMessage(-1001203491308))
 async def from_fwd(e):
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
