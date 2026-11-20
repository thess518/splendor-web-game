import pytest
from app.game.token import TokenBank, GemColor


def test_initial_token_bank_for_two_players():
    bank = TokenBank.create_initial_bank(2)

    for color in GemColor:
        if color == GemColor.GOLD:
            assert bank.tokens[color] == 5
        else:
            assert bank.tokens[color] == 4


def test_initial_token_bank_for_three_players():
    bank = TokenBank.create_initial_bank(3)

    for color in GemColor:
        if color == GemColor.GOLD:
            assert bank.tokens[color] == 5
        else:
            assert bank.tokens[color] == 5


def test_initial_token_bank_for_four_players():
    bank = TokenBank.create_initial_bank(4)

    for color in GemColor:
        if color == GemColor.GOLD:
            assert bank.tokens[color] == 5
        else:
            assert bank.tokens[color] == 7


def test_initial_token_bank_for_zero_player():
    with pytest.raises(ValueError):
        bank = TokenBank.create_initial_bank(0)


def test_initial_token_bank_for_one_player():
    with pytest.raises(ValueError):
        bank = TokenBank.create_initial_bank(1)
        

def test_initial_token_bank_for_five_players():
    with pytest.raises(ValueError):
        bank = TokenBank.create_initial_bank(5)


def test_take_two_blue_tokens():
    bank = TokenBank.create_initial_bank(2)

    bank.take_tokens(GemColor.BLUE, 2)

    assert bank.tokens[GemColor.BLUE] == 2


def test_take_all_blue_tokens():
    bank = TokenBank.create_initial_bank(2)

    bank.take_tokens(GemColor.BLUE, 4)

    assert bank.tokens[GemColor.BLUE] == 0


def test_take_more_tokens_than_available():
    bank = TokenBank.create_initial_bank(2)

    with pytest.raises(ValueError):
        bank.take_tokens(GemColor.BLUE, 5)


def test_take_negative_number_of_tokens():
    bank = TokenBank.create_initial_bank(2)

    with pytest.raises(ValueError):
        bank.take_tokens(GemColor.BLUE, -1)


def test_take_zero_token():
    bank = TokenBank.create_initial_bank(2)

    with pytest.raises(ValueError):
        bank.take_tokens(GemColor.BLUE, 0)


def test_return_two_blue_tokens():
    bank = TokenBank.create_initial_bank(2)

    bank.return_tokens(GemColor.BLUE, 2)

    assert bank.tokens[GemColor.BLUE] == 6


def test_return_zero_token():
    bank = TokenBank.create_initial_bank(2)

    with pytest.raises(ValueError):
        bank.return_tokens(GemColor.BLUE, 0)


def test_return_negative_number_of_tokens():
    bank = TokenBank.create_initial_bank(2)

    with pytest.raises(ValueError):
        bank.return_tokens(GemColor.BLUE, -1)


def test_return_tokens_multiple_times():
    bank = TokenBank.create_initial_bank(2)

    bank.return_tokens(GemColor.BLUE, 2)
    bank.return_tokens(GemColor.BLUE, 3)

    assert bank.tokens[GemColor.BLUE] == 9


def test_return_tokens_does_not_change_other_colors():
    bank = TokenBank.create_initial_bank(2)

    bank.return_tokens(GemColor.BLUE, 2)

    assert bank.tokens[GemColor.BLUE] == 6
    assert bank.tokens[GemColor.WHITE] == 4