from telethon import events
from .. import bot
from telethon.tl.custom import Button 

import asyncio
import openai

openai.api_key = " "
#openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern = "(?i)/ask"))
async def _gpt(event):  
  sender_id = event.sender_id 
  gpt_msg = "hello i am your problem solver"
  await bot.send_msg(sender_id, gpt_msg)