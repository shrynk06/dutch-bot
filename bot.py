import discord
from discord.ext import commands
from translate import Translator

bot = commands.Bot(command_prefix="d.")
bot.remove_command("help")


@bot.event
async def on_ready():
  print("Bot Ready")
  activity = discord.Activity(name='d.help', type=discord.ActivityType.listening)
  await bot.change_presence(activity=activity)

@bot.command()     #REPEATS WORD
async def say(ctx, word):
  await ctx.send(word)

@bot.command() #STARTER COMMAND
async def help(ctx):
  embed = discord.Embed(title="Welcome!",
                        color=discord.Color.green())
  embed.set_image(
    url='https://cdn.discordapp.com/attachments/778977927345733702/778978010891681812/Opera_Snapshot_2020-05-19_110825_www.youtube.com.png')

  embed.add_field(name="d.d", value="Converts message from English to Dutch", inline=False)
  embed.add_field(name="d.e", value="Converteert bericht van Nederlands naar Engels", inline=False)
  embed.add_field(name="d.say", value="repeats a word or message", inline=False)
  await ctx.send(embed=embed)

@bot.command()#TRANSLATES TO DUTCH
async def d(ctx,*,m):
  try:

    translator = Translator(from_lang='english', to_lang='dutch')
    result = translator.translate(m)
    msgembed = discord.Embed(title=ctx.author.name,
                             description= result,
                          color=discord.Color.green())
    msgembed.set_thumbnail(url = ctx.author.avatar_url)


    await ctx.send(embed = msgembed)
  except:
    await ctx.send("I do not understand. Please try again")




@bot.command()#TRANSLATES TO ENGLISH
async def e(ctx,*,m):
  try:
    translator = Translator(from_lang='dutch', to_lang='english')
    result = translator.translate(m)
    Msgembed = discord.Embed(title=ctx.author.name,
                             description=result,
                             color=discord.Color.green())
    Msgembed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=Msgembed)
  except:
    await ctx.send("Ik begrijp het niet. Probeer het a.u.b. opnieuw")
bot.run("token")
