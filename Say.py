if message.content.startswith("/say"): 
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       await message.delete()
       await message.channel.send(f"{message.content.replace('/say', ' ')}")
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /say Nachricht:{message.content.replace('/say', ' ')}")
       print(f"{message.author.mention} schrieb als /say Nachricht: {message.content}")


   if message.content.startswith("/embedsay"):
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       embed = discord.Embed(
       description=f"{message.content.replace('/embedsay', ' ')}", color=0x29B46F)
       await message.channel.send(embed=embed)
       await message.delete()
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /embedsay Nachricht:{message.content.replace('/say', ' ')}")
       print(f"{message.author.mention} schrieb als /embedsay Nachricht: {message.content}")

   if message.content.startswith("/blueembedsay"):
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       embed=discord.Embed(description=f"{message.content.replace('/blueembedsay', ' ')}", color=0x0000FF)
       await message.channel.send(embed=embed)
       await message.delete()
       print(f"{message.author.mention} schrieb als /blueembedsay Nachricht: {message.content}")
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /blueembedsay Nachricht:{message.content.replace('/say', ' ')}")

   if message.content.startswith("/redembedsay"):
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       embed = discord.Embed(
                description=f"{message.content.replace('/redembedsay', ' ')}", color=0xFF0000)
       await message.channel.send(embed=embed)
       await message.delete()
       print(f"{message.author.mention} schrieb als /redembedsay Nachricht: {message.content}")
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /redembedsay Nachricht:{message.content.replace('/say', ' ')}")


   if message.content.startswith("/yellowembedsay"):
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       embed = discord.Embed(
                description=f"{message.content.replace('/yellowembedsay', ' ')}", color=0xFFFF00)
       await message.channel.send(embed=embed)
       await message.delete()
       print(f"{message.author.mention} schrieb als /yellowembedsay Nachricht: {message.content}")
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /yellowembedsay Nachricht:{message.content.replace('/say', ' ')}")

   if message.content.startswith("/greenembedsay"):
     if "@everyone" in message.content:
       embed=discord.Embed(description="Don't use @everyone !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @everyone in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
     else:
      if "@here" in message.content:
       embed=discord.Embed(description="Don't use @here !", color=0x29B46F)
       await message.delete()
       print("Vorgang beendet! Grund: @here in message.content")
       await message.channel.send(embed=embed, delete_after=10)
       return
      else:
       embed = discord.Embed(
                description=f"{message.content.replace('/greenembedsay', ' ')}", color=0x00FF00)
       await message.channel.send(embed=embed)
       await message.delete()
       print(f"{message.author.mention} schrieb als /greenembedsay Nachricht: {message.content}")
       channel = client.get_channel(811527246900756550)
       await channel.send(f"{message.author.name} (ID = {message.author.id}) schrieb als /greenembedsay Nachricht:{message.content.replace('/say', ' ')}")
