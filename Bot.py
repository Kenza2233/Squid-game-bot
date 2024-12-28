import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

# Penyimpanan pemain yang menyertai
players = []
leaderboard = []

# Fungsi untuk memulakan permainan Red Light, Green Light
@bot.command()
async def redlightgreenlight(ctx):
    await ctx.send("Permainan Red Light, Green Light dimulakan!")
    await ctx.send("Pilih [bergerak] apabila Green Light, berhenti apabila Red Light!")
    
    # Senarai pemain yang bergerak
    players_in_game = [p for p in players if random.choice([True, False])]
    await ctx.send(f"Pemain yang bergerak: {', '.join([player.name for player in players_in_game])}")
    
    # Tentukan pemenang atau yang kalah
    if len(players_in_game) == 0:
        await ctx.send("Tiada pemain yang berjaya! Semua kalah!")
    else:
        winner = random.choice(players_in_game)
        await ctx.send(f"Pemenang permainan ini adalah {winner.name}!")

# Fungsi untuk memulakan permainan Tug of War
@bot.command()
async def tugofwar(ctx):
    # Bagi dua pasukan
    random.shuffle(players)
    team1 = players[:len(players)//2]
    team2 = players[len(players)//2:]

    await ctx.send(f"Pasukan 1: {', '.join([player.name for player in team1])}")
    await ctx.send(f"Pasukan 2: {', '.join([player.name for player in team2])}")
    
    # Tentukan pemenang secara rawak
    winner_team = random.choice([team1, team2])
    await ctx.send(f"Pasukan yang menang: {', '.join([player.name for player in winner_team])}")

# Fungsi untuk memulakan permainan Glass Bridge
@bot.command()
async def glassbridge(ctx):
    await ctx.send("Permainan Glass Bridge dimulakan!")
    
    # Pemilihan laluan rawak
    successful_players = []
    for player in players:
        step = random.choice(["selamat", "jatuh"])
        if step == "selamat":
            successful_players.append(player)
        else:
            await ctx.send(f"{player.name} jatuh!")
    
    await ctx.send(f"Pemain yang berjaya adalah: {', '.join([player.name for player in successful_players])}")

# Fungsi untuk menyertai permainan
@bot.command()
async def join(ctx):
    player = ctx.author
    if player not in players:
        players.append(player)
        await ctx.send(f"{player.name} telah menyertai permainan! ID: {len(players):03}")
    else:
        await ctx.send(f"{player.name} sudah menyertai permainan.")

# Fungsi untuk paparkan leaderboard
@bot.command()
async def leaderboard(ctx):
    if len(players) == 0:
        await ctx.send("Tiada pemain dalam permainan.")
        return

    # Buat leaderboard dengan gambar profil dan ID pemain
    leaderboard_message = "Leaderboard:\n"
    for idx, player in enumerate(players, 1):
        profile_picture = player.avatar_url
        leaderboard_message += f"{str(idx).zfill(3)}. {player.name} - {profile_picture}\n"

    await ctx.send(leaderboard_message)

bot.run('MTMyMjU3OTgzNTk0Nzg0MzYxNQ.G4UB9x.ZS8oPbf94_z4LfRgSD01eRvcx9M3pZ7_E8xnLI')
