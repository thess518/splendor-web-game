import pytest
from app.game.token import GemColor
from app.game.card import Card


@pytest.fixture
def sample_card():
    return Card(
        0,
        1,
        GemColor.BLUE,
        0,
        {
            GemColor.WHITE: 2,
            GemColor.BLACK: 1,
            GemColor.RED: 3
        }
    )


def test_initial_card_id(sample_card):
    assert sample_card.card_id == 0


def test_initial_card_tier(sample_card):
    assert sample_card.tier == 1


def test_initial_card_bonus(sample_card):
    assert sample_card.bonus == GemColor.BLUE


def test_initial_card_points(sample_card):
    assert sample_card.points == 0


def test_initial_card_cost_white(sample_card):
    assert sample_card.cost[GemColor.WHITE] == 2


def test_initial_card_cost_black(sample_card):
    assert sample_card.cost[GemColor.BLACK] == 1


def test_initial_card_cost_red(sample_card):
    assert sample_card.cost[GemColor.RED] == 3


def test_initial_card_with_negative_id():
    with pytest.raises(ValueError):
        Card(
            -1,
            1,
            GemColor.BLUE,
            0,
            {
                GemColor.WHITE: 2
            }
        )


def test_initial_card_with_invalid_tier():
    with pytest.raises(ValueError):
        Card(
            0,
            4,
            GemColor.BLUE,
            0,
            {
                GemColor.WHITE: 2
            }
        )


def test_initial_card_with_gold_bonus():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            GemColor.GOLD,
            0,
            {
                GemColor.WHITE: 2
            }
        )



def test_initial_card_with_string_bonus():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            "blue",
            0,
            {
                GemColor.WHITE: 2
            }
        )


def test_initial_card_with_negative_points():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            GemColor.BLUE,
            -1,
            {
                GemColor.WHITE: 2
            }
        )


def test_initial_card_with_string_cost_key():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            GemColor.BLUE,
            0,
            {
                'white': 2
            }
        )


def test_initial_card_with_negative_cost():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            GemColor.BLUE,
            0,
            {
                GemColor.WHITE: -2
            }
        )


def test_initial_card_with_invalid_cost_type():
    with pytest.raises(ValueError):
        Card(
            0,
            1,
            GemColor.BLUE,
            0,
            "invalid"
        )