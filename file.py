# This example requires the 'message_content' privileged intent to function.

import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Halo! Saya bot penghitung.')

        if message.content.startswith('$guess'):
            await message.channel.send('Tebak angka berapapun antara 1 dan 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Maaf, kamu terlalu lama {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Kamu benar!')
            else:
                await message.channel.send(f'Waduh, yang benar adalah {answer}.')

        if message.content.startswith('$pass'):
            def gen_pass(pass_length):
                elements = "+-/*!&$#?=@<>"
                password = ""

                for i in range(pass_length):    
                    password += random.choice(elements)

                return password

            await message.channel.send(gen_pass(10)) 

        if message.content.startswith('$luaspersegi'):
            await message.channel.send("input panjang sisi: ")
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Maaf, kamu terlalu lama {answer}.')
            answer = int(guess.content) * int(guess.content)

            await message.channel.send(answer)

        if message.content.startswith('$luassegitiga'):
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            await message.channel.send("input alas: ")
            
            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Maaf, kamu terlalu lama {answer}.')
            
            alas = int(guess.content)    

            await message.channel.send("input tinggi: ")

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Maaf, kamu terlalu lama {answer}.')

            tinggi = int(guess.content)  
            
            answer = 0.5 * int(alas) * int(tinggi)

            await message.channel.send(answer)

        if message.content.startswith('$luaslingkaran'):
            await message.channel.send("input panjang jari-jari: ")
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Maaf, kamu terlalu lama {answer}.')
            answer = 3.14 * int(guess.content) * int(guess.content)

            await message.channel.send(answer)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTEwNjgwNDg0NzU2MDM2NDA3Mw.GnljL4.7r6Gl8R5eAXuO12jmgVHKolpEWW0zy7u67UPwg')