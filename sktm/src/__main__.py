import hikari
import lightbulb
from lightbulb.ext import tasks

import sqlite3
import aiohttp
import datetime

TOKEN = "daj tu token bota"
bot = lightbulb.BotApp(prefix=".", token=TOKEN, intents=hikari.Intents.ALL_UNPRIVILEGED, help_class=None)

bot.load_extensions_from("./src/extensions")

con = sqlite3.connect('main.db')
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userData(
        userID INTEGER,
        cash INTEGER DEFAULT 0,
        bank INTEGER DEFAULT 0)
        """)

@bot.listen(hikari.MemberCreateEvent)
async def on_joined(event: hikari.MemberCreateEvent) -> None:
    c.execute(f"SELECT userID FROM userData WHERE userID = {event.message.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID)"
                       f"VALUES(?)")
        val = (event.message.author.id)
        c.execute(sql , val , )
        con.commit()
    else:
        pass

@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()
    await bot.rest.create_message(789387159337566258, f"bot odpalony :sunglasses: {TOKEN}")

@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()

@bot.listen(lightbulb.events.CommandErrorEvent)
async def on_command_error(event : lightbulb.events.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.errors.CommandIsOnCooldown):
        await event.context.respond(hikari.Embed(
            description=f"Nie możesz jeszcze użyć komendy. Pozostało: `{str(datetime.timedelta(seconds=int(event.exception.retry_after)))}`",
            color = '#ff0000'))



bot.run()