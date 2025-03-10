"""
This class represents a player in a video game.
It tracks their name and health.
"""
class Player:
    """
    >>> player = Player("Mario")
    >>> player.name
    'Mario'
    >>> player.health
    100
    >>> player.damage(10)
    >>> player.health
    90
    >>> player.boost(5)
    >>> player.health
    95
    """
    def __init__(self, name):
        self.name = name
        self.health = 100
        
    def __str__(self):
        return f"Player(name='{self.name}', health={self.health})"
        
    def damage(self, amount):
        self.health -= amount
        
    def boost(self, amount):
        self.health += amount

# 测试代码
if __name__ == "__main__":
    player = Player("Mario")
    print(f"Initial state: {player}")
    player.damage(10)
    print(f"After damage: {player}")
    player.boost(5)
    print(f"After boost: {player}")