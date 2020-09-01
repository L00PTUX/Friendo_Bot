## words.txt from https://github.com/dwyl/english-words/blob/master/words.txt
from discord.ext.commands import Bot, Cog, command
import random




class hangman(Cog):


    def __init__(self, bot: Bot):
        self.bot = bot

    async def hangman(self, answer, guess, respone):
        answer_list = open("../hangman_resources/words.txt","r")
        answer = answer_list.readline(random)
