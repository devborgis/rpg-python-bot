import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carregas Variaveis
load_dotenv()

# Importar MongoDB
from data.database import *

# Obter o Token do Bot
discord_token = os.getenv("BOT_TOKEN")

if not discord_token:
    raise ValueError("Error: Token não encontrado")

# Intents(Permissões) e Criação do BOT
intents = discord.Intents.all()
Prefix = "jc!"
bot = commands.Bot(Prefix, intents=intents)

# Comandos e Eventos
TestarMongo() # Testando Com MongoDB data/database.py

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    
    # Registrar os comandos no Discord (sync)
    await bot.tree.sync()
    print("Comandos registrados com sucesso!")

# Varregar os comandos da pasta Commands
from commands import *
setup(bot, db)

# Iniciando Bot 
bot.run(discord_token)