import os
import fossbotpy
token = os.environ['BotToken']
base_url = 'https://underground.haydar.com/api/v9/'
bot = fossbotpy.Client(token=token, base_url=base_url, log={"console":False})

prefix = '!'

@bot.gateway.command
def example(resp):
  if resp.event.message:
    m = resp.parsed.auto()
    if m.get('content') == prefix + 'example':
      channel_id = m['channel_id']
      guild = m['guild_id']
      messageID = m['id']
      bot.reply(guild, channel_id, messageID, 'This is only an example command.') 


# This is a message logger. This just priints out snedt messgaes the bot can see. This isn't very useful so i commented it out. -LmTechyTEMalt
      
#@bot.gateway.command
#def helloworld(resp):
#    if resp.event.ready:
#        user = bot.gateway.session.user
#        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
#    if resp.event.message:
#        m = resp.parsed.auto()
#        guildID = m.get('guild_id') #dms do not have a guild_id
#        channelID = m['channel_id']
#        username = m['author']['username']
#        discriminator = m['author']['discriminator']
#        content = m['content']
#        print("> guild {} channel {} | {}#{}: {}".format(guildID, channelID, username, discriminator, content))

bot.gateway.run()