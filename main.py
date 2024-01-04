import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'/{file_name}')
            await ctx.send(f'file telah disimpan di=./{file_name}')
            hasil = get_class('keras_model.h5','label.txt', file_name)

            if  hasil[0] == 'turtle\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah penyu')
                await ctx.send('makanan penya adalah tumbuhan')
            elif  hasil[0] == 'turtoise\n' and hasil[1] >= 0.6:
                await ctx.send('ini adalah kura-kura')
                await ctx.send('makanan kesukaan kura-kura adalah buah dan sayur')
            else:
                await ctx.send('gambar tidak valid')

    else:
        await ctx.send('TIDAK ADA FILE YANG DIKIRIM')

bot.run("TOKEN DISCORD")


