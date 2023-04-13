# A guide to bot commannds!
When you are making your bot you want to be able to have commands otherwise its kind of pointless.
Here's what a command looks like:
```py
@bot.gateway.command
def Example(resp):
  if resp.event.message:
    m = resp.parsed.auto()
    if m.get('content') == prefix + 'example':
      channel_id = m['channel_id']
      guild = m['guild_id']
      messageID = m['id']
      bot.reply(guild, channel_id, messageID, 'This is only an example command.') #replies to command message
```
or
```py
bot.gateway.command
def Example(resp):
  if resp.event.message:
    m = resp.parsed.auto()
    if m.get('content') == prefix + 'example':
      channel_id = m['channel_id']
      bot.sendMessage(channel_id ,"This is only an eaxample command") #sends message in response to command (does not reply to the message)
```
We aren't fully sure how to add arguemnts but here is some code for a command for arguemnts.
```py
bot.gateway.command
def Example(resp):
    if resp.event.message:
      m = resp.parsed.auto()
      content = m.get('content')
      channel_id = m['channel_id']
        if content.startswith('!help')
          if '1' in content:
            bot.sendMessage(channel_id ,"This is for message one") 
          elif '2' in content:
            bot.sendMessage(channel_id, 'this is for messgae 2')
    ```