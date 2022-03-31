import discord
from discord.ext import commands
import requests
import json

TOKEN = ''

client = commands.Bot(command_prefix = '.')

sad_words = ["sad", "bitter", "heartbroken", "mournfal", "unhappy", "depressed", "suicide"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$happy'):
        quote = get_quote()
        await message.channel.send(quote)

    for word in sad_words:
        if word in msg:
            await message.channel.send("https://kidshelpphone.ca/")
        else:
            pass

client.run(TOKEN)
