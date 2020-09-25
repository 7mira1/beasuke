from discord.ext import commands
import config
import asyncio
import discord
import random

bot = commands.Bot(command_prefix="!")

random_name = ["おはし","ととろ","とんかつ"]

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
    # Bot からのメッセージには反応しない
    # この判定をしないと無限ループが起きる
        return

    if "あざといのは？" in message.content:
        content = random.choice(random_name)
        await message.channel.send(content)

    if "ととろ" in message.content:
        await message.channel.send("ナナミさーん、ととろいるよ🥺")

    if "扉" in message.content:
        if bot.user != message.author:
            role = discord.utils.get(message.guild.roles, name='扉')
            await message.author.add_roles(role)

    await bot.process_commands(message)

@bot.command()
async def totoro(ctx):
    await ctx.send(f"{ctx.author.name} さん、ととろいるよ🥺")

@bot.command()
async def delete(ctx):
    await ctx.send('削除するぞ！')
    await ctx.channel.purge()

@bot.event
async def on_mention(message):
    if message.author.guild_permissions.administrator:
        mentions = message.mentions
    if not mentions:
        return

    if message.content.startswith('tobira ' + mentions[0].mention):
        member = message.guild.get_member(mentions[0].id)
        role0 = discord.utils.get(message.guild.roles, name="扉")
        await member.add_roles(role0)
        await message.channel.send('○のロールを付与しました')
    else:
        await message.channel.send('Error')

bot.run(config.TOKEN)