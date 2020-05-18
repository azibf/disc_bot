import discord
import wikipedia
from discord.ext import commands
TOKEN = 'NzExOTA4MjEwOTM1NzI2MjEy.XsJ2lA.Ci_TU57O7eP7MdnoL7fVqk_GCI4'
bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'

wikipedia.set_lang('ru')


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def wiki(ctx, *arg): #создаем асинхронную фунцию бота
    try:
        answer = wikipedia.summary(f"{arg}")
    except wikipedia.exceptions.DisambiguationError:
        answer = "Много статьей могут относитсься к твоему сообщению. Напиши точнее."
    except wikipedia.exceptions.PageError:
        answer = "Увы, но на Википедии такой статьи нет. Попробуй еще раз!"
    await ctx.send(answer) #отправляем обратно аргумент


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def math(ctx, *arg): #создаем асинхронную фунцию бота
    arg = ''.join([*arg])
    print(arg)
    try:
        answer = str(eval(arg))
    except Exception:
        answer = "Sorry..."
    await ctx.send(answer) #отправляем обратно аргумент


bot.run(TOKEN)