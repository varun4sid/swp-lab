""" MEMENTO PATTERN
Consider a video game (Adventure / Racing / Shooting).
While playing, the player progresses through:
• Levels
• Missions
• Health status
• Weapons collected
• Score points
• Map position

Players expect features like:
• Save Game
• Load Game
• Checkpoints
• Restart from last saved state
To implement this, the system must capture and restore the player’s state
without exposing internal game logic.
"""

from copy import deepcopy


class GameState:
    def __init__(self, level, mission, health, weapons, score, position):
        self.level = level
        self.mission = mission
        self.health = health
        self.weapons = weapons
        self.score = score
        self.position = position

    def __str__(self):
        return (f"Level: {self.level}, Mission: {self.mission}, Health: {self.health}, "
                f"Weapons: {self.weapons}, Score: {self.score}, Position: {self.position}")
        

class Game:
    def __init__(self, level=1, mission=1, health=100, weapons=None, score=0, position=(0, 0)):
        self._game_state = GameState(
            level,
            mission,
            health,
            list(weapons) if weapons is not None else [],
            score,
            position,
        )

    def save_state(self, state):
        self._game_state = deepcopy(state)

    def load_state(self):
        return deepcopy(self._game_state)

    def create_checkpoint(self):
        return Checkpoint(self.load_state())

    def restore_checkpoint(self, checkpoint):
        self.save_state(checkpoint.get_state())


class Checkpoint:
    def __init__(self, game_state):
        self._game_state = deepcopy(game_state)

    def get_state(self):
        return deepcopy(self._game_state)


if __name__ == "__main__":
    game = Game(level=2, mission=3, health=85, weapons=["pistol"], score=1500, position=(10, 20))
    checkpoint = game.create_checkpoint()

    game._game_state.health = 20
    game._game_state.weapons.append("rifle")
    game.restore_checkpoint(checkpoint)
    print(game.load_state())