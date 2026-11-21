from dataclasses import dataclass
from app.game.token import GemColor


@dataclass
class Card:
    card_id: int
    tier: int
    bonus: GemColor
    points: int
    cost: dict[GemColor, int]

    def __post_init__(self):
        if self.card_id < 0:
            raise ValueError("Card Id must be non-negative.")

        if self.tier not in range(1,4):
            raise ValueError("Card tier must be between 1 and 3.")

        if not isinstance(self.bonus, GemColor):
            raise ValueError("Card bonus must be a GemColor.")

        if self.bonus == GemColor.GOLD:
            raise ValueError("Card bonus cannot be GOLD.")

        if self.points not in range(6):
            raise ValueError("Card points must be between 0 and 5.")

        for gem_color in self.cost:
            if not isinstance(gem_color, GemColor):
                raise ValueError("Gem color of the cost must be a GemColor.")

        for token_amount in self.cost.values():
            if token_amount <= 0:
                raise ValueError("Card cost must be positive.")

        if not isinstance(self.cost, dict):
            raise ValueError("Card cost must be a dictionary.")