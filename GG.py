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

####################################################################################################################################

import discord
import aiohttp
from keep_alive import keep_alive
import pandas as pd
import random
import requests
import json
import wikipedia

client = discord.Client()

# TOKEN removed for security purposes
TOKEN = 'Your_bot_token'

trivia_api = [
              "https://opentdb.com/api.php?amount=1&category=15" # Video Games
              "https://opentdb.com/api.php?amount=1&category=18", # Science Computer
              "https://opentdb.com/api.php?amount=1&category=30" # Science & Gadgets
             ]

user_input = ["tgb hello", "tgb hii", "tgb hi", "tgb bro", "tgb yo", "tgb yoohoo", "tgb hey", "tgb ola", "tgb wassup", "tgb dude", "tgb what up dude", "tgb ciao", "tgb buddy"]

bot_reply = ["Hello", "Heya", "Ciao", "Hey", "Heya, how's it going", "Hey, wassup", "Good to see you", "Great to see you", "Glad to see you", "Look who it is! It's a bird... it's a plane... it's ", "Nice to see you again", "Hi there","Long time no see","Howdy", "Hiya", "Yoohoo", "Ola", "Bonjour","What's going on","Look who it is. It's"]

wish_morning = ["Rise and shine!", "Top of the morning to you!", "Goos day to you", "Have a great day", "Wishing you the best for the day ahead", "How are you this fine morning?",
                "Isn't it a beatuiful day today?", "Look alive!", "What a pleasant morning we are doing", "Morning!", "Good morning", "Good day"]

wish_afternoon = ["Have a good afternoon and a great day!", "You are as bright as the afternoon sun", "Have an awesome afternoon! thank you for sharing a piece of your heart", "Wishing you a splendid afternoon my one and only!",
                  "This afternoon is a beauty, just like you", "Half of the day is over; have a marvelous afternoon and enjoy the rest of the day!", "i Would like to wish you a good afternoon and an even better evening",
                  "Today, there will be a beautiful sunset after you have a good afternoon!"]

wish_evening = ["Have a nice evening", "Good evening", "Good evening Mayank", "Evening boss", "I hope you are having a refreshing evening as i am having here thinking of you"]

wish_night = ["It was nice to meet you, goodnight!", "Goodnight! see you tomorrow", "It was good to meet you", "I'll catch up with you later", "I'll will see you seen", "Ta-Ta for now"]

li = ['bio of', 'details of', 'about', 'who is', 'info of', 'information of']
nishant = ['nishant gandhi', 'nishant sir']
sarthak = ['sarthak khandelwal', 'sarthak']
samarth = ['samarth sharma', 'samarth']
vipin = ['vipin']
ishika = ['ishika shahaney', 'ishika']
mayank = ['mayank verma', 'mayank']
anushka = ['anushka', 'anushka jain']
aditi_d = ['aditi dandawate', 'aditi d']
aditi_m = ['aditi mandlik', 'aditi m']
raj = ['raj soni', 'raj']
prateeti = ['prateeti jain', 'prateeti']
suchismita = ['suchismita', 'suchismita']
tanisha = ['tanisha', 'tanisha jain']
jasii = ['jassi', 'jaspreet op', 'jaspreet singh saini', 'jaspreet', 'op69']
saud = ['saud hashmi', 'saud']
muskan = ['muskan', 'muskan sogani']
dhanraj = ['dhanraj', 'dhanraj gangrade']

def quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.content)
    quo = "*" + json_data[0]['q'] + "*\n-**" + json_data[0]['a'] + "**"
    return quo

