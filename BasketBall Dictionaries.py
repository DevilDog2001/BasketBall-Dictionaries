class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self): 
        return "Player: {},age{},postion: {}, team: {}".format(                            
            self.name,self.age,self.position,self.team)                 #used format to release all the players information within the dictionary in the specified format     
#PLAYERS
Kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }
    
Jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    }

Damian = {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    }
#Dictionary Of Players        
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]
#Challenge 3 
new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)
    
#Outputs
player_kevin = Player(Kevin)
player_Jason = Player(Jason)
player_Damian = Player(Damian)
print(player_kevin)
print(player_Jason) 
print(player_Damian)
print(f'\nNew Teams:\n{new_team}')