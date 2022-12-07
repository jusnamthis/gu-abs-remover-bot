from random import randint

MAX_CANDIES_IN_ONE_STEP = 28
TOTAL_NUM_OF_CANDIES = 220


def get_user_candies_amount():
    candies = input('enter num of candies you wanna take, [1, 28]: ')
    while not candies.isdigit() or int(candies) > MAX_CANDIES_IN_ONE_STEP:
        print('wrong number!')
        candies = input('enter num of candies you wanna take, [1, 28]: ')
    return int(candies)


def get_smart_bot_move(candies):
    move = randint(1, 28)
    if candies <= 28:
        return candies
    elif candies >= 85:
        while candies - move <= 58:
            move = randint(1, 28)
    elif candies < 85 and candies > 57:
        return candies - 58
    elif candies <= 57:
        return candies - 29
    return move

# TELEGRAM...
def get_bot_move(total_candies):
    if total_candies <= 0:
        return 0

    if total_candies >= 100:
        return randint(1, 28)
    else:
        return get_smart_bot_move(total_candies)
# ...TELEGRAM


if __name__ == '__main__':
    total_candies = TOTAL_NUM_OF_CANDIES
    is_users_move = True

    while total_candies > 0:
        if is_users_move:
            candies_amount = get_user_candies_amount()
            total_candies -= candies_amount
            is_users_move = False
        else:
            print('Bot\'s move', end=': ')
            if total_candies >= 100:
                candies_amount = randint(1, 28)
                total_candies -= candies_amount
            else:
                candies_amount = get_smart_bot_move(total_candies)
                total_candies -= candies_amount
            print(candies_amount)
            is_users_move = True
        print(total_candies)

    is_user_won = not is_users_move

    if is_user_won:
        print(
            """
             ___________
            '._==_==_=_.'
            .-\: YOU  /-.
           | (|: WON  ) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
            """
        )
    else:
        print("UNFORTUNATELY, YOU HAVE LOST.")
        print(
            """
                  _____
                 |     |
                 | | | |
                 |_____|
           ____ ___|_|___ ____
          ()___)         ()___)
          // /|    YOU    |\ \\
         // / |    LOST   | \ \\
        (___) |___________| (___)
        (___)   (_______)   (___)
        (___)     (___)     (___)
        (___)      |_|      (___)
        (___)  ___/___\___   | |
         | |  |           |  | |
         | |  |___________| /__|
        /___\  |||     ||| //   \\
       //   \\ |||     ||| \\   //
       \\   // |||     |||  \\ //
        \\ // ()__)   (__()
              ///       \\
             ///         \\
           _///___     ___\\__
          |_______|   |_______|
            """
        )