@client.event
async def on_ready():
    print('Ready {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    msge = message.content.lower()
    if any(word in msge for word in user_input):  # BOT WILL RESPOND TO HI HELLO MESSAGES
        await message.channel.send(random.choice(bot_reply) + '   {0.author.mention}'.format(message))

    if message.content.lower() == 'tgb cmd':
        embed = discord.Embed(
            title="***TGB Help/Command list***",
            description=f"{user_input}\ntgb event\ntgb council\ntgb core\ntgb exec\ntgb contacts\ntgb trivia\ntgb play <song name> (Connect to voice channel before using command)\ntgb pause, tgb resume, tgb dc\ntgb quote\n",
            colour=discord.Colour.random()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb event":
        embed = discord.Embed(title="*** \t\t\t\t\t\t\t\t\t\t\t:sparkles:  The Blog Spot  :sparkles:***",

        description='**Contest Alert**  :first_place:  \nMedi-Caps University, ACM student chapter is\nconducting a technical blog writing competition- **“The Blog Spot”\n**', color=discord.Colour.random())


        embed.add_field(name="**Guidelines:  :orange_book:**",
                        value="• Article should be a personal piece that expresses\n your opinion/experience with regards to any technical field.\n• The article should be submitted in a PDF format.\n• Last Date- 16th October, 2021; 11:59 PM.\n• Mail us your article at the following mail address:  ***connectwithMUACM@gmail.com***")

                
        embed.add_field(name="Perks  :sparkles:", 
                        value="Best three articles will be published on MUACM’s social media handles and certificates will be awarded to top 10 write-ups")


        embed.set_image(url=r"https://i.ibb.co/zxMFVVD/mu.png")

        await message.reply(embed=embed)

    
    code = ['bad words']

    msg_content = message.content.lower()
    new = msg_content.split(" ")
    if any(word in new for word in code):
        await message.delete()
        embed = discord.Embed(
            title="***Warning!!!***",
            description="{0.author.mention}".format(message) + "**   If you again use this type of words you will be banned from the sever**",
            colour=discord.Colour.random()
        )
        await message.channel.send(embed=embed)
        
    if message.content.lower() == 'tgb council':
        embed = discord.Embed(
            title="***\t\t\t\t\tCouncil Members***",
            description="***Nishant Gandhi*** >>> Mentor\n***Sarthak Khandelwal*** >>> Mentor\n***Samarth Sharma*** >>> Chairman\n***Vipin Gupta*** >>> Vice-Chairman\n***Saud Hashmi*** >>> Membership Chairperson\n***Ishika Shahaney***  >>> Treasurer & Secretary",
            colour=discord.Colour.from_rgb(138,43,226)
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb core':
        embed = discord.Embed(
            title="***\t\t\t\t\tHead Members***"
            ,
            description="***Aditi Dandawate*** -->  Content & Ideation\n"
            "***Aditi Mandlik*** -->  Social Media & Outreach\n"
            "***Anushka Jain*** -->  Management\n"
            "***Jaspreet Singh Saini*** --> Graphics\n"
            "***Mayank Verma*** -->  Technical\n"
            "***Prateeti Jain*** -->  Junior Coordinator\n"  
            "***Raj Soni*** -->  Marketing\n"
            "***Suchismita Nanda*** -->  Documentation\n"
            "***Tanisha Jain*** -->  Graphics\n",          
        
            colour=discord.Colour.from_rgb(0, 255, 255)
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb exec':
        embed = discord.Embed(
            title="***Executives Members***",
            colour=discord.Colour.green()
        )

        embed.add_field(name='Content and Ideation',
                        value='Muskan Sogani\nSneha Farkya')

        embed.add_field(name='Graphics',
                        value='Arin Bagul\nShriyansh Bargava')
                    
        embed.add_field(name='Management',
                        value='Aastha Khandelwal\nMohammed Murtuza\nRushat Dubey\nVanshika Juneja')

        embed.add_field(name='Marketing',
                        value='Harsh Seth\nMitali Nighoskar\nRicha Deshpande\nRishita Gangwal')                       
        embed.add_field(name='Media & Outreach',
                        value='Aditi Modi\nKrati Sengar')

        embed.add_field(name='Technical',
                        value='Dhanraj Gangrade\nJaskirat Singh Sudan\nMayur Paliwal')

        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb contacts":
        embed = discord.Embed(
            title='***\t\t\t\t\tConnect us on*** !',
            description='**[Instagram](https://instagram.com/mu_acm?utm_medium=copy_link)**\n\n'
                        '**[LinkedIn](https://www.linkedin.com/company/acm-student-chapter-medicaps/)**'
                        '\n\n**[Website](http://medicaps.hosting.acm.org/)**\n\n**[YouTube](https://www.youtube.com/channel/UC5kQv1TB5GVNuttr2LuSKhA)**',
            colour=discord.Colour.orange()
        )
        embed.set_image(url='https://i.ibb.co/YWV5Bx0/Mu-ACMlogo.png')
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb trivia":
        res = requests.get(random.choice(trivia_api))
        data = res.json()
        val = data["results"][0]["question"] + "\n**Answer: **" + data["results"][0]["correct_answer"]
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="**Trivia**", value=val)
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb meme':
        await message.channel.send(embed=await ran_meme())

    if message.content.lower() == "tgb quote":
        quo = quote()
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="Quote:", value=quo)
        embed.set_footer(text="Requested by {0.author.name}".format(message))
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb bio':
        await message.channel.send(tgb_bio(message))

    if 'tgb bio: ' in message.content.lower() and message.content[9] != None:
      code = message.content[9:]
      userid = int(code[3:len(code) - 1])
      await message.channel.send(tgb_bio_with_user(message, userid))

    if ("tgb add bio: " in message.content.lower()) and (message.content[13] != None):
      await message.channel.send(add_bio(message))

    if ("tgb change bio: " in message.content.lower()) and (message.content[16] != None):

      await message.channel.send(change_bio(message))

    query = message.content.lower()
    # query = input("- ").lower()

    if any(word in query for word in li) and any(word in query for word in nishant):
      embed = discord.Embed(title="Co-founder & Mentor of MUACM\nDevOps Engineer with hands over the cloud", colour=discord.Colour.red())
      await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in saud):
        embed = discord.Embed(title='Membership Chairperson at MUACM\nFounder @CSCult\nLoves STEM, Economics and Philosophy\nSpends time building stuff and jamming', colour=discord.Colour.red())
        await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in samarth):
        embed = discord.Embed(title="Chairman at MUACM\nCloud Enthusiast\nWorking for my goals", colour=discord.Colour.red())
        await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in sarthak):
        embed = discord.Embed(title="Ex-Vice Chairman, Founder & Mentor at MUACM\nMachine Learning Geek, Zealot Researcher", colour=discord.Colour.red())
        await message.reply(embed=embed)

    if any(word in query for word in li) and any(word in query for word in muskan):
      embed = discord.Embed(title="Executive member at MUACM\nImproving technical & interpersonal skills\nLove to work on myself", colour=discord.Colour.red())
      await message.reply(embed=embed)       

    if any(word in query for word in li) and any(word in query for word in dhanraj):
      embed = discord.Embed(title="Executive member at MUACM\nWeb Development enthusiastic\nIndulge in Programming", colour=discord.Colour.red())
      await message.reply(embed=embed)    

    if any(word in query for word in li) and any(word in query for word in jasii):
        embed = discord.Embed(title="Coolest member of MUACM\nGraphic designing enthusiast\nIn love with cats\n69", colour=discord.Colour.red())
        await message.reply(embed=embed)

    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        embed = discord.Embed(title="According to Wikipedia", description=results, colour=discord.Colour.random())
        await message.reply(embed=embed)

    if "google" in query:
        query = query.replace("google", "")
        results = wikipedia.summary(query, sentences=2)
        embed = discord.Embed(title="According to Google", description=results, colour=discord.Colour.random())
        #await message.reply(embed=embed)

