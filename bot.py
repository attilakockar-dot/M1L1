import discord
from discord.ext import commands
import random
from disappear_times import disappear_times

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_input = message.content.lower().strip()

    if user_input in disappear_times:
        await message.channel.send(f'{message.content} yaklaşık olarak {disappear_times[user_input]} içinde doğada kaybolur.')
    else:
        await message.channel.send('Bu madde hakkında bilgi bulunamadı. Lütfen başka bir madde deneyin.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')



bot.run("")