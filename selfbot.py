import discord

client = discord.Client(chunk_guilds_at_startup=False)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    
    owned_servers = [guild for guild in client.guilds if guild.owner_id == client.user.id]
    
    print(f'Connected as {client.user}')
    print(f'Servers: {len(client.guilds)}')
    print(f'Owned servers: {len(owned_servers)}')
    print(f'Friends: {len(client.friends)}')

client.run('TOKEN_HERE')
