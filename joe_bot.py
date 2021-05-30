import discord
import os
import random
import json
from datetime import datetime
from dotenv import load_dotenv
from github import Github
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix='$')

qoutes = {}

def write_json(data, filename='qoutes.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

@bot.command()
async def foo(ctx, qoute, speaker):

    filename ="qoutes.json"

    #send message in discord and tag speaker
    if (speaker == "Eli" or speaker == "Elijah" or speaker == "Elijah Leung" or speaker == "eli"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['eli_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('E_TOKEN') + '>' )
    elif (speaker == "David" or speaker == "david"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['david_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)        
        await ctx.send('"' + qoute + '" -<@' + os.getenv('D_TOKEN') + '>' )
    elif (speaker == "Nicky" or speaker == "nicky"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['nicky_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('N_TOKEN') + '>' )
    elif (speaker == "Emilio" or speaker == "emilio"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['emilio_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('ITALIAN_TOKEN') + '>' )
    elif (speaker == "Joe" or speaker == "joe"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['joe_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('J_TOKEN') + '>' )
    elif (speaker == "Brandon" or speaker == "brandon"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['brandon_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('B_TOKEN') + '>' )
    elif (speaker == "Jeremy" or speaker == "jeremy"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['jeremy_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('JE_TOKEN') + '>' )
    elif (speaker == "Quinn" or speaker == "quinn"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['quinn_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('Q_TOKEN') + '>' )
    elif (speaker == "James" or speaker == "james"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['james_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('BOOTY_TOKEN') + '>' )
    elif (speaker == "Chris" or speaker == "chris"):
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['chris_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('C_TOKEN') + '>' )
    else:
        with open('qoutes.json') as json_file:
            data = json.load(json_file)
            
            temp = data['meme_magic_qoutes']
            x = len(temp)
        
            # python object to be appended
            y = {"id": x+1,
                "qoute":qoute,
                "speaker": speaker,
                }
        
            # appending data to emp_details 
            temp.append(y)

        write_json(data)
        await ctx.send('"' + qoute + '" -<@' + os.getenv('C_TOKEN') + '>' )

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if current_time == "12:00:00" or current_time == "20:00:00":
        token = os.getenv('GITHUB_TOKEN')

        repo = "CJcrispy/E-zone"
        path = "site/assests/qoutes.json"

        #API requests to get updated SHA file 
        url = f"https://api.github.com/repos/CJcrispy/E-zone/contents/site/assests/qoutes.json"
        get_response = requests.get(url)
        sha = get_response.json()['sha']

        g = Github(token)

        data = open("qoutes.json", "r").read()

        repo = g.get_repo(repo)
        repo.update_file(
            path = path, 
            message = "update file", 
            content = data, 
            branch = "main",
            sha = sha
        )
    else:
        pass

@bot.command()
async def fool(ctx):
    discord_id = {
        "Eli": os.getenv('E_TOKEN'),
        "Nicky": os.getenv('N_TOKEN'),
        "David": os.getenv('D_TOKEN'),
        "Emilio": os.getenv('ITALIAN_TOKEN'),
        "Joe": os.getenv('J_TOKEN'),
        "Brandon": os.getenv('B_TOKEN'),
        "Jeremy": os.getenv('JE_TOKEN'),
        "Quinn": os.getenv('Q_TOKEN'),
        "James": os.getenv('BOOTY_TOKEN'),
        "Chris": os.getenv('C_TOKEN'),
    }
    myid = "<@" + str(random.choice(list(discord_id.values()))) +">"
    await ctx.send(' %s loves feet ' % myid)

@bot.command()
async def spare(ctx):
    discord_id = {
        "Eli": os.getenv('E_TOKEN'),
        "Nicky": os.getenv('N_TOKEN'),
        "David": os.getenv('D_TOKEN'),
        "Emilio": os.getenv('ITALIAN_TOKEN'),
        "Joe": os.getenv('J_TOKEN'),
        "Brandon": os.getenv('B_TOKEN'),
        "Jeremy": os.getenv('JE_TOKEN'),
        "Quinn": os.getenv('Q_TOKEN'),
        "James": os.getenv('BOOTY_TOKEN'),
        "Chris": os.getenv('C_TOKEN'),
    }
    myid = "<@" + str(random.choice(list(discord_id.values()))) +">"
    await ctx.send(' %s just rolled a spare. Spare me some of that nice cock.' % myid)


@bot.command()
async def website(ctx):
    await ctx.send('check out the official Eli zone at https://elijahisland.netlify.app/')   

@bot.command()
async def doctor(ctx):
    myid = "<@" + os.getenv('E_TOKEN') + ">" 
    await ctx.send(' %s, why you no doctor'  % myid)   

@bot.command()
async def joe_island(ctx):
    await ctx.send('A place no Joe should go...')   

bot.run(os.getenv('DISCORD_TOKEN'))