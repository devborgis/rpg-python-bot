def setup(bot, db):
    from .campanha import load_commands_campanha as set_commands_campanha
    set_commands_campanha(bot, db)