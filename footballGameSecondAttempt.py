import random
class Player(object):
    attribute_points = 10
    name = ""
    speed = 5
    dribble = 5
    passing = 5
    tackle = 5
    kickblock = 5
    shooting = 5
    goalie_save = 0
    level = 1
    def __init__(self, name, shooting, speed, dribble, passing, tackle, kickblock,goalie_save):
        self.name = name
        self.shooting = shooting
        self.speed = speed
        self.dribble = dribble
        self.passing = passing
        self.tackle = tackle
        self.kickblock = kickblock
        self.goalie_save = 0

    def __init__(self,name: str, position: str):
        self.name = name
        if position.lower() == "attacker" or position.lower() == "striker":
            self.shooting += 2
            self.dribble += 1
            self.tackle -= 1
            self.kickblock -= 1
        if position.lower() == "midfielder":
            self.dribble += 2
            self.passing += 2
            self.tackle -= 2
            self.kickblock -= 1
            self.speed += 2
            self.shooting -= 1
        if position.lower() == "defender":
            self.shooting -= 3
            self.dribble -= 1
            self.tackle += 2
            self.kickblock += 2
        if position.lower() == "goalie":
            self.speed -= 5
            self.dribble -= 5
            self.passing -= 5
            self.tackle -= 5
            self.kickblock -= 5
            self.shooting -= 5
            self.goalie_save += 2

    def levelUp(self):
        while self.attribute_points != 0:
            chosen = input("Please enter the name of the attribute you wish to add points to: ")
            setattr(self,chosen.strip(),5)
            self.attribute_points -= 1
            print("One point was added to " + chosen)
            print(chosen,getattr(self,chosen))
    def tryToScore(self, opponent):
        genRan = random.randint(1,10)
        statDiff = self.kick - opponent.goalie_save
        if(genRan >= statDiff):
            return True
        else:
            return False
    def tryToDribble(self,opponent):
        dribblerName = ""
        opponentName = ""
        if("Opponent" in self.name):
            print(True)
            dribblerName = "The opponent dribbles pass"
            dribblerFail = "The opponent's"
            opponentName = "your teammates"
        else:
            dribblerName = "You dribble pass"
            dribblerFail = "Your"
            opponentName = "the opposing team's defender"
        if(self.dribble >= opponent.tackle and self.speed >= opponent.speed):
            return dribblerName + opponentName + " with relative ease!"
        else:
            return dribblerFail + " dribble attempt is intercepted by " + opponentName + "!"
    def tryToPass(self,opponent):
        dribblerName = ""
        opponentName = ""
        if("Opponent" in self.name):
            dribblerName = "The opponent passes"
            opponentName = "your teammates"
        else:
            print(False)
            dribblerName = "You pass"
            opponentName = "the opposing team's defender"
        if(self.passing >= opponent.kickblock):
            return dribblerName + " the ball through " + opponentName + " with relative ease!"
        else: 
            return dribblerName + " the ball, but it is intercepted by "+opponentName+"!!!"
        

MyPlayer = Player("Anon","Striker")
Opponent_1 = Player("Opponent 1","Goalie")
Opponent_2 = Player("Opponent 2","Defender")
Opponent_3= Player("Opponent 3","Defender")
Opponent_4 = Player("Opponent 4","Defender")
Opponent_5 = Player("Opponent 5","Defender")
Opponent_6 = Player("Opponent 6","Midfielder")
Opponent_7 = Player("Opponent 7","Midfielder")
Opponent_8 = Player("Opponent 8","Midfielder")
Opponent_9 = Player("Opponent 9","Midfielder")
Opponent_10 = Player("Opponent 10","Striker")
Opponent_11 = Player("Opponent 11","Striker")

def sequence1(playerTeam, playerName):
    print('''And the match is kicking off!!! Ladies and Gentlemen here we go!!! The %s are going to be kicking it off first and oh well it looks like 
    there star player, %s, has the ball!!!! He takes it pass midfield and tries to dribble through the opposing team's defender!!!''' % (playerTeam, playerName))
    print(MyPlayer.tryToDribble(Opponent_5))

def preset_introfunction(team1, team2):
    print('''Ladies and Gentlemen! Welcome to today's game.
Today we're going to be watching the %s and %s going head-to-head!
Alright, without any further adieu, let's get right into the action
''' % (team1, team2))
    return
##print(Opponent_1.tryToPass(MyPlayer))
team_list = ["Bangkok Battlers", "Siamese Sharks", "Chaing Mai Comets"]
team_1 = input("Please enter your team name: ")
team_2 = random.choice(team_list)
MyPlayer.levelUp()
preset_introfunction(team_1, team_2)
sequence1(team_1, MyPlayer.name)

