# Create a class called Player.
class Player:

# Every player should have three attributes: gold_coins, health_points, and lives.
# lives should start at 5.
# gold_coins should start at 0.
# health_points should start at 10.

    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

# Define an __str__() instance method.
    def __str__(self):
        return "You have {} gold coins, {} health points and {} lives.".format(self.gold_coins, self.health_points,
        self.lives)

# Your class should have an instance method called level_up that increases lives by one.
    def level_up(self):
        self.lives += 1
        return self.lives

# Your class should have an instance method called collect_treasure that increases gold_coins by one.
# If gold_coins is a multiple of ten (eg, 10, 20, 30, and so on) then the collect_treasure method should run
# the level_up method.

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            return self.level_up()
        else:
            return self.gold_coins

# Your class should have an instance method called do_battle that accepts one damage argument and subtracts
# it from the player's health_points. If health_points falls below one, subtract one from lives and
# reset health_points to ten. If you have run out of lives, this method should run another method called
# restart (see below).
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10
            return self.health_points
        elif self.lives <= 0:
            return self.restart()


# The restart instance method should set all attributes back to their starting values (5, 0, and 10).
    def restart(self):
        self.gold_coins = 5
        self.health_points = 0
        self.lives = 10
        return self

player_1 = Player(9, 2, 1)
print(player_1)
player_1.collect_treasure()
print(player_1)
player_1.collect_treasure()
print(player_1)
player_1.do_battle(1)
print(player_1)
player_1.do_battle(1)
print(player_1)
player_1.do_battle(30)
print(player_1)
