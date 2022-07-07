from math import floor as down  # , ceil as up
from random import choice
from time import time as epoch
from discord.ext import tasks
import discord
from discord.ext import commands


async def dm_user(user, content=None, embed=None, dels_after=None):
    dm_channel = user.dm_channel
    if dm_channel is None:
        dm_channel = user.create_dm()
    if dm_channel:
        await dm_channel.send(content, embed=embed, delete_after=dels_after)


async def forbidden_error(ctx):
    text = ('im missing permissions\n to solve this enable embed links ' +
            f'on my role and say `message.perms`' +
            ' and enable the things listed here except administrator')
    await dm_user(ctx.author, dels_after=60, content=text)


class SuperCount:
    def __init__(self, file):
        self.file = file

    def add(self, amount=1):
        with open(self.file, 'r') as f:
            inside = f.read()
        inside = int(inside) + amount
        with open(self.file, 'w') as f:
            f.write(str(inside))
        return inside


invite_last_created = 0
bot = commands.Bot(command_prefix='give ')
memey_version = SuperCount(r'version_meme.txt').add(1)

TOKEN = '' # paste your bot token
channel_topics = [
    'whats you favorite artist? how goods is he?',
    'which meme is the best? ||honey bee face meme|| , ||rickroll|| , ||stick bugged|| , ||memenade|| , ||Qin2007||',
    'whats you favorite meme?',
    'what is the reason you are here?',
    'Who was the first band or musician you were really into? Do you still like them?',
    'What outdoor activity haven’t you tried, but would like to?',
    'What’s the most embarrassing thing you did?',
    'What was the last movie you watched? How was it?',
    'If you could call up anyone in the world and have a one-hour conversation, who would you call?',
    'ever build a bot? how was the experience?'
]
meme_links = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ',
              'https://cdn.discordapp.com/attachments/951781029989998612/951781767164096552/HoneyBeeFaceMeme.png',
              # sprint memes
              'https://i.redd.it/1meyqlnuhqm81.jpg',
              ]

dcda_links = ['https://media.discordapp.net/attachments/927255879361921104/931964820977242132/file.gif',
              'https://tenor.com/view/did-you-know-no-one-gif-24072009']  # dont care dint ask
screenshot_time_links = [  # screen shot challange links
    'https://media.discordapp.net/attachments/427559290153467916/932342448590557255/image0.gif',
    'https://media.discordapp.net/attachments/427573109600550919/935483361026277386/ezgif-5-fc2d21fbf7-3.gif'
]
emb_fail_links = [  # epic embed fail
    'https://tenor.com/view/embed-fail-epic-epic-embed-fail-gif-21570335',
    'https://tenor.com/view/epic-embed-fail-epic-embed-fail-gif-epic-embed-embed-fail-embed-epic-gif-24349427',
    'https://tenor.com/view/epic-embed-fail-embed-discord-embed-rage-gif-21044991',
    'https://tenor.com/view/epic-embed-fail-embed-fail-fail-embed-epic-gif-22512028'
]
rickroll_links = [
    'https://tenor.com/view/rick-astly-rick-rolled-gif-22755440',
    'https://tenor.com/view/rickroll-gif-20435173',  # stick bug
    'https://tenor.com/view/attempting-to-get-a-life-rickroll-gif-21335821'
]
ban_apeals = [  # fake ban appeals
    'you spammed for party mode',
    'your cat steppped on a keyboard and said a basic swear word',
    'dumb moderators just banned you', 'youre sus',
    'impostor sus', 'you watched too much discord',
    'a :star:'
]


def convert_instance_to_str(emoji_arg):
    return str(emoji_arg)


def perm_thing(emoji_str, perm_name):
    return f'\n{emoji_str} : {perm_name} ,'


def calculate_emoji_for_perms(t, n, f, perm):
    if perm:
        return t
    elif perm is None:
        return n
    else:
        return f


def short_perm_thing(name, perm, client):
    emoji = {
        1: discord.utils.find(lambda m: m.name == 'BotDislike', client.get_guild(943489205546401842).emojis),
        2: discord.utils.find(lambda m: m.name == 'BotNeutral', client.get_guild(943489205546401842).emojis),
        3: discord.utils.find(lambda m: m.name == 'BotLike', client.get_guild(943489205546401842).emojis)
    }
    emoji_true_ = convert_instance_to_str(emoji_arg=emoji[3])
    emoji_none_ = convert_instance_to_str(emoji_arg=emoji[2])
    emoji_false = convert_instance_to_str(emoji_arg=emoji[1])
    return perm_thing(emoji_str=calculate_emoji_for_perms(emoji_true_, emoji_none_, emoji_false,
                                                          perm),
                      perm_name=name.replace('_', ' '))  # + '\n'


