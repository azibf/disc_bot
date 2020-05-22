import discord
import wikipedia
import requests
from random import randint
from discord.ext import commands
from discord import opus
import requests
from bs4 import BeautifulSoup as bs
import random
import lxml.html

TOKEN = 'NzExOTA4MjEwOTM1NzI2MjEy.XsJ2lA.Ci_TU57O7eP7MdnoL7fVqk_GCI4'
bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'
YOUTUBE_API = 'AIzaSyBUg6SK6IEbAXu_zmVAa2SIS2aRMJukt4I'
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
async def mem(ctx, *arg): #создаем асинхронную фунцию бота
    search = 'мем' + ' '.join([*arg])
    try:
        r = requests.get("https://www.google.ru/search?tbm=isch&q=" + search)
        text = r.text
        soup = bs(text, "html.parser")
        img = soup.find_all('img')[2].get('src')
        await ctx.send(img)  # отправляем обратно аргумент
        with open('newfile.jpg', 'wb') as answer:
            a = requests.get(img)
            answer.write(a.content)
            answer = discord.File(answer)
            await ctx.send(file=answer)  # отправляем обратно аргумент
    except Exception:
        answer = "Sorry..."
        await ctx.send(answer) #отправляем обратно аргумент


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def wiki(ctx, *arg): #создаем асинхронную фунцию бота
    try:
        answer = wikipedia.summary(f"{arg}")
    except wikipedia.exceptions.PageError:
        answer = "Увы, но на Википедии такой статьи нет. Попробуй еще раз!"
    except wikipedia.exception.Exception:
        answer = "Sorry..."
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


@bot.command(pass_context=True)
async def join(ctx, *arg):
    pass


@bot.command(pass_context=True)
async def skip(ctx, *arg):
    pass


@bot.command(pass_context=True)
async def play(ctx, *arg):
    pass


@bot.command(pass_context=True)
async def leave(ctx, *arg):
    pass


@bot.command(pass_context=True)
async def stop(ctx, *arg):
    pass

bot.run(TOKEN)
