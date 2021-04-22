import random
import json

# discord_id = {
#         "Eli": 255487430021349377,
#         "Nicky": 175172832932790272,
#         "David": 102619624457117696,
#         "Emilio": 175456751485845504,
#         "Joe": 286373232658087936,
#         "Brandon": 501940668130918410,
#         "Jeremy": 810635012079878174,
#         "Quinn": 183339268070965249,
#         "James": 543605006717288449,
#     }
# print(random.choice(list(discord_id.values())))

# qoutes["qoute"] = "speaker"
# qoutes_json = json.dumps(qoutes)
# print(qoutes_json)

# function to add to JSON
def write_json(data, filename='test.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
      
      
with open('test.json') as json_file:
    data = json.load(json_file)
      
    temp = data['qoutes']
    x = len(temp)
    print(x)
    # python object to be appended
    y = {"id": x+1,
        "qoute": "i love unseasoned men",
         "speaker": "Nicky",
        }
  
  
    # appending data to emp_details 
    temp.append(y)
      
write_json(data) 