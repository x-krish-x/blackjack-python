#Yay -  Play some blackjack!

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score

def blackjack():
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print("Your cards:", player, "Score:", player_score)
        print("Dealer's first card:", dealer[0])

        if player_score == 21:
            print("Blackjack! You win!")
            game_over = True
        elif player_score > 21:
            print("You went bust. You lose.")
            game_over = True
        else:
            choice = input("Hit or stand? ").lower()

            if choice == "h":
                player.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer) < 17 and calculate_score(player) <= 21:
        dealer.append(deal_card())

    if calculate_score(player) <= 21:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print("Your final hand:", player, "Score:", player_score)
        print("Dealer's final hand:", dealer, "Score:", dealer_score)

        if dealer_score > 21:
            print("Dealer busts. You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose.")
        else:
            print("Draw.")

blackjack()