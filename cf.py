import logging
import asyncio
from telethon import TelegramClient, events
import config
logging.basicConfig(level=logging.INFO)

async def main():
	client = TelegramClient('ses', config.api_id, config.api_hash)
	msg_ids = {}

	@client.on(events.NewMessage(chats=config.from_channel))
	async def from_fwd(e):
		z = await e.client.send_message(config.to_channel, e.message)
		msg_ids[e.id] = z

	@client.on(events.MessageEdited(chats=config.from_channel))
	async def fwd_edit(e):
		if e.id not in msg_ids:
			return
		await msg_ids[e.id].edit(e.text, file=e.media)

	await client.start()
	await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