def add_str(perms, client):
    local_perms = perms
    return (short_perm_thing("create_instant_invite", local_perms.create_instant_invite, client) +

            # short_perm_thing("kick_members", local_perms.kick_members, client) +

            # short_perm_thing("ban_members", local_perms.ban_members, client) +

            short_perm_thing("administrator", local_perms.administrator, client) +

            # short_perm_thing("manage_channels", local_perms.manage_channels, client) +

            # short_perm_thing("manage_guild", local_perms.manage_guild, client) +

            short_perm_thing("add_reactions", local_perms.add_reactions, client) +

            short_perm_thing("read_messages", local_perms.read_messages, client) +

            short_perm_thing("send_messages", local_perms.send_messages, client) +

            short_perm_thing("manage_messages", local_perms.manage_messages, client) +

            short_perm_thing("embed_links", local_perms.embed_links, client) +

            # short_perm_thing("attach_files", local_perms.attach_files, client) +

            short_perm_thing("read_message_history", local_perms.read_message_history, client) +

            # short_perm_thing("mention_everyone", local_perms.mention_everyone, client) +

            short_perm_thing("external_emojis", local_perms.external_emojis, client) +

            # short_perm_thing("use_voice_activation", local_perms.use_voice_activation, client) +

            short_perm_thing("change_nickname", local_perms.change_nickname, client) +

            short_perm_thing("manage_nicknames", local_perms.manage_nicknames, client) +

            short_perm_thing("manage_roles", local_perms.manage_roles, client) +

            # short_perm_thing("manage_permissions", local_perms.manage_permissions, client) +

            short_perm_thing("manage_webhooks", local_perms.manage_webhooks, client) +

            # short_perm_thing("manage_emojis", local_perms.manage_emojis, client) +)
            '')


async def calculate_perms_for_memey_ant(message, client):
    guild_perms = message.guild.me.guild_permissions
    local_perms = message.guild.me.permissions_in(message.channel)
    if local_perms.embed_links:
        local_str = add_str(local_perms, client)
        guild_str = add_str(guild_perms, client)
        return local_str, guild_str


@bot.event
async def on_command_error(ctx, error):
    # print(error, type(error))
    res = 'no response set'
    if isinstance(error, discord.Forbidden):
        await forbidden_error(ctx)
        res = 'None'

    elif isinstance(error, commands.MissingRequiredArgument):
        res = 'missing argument'  # ('you provided too little arguments')

    elif isinstance(error, commands.TooManyArguments):
        res = 'you provided too much arguments'

    elif isinstance(error, commands.BadBoolArgument):
        text = ['yes', 'y', 'true', 't', '1', 'enable', 'on']
        textt = '\'`' + '`\',  \'`'.join(text) + f'`\' count as {True}'

        text = ['no', 'n', 'false', 'f', '0', 'disable', 'off']
        textf = '\'`' + '`\',  \'`'.join(text) + f'`\' count as {False}'

        res = f'{textt}\n{textf}'

    elif isinstance(error, commands.InvalidEndOfQuotedStringError):
        res = 'seems like you didnt quote the end'

    elif isinstance(error, commands.CommandNotFound):
        res = 'to me?\ncommand is not found'

    elif isinstance(error, commands.CommandOnCooldown):
        res = 'cool down'

    elif isinstance(error, RuntimeWarning):
        res = 'i think i for got to await something'

    elif isinstance(error, commands.CommandInvokeError):
        res = (str(error) + '\n says the error')

    elif isinstance(error, discord.HTTPException):  # issubclass(error, discord.HTTPException):
        res = 'HTTPException (ask bot support)'
        # ('something went wrong (i dont know what)\n```\n' + str(type(error)) + '\n```')

    elif isinstance(error, commands.NoPrivateMessage):
        res = 'NoPrivateMessage'

    elif isinstance(error, discord.DiscordException):
        res = ('something went wrong (i dont know what)\n```\n' + str(type(error)) + '\n```')

    else:
        res = 'BotError'
    res = (res + '\n```' + str(error) + '```\n says the error')
    try:  # Exception
        await ctx.reply(res)
    except discord.Forbidden:
        await forbidden_error(ctx)
    # print('just print',file=sys.stderr)


@bot.command(brief='my version')
async def version(ctx):
    embed = discord.Embed(title=f'{bot.user.name}\'s version',
                          description='the current version is' + f' `{memey_version}`',
                          color=discord.Color.random())

    await ctx.reply(embed=embed, content=f'"`{bot.user.name}`"\'s version')


@tasks.loop(minutes=15)
async def send_topic():
    channel = await bot.fetch_channel(961286466313543731)
    try:
        mgs = await channel.send(choice(channel_topics))
        await mgs.publish()
    except discord.Forbidden as the_error:
        print(the_error)
    except discord.HTTPException as the_error:
        print(the_error)
        print('i think cool down')
    # print('hello world')


send_topic.start()


@bot.command(brief='dont care didnt ask')
async def dcda(ctx):
    await ctx.reply(choice(dcda_links))


@bot.command(brief='memes can be submited at support')
async def meme(ctx):
    await ctx.reply(choice(meme_links))


@bot.command(brief='epic embad fails')
async def embedfail(ctx):
    await ctx.reply(choice(emb_fail_links))


@bot.command(brief='gives a screenshottime')
async def screenshottime(ctx):
    await ctx.reply(choice(screenshot_time_links))


