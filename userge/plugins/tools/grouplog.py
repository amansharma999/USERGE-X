#made by @xcruzhd2
import asyncio
from pyrogram.errors import FloodWait 
from pyrogram import filters
from userge import userge
chatid= (-1001484517886)
@userge.on_message(filters.text&filters.chat('@xcruz_drive'))
async def group_logger(_,x):
	await x.forward(chatid)
	id = x.from_user.id
	name = x.from_user.first_name
	uname = x.from_user.username
	text = x.text
	link = f'https://t.me/{x.chat.username}/{x.message_id}'
	message = f'<b>User: </b>{name}\n<b>Username: </b>@{uname}\n<b>USER ID: </b>{id}\n<b>TEXT : </b>{text}\n<b>Message Link: </b><code>{link}</code>'
	await _.send_message(chat_id = chatid, text = message, parse_mode = 'html' )
