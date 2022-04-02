import hikari
import lightbulb

import random
import math
import sqlite3

eco_plugin = lightbulb.Plugin("Ustawienia ekonomii - admin")
con = sqlite3.connect('main.db')
c = con.cursor()


@eco_plugin.command()
@lightbulb.command("sklep", 'sklep')
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def sklep(ctx: lightbulb.Context) -> None:
  await ctx.respond(hikari.Embed(
    title="Sklep z itemami",
    description="""`1.` kiedys -> `10 000`$
    ```Uagasg asg aso jkopagsk koasp k```
    """,
    color='#0012ff'
  ))

@eco_plugin.command()
@lightbulb.command('bank', 'bank', aliases=['bal', 'cash', 'balance', 'portfel'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def bank(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash, bank FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return
    
    await ctx.respond(hikari.Embed(
        title="Twój portfel",
        color = '#FFFFFF'
    ).set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url).add_field(name='Portfel', value=f'`{r[0]}`$', inline=True).add_field(name='Bank', value=f'`{r[1]}`$', inline=True), reply=True)

@eco_plugin.command()
@lightbulb.add_cooldown(21600, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('prankuj', 'prankuj')
@lightbulb.implements(lightbulb.PrefixCommand)
async def prankuj(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return
    if 70 < random.randint(0, 100):
        kara = random.randint(50, 300)
        cash = r[0]
        nowy_balans = int(cash) - kara

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        
        await ctx.respond(hikari.Embed(
            title="Przyłapano Cię na pranku",
            description=f"""Niestety, ale tym razem nie udało Ci się zrobić pranka. Zabieram Ci z portfela `{kara}`$. 
            
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
<:nie:866036882553700353> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#ff0000').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url))
    else:
        nagroda = random.randint(100, 450)
        cash = r[0]
        nowy_balans = nagroda + int(cash)

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        await ctx.respond(hikari.Embed(
            title="Zrobiono pranka!",
            description=f"""<@{ctx.author.id}>, zarobiłeś/-aś `{nagroda}`$!
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
            
<:tak:866036793455280180> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)

@eco_plugin.command()
@lightbulb.add_cooldown(21600, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('kop', 'kop')
@lightbulb.implements(lightbulb.PrefixCommand)
async def kop(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return

    if 70 < random.randint(0, 100):
        kara = random.randint(50, 300)
        cash = r[0]
        nowy_balans = int(cash) - kara

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        
        await ctx.respond(hikari.Embed(
            title="Nie udało się wykopać",
            description=f"""Niestety, ale tym razem nie udało Ci się nic wykopać. Zabieram Ci z portfela `{kara}`$.
            
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
<:nie:866036882553700353> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""",
            color = '#ff0000').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url))
    else:
        nagroda = random.randint(100, 450)
        cash = r[0]
        nowy_balans = nagroda + int(cash)

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        await ctx.respond(hikari.Embed(
            title="Kopanie!", # do edycji
            description=f"""<@{ctx.author.id}>, zarobiłeś/-aś `{nagroda}`$!
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
            
<:tak:866036793455280180> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)

@eco_plugin.command()
@lightbulb.add_cooldown(21600, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('montuj', 'montuj')
@lightbulb.implements(lightbulb.PrefixCommand)
async def montuj(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return

    if 70 < random.randint(0, 100):
        kara = random.randint(50, 300)
        cash = r[0]
        nowy_balans = int(cash) - kara

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        
        await ctx.respond(hikari.Embed(
            title="Nie udało się zmontować filmu", # do edycji
            description=f"""Niestety, ale tym razem nie udało Ci się nic zmontować. Zabieram Ci z portfela `{kara}`$.
            
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
<:nie:866036882553700353> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#ff0000').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url))
    else:
        nagroda = random.randint(100, 450)
        cash = r[0]
        nowy_balans = nagroda + int(cash)

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        await ctx.respond(hikari.Embed(
            title="Zmontowano film!",
            description=f"""<@{ctx.author.id}>, zarobiłeś/-aś `{nagroda}`$!
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
            
<:tak:866036793455280180> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""",
            color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)

@eco_plugin.command()
@lightbulb.add_cooldown(21600, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('live', 'live')
@lightbulb.implements(lightbulb.PrefixCommand)
async def live(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return

    if 70 < random.randint(0, 100):
        kara = random.randint(50, 300)
        cash = r[0]
        nowy_balans = int(cash) - kara

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        
        await ctx.respond(hikari.Embed(
            title="Nie udało się odpalić streama", # do edycji
            description=f"""Niestety, ale tym razem nie udało Ci się odpalić streama. Zabieram Ci z portfela `{kara}`$.
            
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
<:nie:866036882553700353> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#ff0000').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url))
    else:
        nagroda = random.randint(100, 450)
        cash = r[0]
        nowy_balans = nagroda + int(cash)

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        await ctx.respond(hikari.Embed(
            title="Odpalono streama!",
            description=f"""<@{ctx.author.id}>, zarobiłeś/-aś `{nagroda}`$!
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
            
<:tak:866036793455280180> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""",
            color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)
    
@eco_plugin.command()
@lightbulb.add_cooldown(21600, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('nagrywaj', 'nagrywaj')
@lightbulb.implements(lightbulb.PrefixCommand)
async def nagrywaj(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return

    if 70 < random.randint(0, 100):
        kara = random.randint(50, 300)
        cash = r[0]
        nowy_balans = int(cash) - kara

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        
        await ctx.respond(hikari.Embed(
            title="Nie udało się zmontować filmu", # do edycji
            description=f"""Niestety, ale tym razem nie udało Ci się nic nagrać. Zabieram Ci z portfela `{kara}`$.
            
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
<:nie:866036882553700353> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""", # do edycji
            color = '#ff0000').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url))
    else:
        nagroda = random.randint(100, 450)
        cash = r[0]
        nowy_balans = nagroda + int(cash)

        sql = "UPDATE userData SET cash = ? WHERE userID = ?"
        val = (nowy_balans, ctx.author.id)
        c.execute(sql, val)
        con.commit()
        await ctx.respond(hikari.Embed(
            title="Nagrano film!",
            description=f"""<@{ctx.author.id}>, zarobiłeś/-aś `{nagroda}`$!
<:neutral:866036839348699176> **Stan portfela przed użyciem komendy**:
`{cash}`$
            
<:tak:866036793455280180> **Stan portfela po użyciu komendy**:
`{nowy_balans}`$""",
            color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)

@eco_plugin.command()
@lightbulb.add_cooldown(43200, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command('daily', 'daily')
@lightbulb.implements(lightbulb.PrefixCommand)
async def nagrywaj(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT cash FROM userData WHERE userID = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        sql = (f"INSERT INTO userData(userID, cash, bank)"
               f"VALUES(?, ?, ?)")
        val = (ctx.author.id , 0 , 0)
        c.execute(sql , val)
        con.commit()
        await ctx.respond(hikari.Embed(
            description="Nie było Cię w bazie danych. Już jesteś zarejestrowany. Użyj komendy jeszcze raz",
            color = '#ff0000'
        ))
        return
    
    nagroda = random.randint(100, 300)
    cash = r[0]
    nowy_balans = nagroda + int(cash)

    sql = "UPDATE userData SET cash = ? WHERE userID = ?"
    val = (nowy_balans, ctx.author.id)
    c.execute(sql, val)
    con.commit()

    await ctx.respond(hikari.Embed(
        title="Odebrano daily!",
        description=f"Odebrałeś dzienną nagrodę o wysokości `{nagroda}`$!",
        color = '#FFFFFF').set_footer(text=f"{ctx.author.username} | SKTM", icon = ctx.author.avatar_url), reply=True)
    

def load(bot):
    bot.add_plugin(eco_plugin)


def unload(bot):
    bot.remove_plugin(eco_plugin)
