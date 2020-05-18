import discord
import wikipedia
import requests
from random import randint
from discord.ext import commands
TOKEN = 'NzExOTA4MjEwOTM1NzI2MjEy.XsJ2lA.Ci_TU57O7eP7MdnoL7fVqk_GCI4'
bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'

wikipedia.set_lang('ru')
KEY = 'trnsl.1.1.20200518T133822Z.481fcb2b53d946a1.da23af2a80758568e5e74bf20c735509e234a0d5'
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate" #это адрес для обращения к API

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def random(ctx, type='6'): #создаем асинхронную фунцию бота
    try:
        answer = randint(0, int(type))
    except Exception:
        answer = 'Неверный формат ввода. Введите максимальное число'
    await ctx.send(answer) #отправляем обратно аргумент

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


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def translate(ctx, *arg): #создаем асинхронную фунцию бота
    global URL, KEY
    lang = 'ru'
    mytext = ' '.join([*arg])
    try:
        params = {
            "key": KEY,
            "text": mytext
        }
        response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/detect', params=params).json()
        if response['lang'] == 'ru':
            lang = 'en'
        params = {
            "key": KEY,
            "text": mytext,
            "lang": lang # Здесь мы указываем с какого языка на какой мы делаем переводим
        }
        response = requests.get(URL, params=params)
        json = response.json()
        answer = ''.join(json["text"])
    except Exception:
        answer = "Sorry..."
    await ctx.send(answer) #отправляем обратно аргумент


bot.run(TOKEN)