import hikari
import lightbulb

utility_plugin = lightbulb.Plugin("Ustawienia ekonomii - admin")


@utility_plugin.command()
@lightbulb.command('help', 'help')
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(
        description="""**Ekonomia**
```.prankuj, .nagrywaj, .live, .kop, .daily```""",
color = '#FFFFFF'
    ).set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)


def load(bot):
    bot.add_plugin(utility_plugin)

def unload(bot):
    bot.remove_plugin(utility_plugin)