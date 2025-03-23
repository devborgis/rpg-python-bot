import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carregas Variaveis
load_dotenv()

# Obter o Token do Bot
discord_token = os.getenv("BOT_TOKEN")

if not discord_token:
    raise ValueError("Error: Token não encontrado")

# Intents e Criação do BOT
intents = discord.Intents.all()
bot = commands.Bot("?", intents=intents)


# Comandos e Eventos
@bot.event
async def on_ready():
    print("Bot inicializado")

@bot.command()
async def ola(ctx):
    nome = ctx.author.name
    await ctx.reply(f"Hello, World ! {nome}")

# Iniciando Bot 
bot.run(discord_token)