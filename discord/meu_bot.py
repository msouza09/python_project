import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        async def on_message(self, message):
            print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('MTAyNDAxMTYwNjg5MzU0NzU0MQ.Gy8YP9.0gl5TyEw8YeUi2VDRJ4YvJwWKM3eVH3iydFb6k')