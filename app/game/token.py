from enum import Enum
from dataclasses import dataclass


class GemColor(Enum):
    WHITE = "white"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    BLACK = "black"
    GOLD = "gold"



@dataclass
class TokenBank:
    tokens: dict[GemColor, int]

    @classmethod
    def create_initial_bank(cls, player_count: int):
        if player_count == 2:
            regular_tokens = 4
        elif player_count == 3:
            regular_tokens = 5
        elif player_count == 4:
            regular_tokens = 7
        else:
            raise ValueError("Player count must be between 2 and 4.")

        tokens = {
            color: regular_tokens
            for color in GemColor
            if color != GemColor.GOLD
        }

        tokens[GemColor.GOLD] = 5

        return cls(tokens)


    def take_tokens(self, color: GemColor, amount: int):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        if self.tokens[color] >= amount:
            self.tokens[color] -= amount
        else:
            raise ValueError(f"{color.value} tokens are less than {amount}.")


    def return_tokens(self, color: GemColor, amount: int):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.tokens[color] += amount