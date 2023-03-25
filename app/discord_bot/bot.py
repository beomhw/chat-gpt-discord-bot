from dotenv import load_dotenv
import discord
import os
from app.open_ai.chat_gpt import chatgpt_response

load_dotenv()

discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as : ", self.user.name)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

        command, user_message = None, None
        for text in ['/ai','/bot','/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)