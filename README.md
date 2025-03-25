# 🌟 Grande Jornada - Um RPG de Fé e Aventura

Bem-vindo ao **Grande Jornada**, um RPG inspirado nas grandes histórias da Bíblia. Aqui, os jogadores embarcam em uma aventura épica, enfrentando desafios, batalhas intensas e decisões que moldam seu destino.

## 📖 Sobre a Lore

Em um mundo inspirado nas Escrituras, a luz e as trevas travam uma batalha sem fim. Os jogadores assumem o papel de heróis guiados pela fé, explorando terras sagradas, enfrentando inimigos poderosos e coletando artefatos divinos. A cada decisão, o caminho rumo à redenção ou à perdição se desenha.

## 🤝 Como Contribuir

Quer ajudar a moldar esse mundo? Estamos abertos a novas ideias, códigos e melhorias!

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/devborgis/rpg-python-bot.git
   cd rpg-python-bot
   ```
2. **Crie uma nova branch para sua contribuição:**
   ```sh
   git checkout -b minha-contribuicao
   ```
3. **Implemente suas ideias e faça um commit:**
   ```sh
   git commit -m "Adicionando novo recurso X"
   ```
4. **Envie um Pull Request:**
   ```sh
   git push origin minha-contribuicao
   ```

## 📢 Participe da Nossa Comunidade!

Toda grande jornada precisa de um conselho de sábios! Para alinhar ideias e garantir que as contribuições se encaixem na visão do projeto, convidamos todos os colaboradores a participarem do nosso **Discord privado**. Entre no servidor e faça parte da construção desse universo épico! 🚀

🔗 **Link do Discord:** [Clique aqui para entrar](https://discord.gg/6MtQ679zdW)

## 📂 Estrutura de Pastas do Projeto

```
│── bot.py                 # Ponto de entrada do bot
├── commands/              # Comandos do bot (explorar, batalha, status)
├── lore/                  # História do RPG, personagens e eventos bíblicos
├── resources/             # Recursos como imagens, sons e gráficos
├── data/                  # Banco de dados ou arquivos persistentes
├── utilities/             # Funções auxiliares e ferramentas
├── logs/                  # Logs do sistema para debugging
└── README.md              # Documentação do projeto
```

## ⚙️ Configuração e Dependências

O bot depende do **MongoDB** para armazenar dados e progresso dos jogadores. Para configurar seu ambiente, siga os passos abaixo:

### 1️⃣ Criando um Bot no Discord
1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em **New Application** e dê um nome ao seu bot.
3. Vá até **Bot** e clique em **Add Bot**.
4. Copie o **Token** do bot e configure no arquivo `.env`.

### 2️⃣ Configurando o MongoDB
1. Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/atlas/database)
2. Configure um banco de dados gratuito.
3. Copie a string de conexão e adicione no `.env`.

### 3️⃣ Configurando o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto seguindo o exemplo do arquivo `.env.example` 

## 📝 Licença

Este projeto está licenciado sob a **MIT License** – fique à vontade para usar, modificar e contribuir!

---
💡 **"A tua palavra é lâmpada para os meus pés e luz para o meu caminho."** - Salmos 119:105