def isowner_server(ctx):
    return bool(ctx.guild.id == 951768916030533662)


#
# @bot.command(brief='make a fake appeal')
# @commands.check(isowner_server)
# async def fakeban(ctx):
#     await ctx.reply('please only fake an appeal on a dedicated fake appeal forum\n```\n'+choice(ban_apeals)+'\n```')


@bot.command(brief='never gonna give you up, never gonna let you down')
async def rickroll(ctx):
    await ctx.reply(choice(rickroll_links))


@bot.command(brief='follow a secret channel',
             description='follow a secret channel\n#topics-memey to be exact\n(from support server)')
@commands.has_permissions(manage_webhooks=True)
@commands.bot_has_permissions(manage_webhooks=True)
@commands.cooldown(rate=1, per=60 * 5, type=commands.BucketType.guild)
# @commands.has_role('MemersFollow')
async def follow(ctx):
    if True:  # ctx.guild.owner_id == ctx.author.id or userhasrole(ctx.author, 'MemersFollow'):
        channel = await bot.fetch_channel(961286466313543731)
        await channel.follow(destination=ctx.channel, reason=f'{ctx.author.name} wanted to follow')
        await ctx.reply('DONE!')
    # ctx.reply('turnd off globaly by dev')


@bot.command(brief='give server info')
async def serverinfo(ctx):
    guild = ctx.guild
    emb = discord.Embed(title='server info',
                        description='info about the server')
    emb.add_field(name='basic info', value=f'name="`{guild.name}`", icon_url="`{guild.icon_url}`"')
    emb.set_thumbnail(url=guild.icon_url)
    # await user.send(content='message derect to user', delete_after=15)

    if 'VANITY_URL' in guild.features:
        if guild.me.guild_permissions.manage_guild:
            invite = await guild.vanity_invite()
            emb.add_field(name='vanity url', value=f'url={invite}')
        else:
            emb.add_field(name='vanity url', value='i need the manage_guild to get the info')
    if 'BANNER' in guild.features:
        emb.set_image(url=guild.banner_url)
    boosts = ctx.guild.premium_subscription_count
    boost_lvl = ctx.guild.premium_tier
    if boost_lvl > 0:
        emb.add_field(name='boosts', value=f'this guild has `{boosts}` boosts\nand level `{boost_lvl}`')
    else:
        emb.add_field(name='boosts', value=f'field locked `{boosts}` boosts')
    await ctx.reply(embed=emb, content=f'looking up "`{guild.name}`"')


@commands.command(description='view the bots perms,' +
                              'admin is never required but is helpfull bypass Forbidden errors',
                  # 'to not show `bot break dms`',
                  aliases=['perms', 'permissions'],
                  brief='view the bots perms')
async def calculate_perms(ctx):
    message = ctx.message
    # guild_perms = message.guild.me.guild_permissions
    local_perms = message.guild.me.permissions_in(message.channel)
    if local_perms.embed_links:
        local, guild = await calculate_perms_for_memey_ant(message, bot)
        l_emb = discord.Embed(title='my channel perms', description=local)
        g_emb = discord.Embed(title='my server perms ', description=guild)
        await message.channel.send(message.author.mention, embed=l_emb)
        await message.channel.send(message.author.mention, embed=g_emb)
        # await message.reply('currently disabled')


@bot.command(brief='invite to support')
async def support(ctx):
    global invite_last_created
    epoch_time = down(epoch())
    # seconds_until_ready = epoch_time - invite_last_created
    seconds_cooldown = 60 * 10

    seconds_until_ready = epoch_time - invite_last_created
    if seconds_until_ready > seconds_cooldown:
        invite_last_created = epoch_time
        await ctx.reply('Qin2007s bot support=https://discord.gg/jMaD9gjNkj')
    else:
        await ctx.reply('cant do it now, try <t:' + str(epoch_time + seconds_cooldown) + ':R> , ' +
                        '<t:' + str(epoch_time + seconds_cooldown) + ':T>')


@bot.command(brief='force to send a channel topic(only bot owner)')
@commands.is_owner()
async def force_send(ctx):
    if ctx.author.id == 894198592670158898:
        await send_topic()
        await ctx.reply('done!')
    else:
        await ctx.reply('not for you')


@bot.command(brief='makes the bot leave the server')
async def leave(ctx):
    appinfo = await bot.application_info()
    appid = appinfo.id

    descr = f'\n```{appinfo.description}```'
    icon_url = 'https://cdn.discordapp.com/avatars/894198592670158898/060fc0a3dc52023fced2bb1d25384e2c.webp?size=1024'
    embed = discord.Embed(title=bot.user.name, description=descr)
    embed.add_field(name='invite me back',
                    value=discord.utils.oauth_url(client_id=str(appid),
                                                  permissions=discord.Permissions(536955904)
                                                  ))
    embed.set_author(name='Qin2007#7826',
                     icon_url=icon_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    await ctx.reply(embed=embed)
    await ctx.guild.leave()


bot.run(TOKEN)