api = ['https://memes.blademaker.tv/api?lang=hi', 'https://memes.blademaker.tv/api?lang=en']

async def ran_meme():
    pymeme = discord.Embed(title="Meme requested", description="Enjoy !", color=discord.Colour.random())
    async with aiohttp.ClientSession() as cs:
        async with cs.get(random.choice(api)) as r:
            res = await r.json()
            pymeme.set_image(url=res['image'])
            return pymeme
        await ran_meme()

def tgb_bio(message):
  df = pd.read_csv(r'bio.csv')
  user = str(message.author)
  users = list(df['user'].values)
  userid = message.author.id
  if user in users:
      return df[df['userid'] == userid].bio.values[0]
  else:
      rtn = f"No bio found for {user}"
      return rtn

def tgb_bio_with_user(message, userid):

  df = pd.read_csv(r'bio.csv')
  user = str(message.author)
  users = list(df['user'].values)
  userid = message.author.id
  if user in users:
      return df[df['userid'] == userid].bio.values[0]
  else:
      rtn = f"No bio found for {user}"
      return rtn

def add_bio(message):
  df = pd.read_csv(r'bio.csv')
  bio = str(message.content[13:])
  user = str(message.author)
  userid = message.author.id
  users = list(df['user'].values)
  if user in users:
      return 'You already have a bio!'
  df.loc[len(df.index)] = [userid, user, bio]
  df.to_csv(r'bio.csv', index=False)
  return 'Bio added!'

def change_bio(message):
  df = pd.read_csv(r'bio.csv')
  new_bio = str(message.content[16:])
  user = str(message.author)
  userid = str(message.author.id)
  users = list(df['user'].values)
  if user in users:
      df.loc[df.userid == userid, 'bio'] = new_bio
      df.to_csv(r'bio.csv', index=False)
      return 'Bio changed!'
  else:
      rtn = f"No bio found for {user}"
      return rtn

keep_alive()
client.run(TOKEN)

