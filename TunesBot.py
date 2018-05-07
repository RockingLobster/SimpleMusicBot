import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

token = ''


startup_extensions = ["Music"]
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print ("Bot online")
    
class Main_Commands():
        def __init__(self, bot):
         self.bot = bot
        
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hello :thinking: ")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}:'.format(extension, exc))

bot.run(token)
