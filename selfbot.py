import discord

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd) # Do not disturb
    print(f'Connected as {client.user} !')

client.run('TOKEN_HERE')