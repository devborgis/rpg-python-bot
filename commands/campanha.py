import discord
from datetime import datetime
from . import utils as u

def load_commands_campanha(bot, db):  
  @bot.tree.command(name="info_campanha", description="Veja informações da campanha ativa")
  async def info_campanha(interaction: discord.Interaction):
  # Buscar Campanha no MongoDB
    campanha = u.search_campanha(interaction.guild.id, db)
    # Se não tiver nenhuma campanha ativa no momento retorna
    if not campanha:
      await interaction.response.send_message("❌ Nenhuma campanha para este servidor", ephemeral=False) 
      return
  

    # Campanha encontrada Cria o Embed 
    embed = discord.Embed(title="ℹ️ Informações da Campanha", color=discord.Color.blue())
    embed.add_field(name="👑 Criador", value=f"<@{campanha['author_id']}>", inline=False)
    #embed.add_field(name="👥 Jogadores", value=str(len(campanha["jogadores"])), inline=True)
    embed.add_field(name="⏳ Início", value=campanha["data_inicio"].strftime("%d/%m/%Y %H:%M:%S"), inline=True)

    await interaction.response.send_message(embed=embed)

  # Criar camapnha no servidor
  @bot.tree.command(name="criar_campanha", description="Inicie um novo mundo de Aventuras")
  async def criar_campanha(interaction: discord.Interaction):
        server_id = interaction.guild.id
        channel_id = interaction.channel.id
        author_id = interaction.user.id

        # Verificar se já existe uma campanha ativa
        campanha_existente = u.search_campanha(interaction.guild.id, db)

        if campanha_existente:
            return await interaction.response.send_message("❌ Já existe uma campanha ativa neste servidor!")

        # Criar nova campanha
        campanha = {
            "server_id": server_id,
            "channel_id": channel_id,
            "author_id": author_id,
            "data_inicio": datetime.now(),
            "status": "ativa"
        }

        # Salvar no MongoDB
        db.campanhas.insert_one(campanha)

        await interaction.response.send_message(f"👑 Campanha criada por <@{author_id}> no canal <#{channel_id}>!")