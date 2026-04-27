import discord

client = discord.Client(chunk_guilds_at_startup=False)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd) # Do not disturb
    print(f'Connected as {client.user} !')
    print(f'Servers: {len(client.guilds)}')

client.run('TOKEN_HERE')
