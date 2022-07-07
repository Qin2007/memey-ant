pass


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


#
# @bot.event
# async def on_command_error(ctx, error):
#     # print(error, type(error))
#     res = 'no response set'
#     if isinstance(error, discord.Forbidden):
#         await forbidden_error(ctx)
#         res = 'None'
#
#     elif isinstance(error, commands.MissingRequiredArgument):
#         res = 'missing argument'  # ('you provided too little arguments')
#
#     elif isinstance(error, commands.TooManyArguments):
#         res = 'you provided too much arguments'
#
#     elif isinstance(error, commands.BadBoolArgument):
#         text = ['yes', 'y', 'true', 't', '1', 'enable', 'on']
#         textt = '\'`' + '`\',  \'`'.join(text) + f'`\' count as {True}'
#
#         text = ['no', 'n', 'false', 'f', '0', 'disable', 'off']
#         textf = '\'`' + '`\',  \'`'.join(text) + f'`\' count as {False}'
#
#         res = f'{textt}\n{textf}'
#
#     elif isinstance(error, commands.InvalidEndOfQuotedStringError):
#         res = 'seems like you didnt quote the end'
#
#     elif isinstance(error, commands.CommandNotFound):
#         res = 'to me?\ncommand is not found'
#
#     elif isinstance(error, commands.CommandOnCooldown):
#         res = 'cool down'
#
#     elif isinstance(error, RuntimeWarning):
#         res = 'i think i for got to await something'
#
#     elif isinstance(error, commands.CommandInvokeError):
#         res = (str(error) + '\n says the error')
#
#     elif isinstance(error, discord.HTTPException):  # issubclass(error, discord.HTTPException):
#         res = 'HTTPException (ask bot support)'
#         # ('something went wrong (i dont know what)\n```\n' + str(type(error)) + '\n```')
#
#     elif isinstance(error, commands.NoPrivateMessage):
#         res = 'NoPrivateMessage'
#
#     elif isinstance(error, discord.DiscordException):
#         res = ('something went wrong (i dont know what)\n```\n' + str(type(error)) + '\n```')
#
#     else:
#         res = 'BotError'
#     res = (res + '\n```' + str(error) + '```\n says the error')
#     try:  # Exception
#         await ctx.reply(res)
#     except discord.Forbidden:
#         await forbidden_error(ctx)
#     # print('just print',file=sys.stderr)

