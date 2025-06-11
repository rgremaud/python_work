from random import choice
random_items = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e']

def lottery_winner(list):
    i = 1
    winners = []
    while i <= 4:
        winners.append(choice(list))
        i += 1
    return winners

my_numbers = lottery_winner(random_items)

def win_count(numbers):
    i = 1
    winning_numbers = lottery_winner(random_items)
    while my_numbers != winning_numbers:
        winning_numbers = lottery_winner(random_items)
        i += 1
    print(f"It took {i} drawings to win")

win_count(my_numbers)