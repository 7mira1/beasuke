from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
    # Bot からのメッセージには反応しない
    # この判定をしないと無限ループが起きる
        return

    if "ととろ" in message.content:
        await message.channel.send("ナナミさーん、ととろいるよ🥺")

bot.run(config.TOKEN)