#bot functionality code
import discord
from discord.ext import commands
import json
import random
from discord.ext.commands.help import MinimalHelpCommand
import requests
from requests import get
import os

#consts
true_false_responses = [
  "Is the sky blue?", 
  "Is that even a question lol? Sure XD", 
  "Yesh", 
  "OfCourse!", 
  "Why not?", 
  "Definately not NO", 
  "Nice question, tho I suggest you ask me later when I'm done with Ayam's Mom.", 
  "Definately not", 
  "NO.", 
  "Are u dum?", 
  "Nope", 
  "I would say yes, but Tommy(my dog) says no so....", 
  "I’m too lazy to even breath(wait discord bots dont actually breathe....nvm), so why would you ask that of me?!"
]  

bot = commands.Bot(command_prefix="&") #setting a universal bot prefix & init

@bot.event #notifying myself that bot be active  
async def on_ready():
  print("All set for launch! {0.user}".format(bot))  


#commands
@bot.command() #making sure lolli is alive
async def hi(ctx):
  await ctx.reply("Sup man!")

@bot.command() #bot ping
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency)*1000}ms')  
 
@bot.command() #getting quote thru api told by famouse peepal
async def quote(ctx):
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0] ['q'] + "\n- " + json_data[0] ['a']
  await ctx.reply(quote) 

@bot.command(aliases=["ToF", "tof", "truefalse", "TrueorFalse", "TrueFalse"])  #true or false 
async def _8ball(ctx, *, question):
   await ctx.send(f'Question: {question}\n Answer: {random.choice(true_false_responses)}')

@bot.command() #memes
async def meme(ctx):
    #content
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content, )
    meme = discord.Embed(
        title=f"{data['title']}",
        Color=discord.Color.random()).set_image(url=f"{data['url']}")
    
    await ctx.reply(embed=meme) #sending the meme in an embed

@bot.command() #kick an annoying user like jeet
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason = reason)  
  await ctx.send(f'{member.mention} was kicked on da ass!\nReason: ') 

@bot.command() #ban a kiddo like sharanya
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason = reason)     
  await ctx.send(f'{member.mention} was banned, suck that cock mf!\nReason :{reason}') 


@bot.command() #unban annoying previously banned people
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split("#")

  for ban_entry in banned_users():
    user = ban_entry.user
 
    if(user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'{member_name}#{member_discriminator} successfully unbanned, though I would prefer them banned.')
      return
 


bot.run("your token")
#client.run(os.environ('TOKEN'))  -- doesnt work yet

