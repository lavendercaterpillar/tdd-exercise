VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    count_ace = 0

    if len(hand) > 5 or len(hand) < 2:
        return "Invalid"

    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        elif isinstance(card, int):
            score += card
        elif card == "Ace":
            count_ace += 1
            if count_ace > 1 and score == 10:
                score += 1
            else:
                score += 11
        else:
            score += 10

    if score > 21:
        return "bust"

    return score

hand = ["king","queen",5,8,6]
print(len(hand))