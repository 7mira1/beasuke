from discord.ext import commands
import config
import asyncio
import discord
import random

#bot = commands.Bot(command_prefix="!")
client = discord.Client()

random_name = ["おはし","ととろ","とんかつ"]

@client.event
async def on_ready():
    print("on_ready")

@client.event
async def on_message(message):
    if message.author == client.user:
    # Bot からのメッセージには反応しない
    # この判定をしないと無限ループが起きる
        return

    if "あざといのは？" in message.content:
        content = random.choice(random_name)
        await message.channel.send(content)

    if "ととろ" in message.content:
        await message.channel.send("ナナミさーん、ととろいるよ🥺")

    if "扉" in message.content:
        if client.user != message.author:
            role = discord.utils.get(message.guild.roles, name='扉')
            await message.author.add_roles(role)

    if "!delete" in message.content:
        if message.author.guild_permissions.administrator:
            await message.channel.send('削除するぞ')
            await message.channel.purge()
        else:
            await message.channel.send('消せないぞ')

 #   await client.process_commands(message)

#@client.command()
#async def delete(ctx):
#    await ctx.send('削除するぞ！')
#    await ctx.channel.purge()

@client.event
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

client.run(config.TOKEN)