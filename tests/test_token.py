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