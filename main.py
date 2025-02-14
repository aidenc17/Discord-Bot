import discord 

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}') #prints bots user name when working

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default() #new instance of intents
intents.message_content = True # enable the message_content intent

client = Client(intents=intents) #new instance w specified intents
token = None
with open('.env.txt', 'r') as file:
    token = file.read().strip() 
client.run(token)