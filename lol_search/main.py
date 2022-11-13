from discord.ext import commands
from cryptography.fernet import Fernet

def get_token():
    with open('cipher\secret_key.key') as f:
        key = f.readline()

    with open('cipher\cipher.txt') as f:
        cipher = f.readline()

    fernet = Fernet(key.encode())
    dectex = fernet.decrypt(cipher.encode()).decode()

    return dectex

bot = commands.Bot(command_prefix='!')
bot.load_extension("lol_search")
bot.run(get_token())