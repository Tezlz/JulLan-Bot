import discord

client = discord.Client(intents=discord.Intents.all(), command_prefix="/")


@client.event
async def on_ready():
    print(f"Logged on as {client.user}")


@client.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")

client.run(open("client.secret", "r").read())
