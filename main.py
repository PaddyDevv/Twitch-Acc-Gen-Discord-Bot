import os
os.system("pip install selenium==3.141.0")
os.system("pip install webbot")
from webbot import Browser
import time
from time import sleep
import time
import string
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!t')
@bot.event
async def on_ready():
  print("Bot Online!")

user = 'GhostDev_' + ''.join(random.choice(string.ascii_lowercase) for i in range(3))
email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + '@ghostdev.com'
password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(15))

TrovoLink = 'https://twitch.tv/signup'


@bot.command()
async def gen(ctx):
  embed=discord.Embed(title="Creating Twitch Account", description="We Are Currently Creating Your Twitch Acc!", color=0x8000ff)
  embed.set_author(name="Twitch Account Creator", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8Mtk6u84WKnoWg2-bdp1I1jsOHUjquQaNqA&usqp=CAU")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8Mtk6u84WKnoWg2-bdp1I1jsOHUjquQaNqA&usqp=CAU")
  await ctx.send(embed=embed)
  for i in range(1):
    driver = Browser()
    driver.go_to(TrovoLink)
    driver.click('Username')
    driver.type(user)
    driver.click('Password')
    driver.type(password)
    driver.click('Confirm Password')
    driver.type(password)
    driver.click('Month')
    driver.click('November')
    driver.click('Day')
    driver.type('13')
    driver.click('Year')
    driver.type('1999')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.click('Use email Instead')
    driver.click('Email')
    driver.type(email)
    await ctx.send(f"Here Is Your Twitch Account Information\n\n Email: {email}\nPassword: {password}\nUsername: {user}")
    driver.quit

bot.run("TOKEN HERE")

acc = open('acc.txt','w')
acc.write(f"\n" + 'email:{email}:password:{password}:username:{user}' + "\n")
acc.close()
  
