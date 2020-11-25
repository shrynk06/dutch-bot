import discord
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('hello')

    if message.content == 'thanks':
        await message.channel.send('ok')

    if message.content == 'bruh':
        await message.channel.send('bruh')

client.run('Nzc3MTA4NTAxOTM5NzQ4ODY2.X6-osA.y7dvDqRP5jA2ECNqrl30UYEG0fA')
