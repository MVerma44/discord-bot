import discord
import aiohttp
import datetime
import random
import requests
import json
from api import *
from alive import keep_alive

client = discord.Client()

user_inp = ["gg hello", "gg hii", "gg hi", "gg gm", "gg namaste", "gg namaskar", "gg bot", "gg yo", "gg yoo", "gg hey",
            "gg hola", "gg what's up", "gg dude", "gg what's up dude", "gg ciao", "gg pranam", "gg ram ram",
            "gg radhe radhe",
            "gg mahankal", "gg bhole"]

bot_reply = ["Hello!", "Hii", "CIAO", "Hey Buddy!", "Heya, how's it going?", "Hey, What's up?", "Good to see you",
             "Great to see you", "Glad to see you", "Look who it is!", "Nice to see you again", "Hi there",
             "Long time no see",
             "Howdy-doody!", "Hiya!", "Howdy, howdy, howdy!", "Yoo!", "Cool dude!", "Hola", "Bonjour", "Namaste",
             "Namaskar", "What's going on?", "Doing OK", "Everything Alright!", "Radhe Radhe", "Pranam"]


#   TO GIVE THE RANDOM INSPIRATIONAL QUOTES
def quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.content)
    quo = "*" + json_data[0]['q'] + "*\n-**" + json_data[0]['a'] + "**"
    return quo


@client.event
async def on_ready():
    print('Sir, {0.user.name}'.format(client), 'is ready to follow your commands')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if any(word in msg for word in user_inp):  # BOT WILL RESPOND TO HI HELLO MESSAGES
        await message.channel.send(random.choice(bot_reply) + '   {0.author.mention}'.format(message))

    # TO SEND THE QUOTE TO THE OUTPUT
    if message.content.lower() == "gg quotes" or message.content.lower() == "gg quote":
        quo = quote()
        embed = discord.Embed(
            colour=discord.Colour.random(),
        )
        embed.add_field(name="***Quote requested***  !", value=quo)
        await message.reply(embed=embed)

    # TO SEND THE RANDOM JOKES
    if message.content.lower() == ('gg jokes'):
        with open('jokes.txt') as file:
            content = file.read().splitlines()
            embed = discord.Embed(colour=discord.Colour.random())
            embed.add_field(name="***Jokes requested***  !", value=random.choice(content))
            await message.reply(embed=embed)

    # TO RETURN THE CURRENT TIME
    if message.content.lower() == "gg time":
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S  %p")
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="***Current time***", value=current_time)
        await message.reply(embed=embed)

    # TO RETURN THE TODAY'S DATE
    if message.content.lower() == "gg date":
        d = datetime.date.today()
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="***Today's Date***", value=d.strftime("%A %d %B %Y"))
        await message.reply(embed=embed)

    # TO PRINT THE LIST OF TEAM MATES
    if message.content.lower() == ("gg mates"):
        embed = discord.Embed(
            title='***Team Members***',
            description="",
            colour=discord.Colour.random()
        )
        embed.add_field(name="***Mentor's***", value="Mayank Verma\nMihi Pal\nMukta Gupta\nKalash Jain\nVarun Sen\n")
        embed.add_field(name="***Content Designer***", value="Harsh Seth\nJanhvi Matkar\nManas Gupta\n", inline=False)
        embed.add_field(name="***Social Media Handler's***", value="Dishika Jain\nPratyush Gupta\n", inline=True)
        embed.add_field(name="***Server Designer***", value="Ishaan Shivhare", inline=False)
        embed.add_field(name="***Management***", value="Amitesh Sharma\nDishika Jain\nPratyush Gupta\n", inline=True)
        await message.reply(embed=embed)

    # TO SEND THE RANDOM IMAGES FROM FILE
    if message.content.lower() == ("gg image"):
        ran_image = random.choice(images)
        await message.reply(ran_image)

    # TO VIEW ALL THE COMMANDS THAT BOT CAN PERFORM
    if message.content.lower() == ("gg cmd"):
        embed1 = discord.Embed(
            title='***Command List***',
            description='1. gg hii, hello, dude, ciao, hola\n2. gg date\n3. gg time\n4. gg quotes\n5. gg memes'
                        '\n6. gg mates\n7. gg jokes\n8. gg image\n9. gg trivia',
            colour=discord.Colour.red()
        )
        await message.reply(embed=embed1)

    #  SEND RANDOM MEMES FROM THE API
    if message.content.lower() == ("gg meme") or message.content.lower() == ("gg memes"):
        await message.reply(embed=await ran_meme())

    #  HOW TO CONTACT US
    if message.content.lower() == ("gg contacts"):
        embed = discord.Embed(
            title='Follow us',
            description='***[Instagram](https://instagram.com/0_guru_ghantal_0?utm_medium=copy_link)***\n***[YouTube](https://www.youtube.com/channel/UCsJmG3QnL-6wrOrRxEQFNvA)***'
                        '\n***[Website](https://gurughantal.godaddysites.com/class-12)***',
            colour=discord.Colour.random()
        )
        embed.set_image(url='https://i.ibb.co/5r56cSL/gg-logo.jpg')
        await message.reply(embed=embed)

    # TO SEND RANDOM TRIVIA FROM API
    if message.content.lower() == "gg trivia":
        res = requests.get(random.choice(trivia_api))
        data = res.json()
        val = data["results"][0]["question"] + "\n**Answer: **" + data["results"][0]["correct_answer"]
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="***Trivia Enjoy !***", value=val)
        await message.reply(embed=embed)


async def ran_meme():
    pymeme = discord.Embed(title="Meme requested", description="Enjoy !", color=discord.Colour.random())
    async with aiohttp.ClientSession() as cs:
        async with cs.get(api) as r:
            res = await r.json()
            pymeme.set_image(url=res['image'])
            return pymeme
        await ran_meme()


keep_alive()
client.run(Token)
