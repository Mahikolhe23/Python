import  random
from game_data import  data

def selecter(user_1,user_2):
    count = 0
    game = True
    while game:
        user_1_name = user_1['name']
        user_1_score = user_1['follower_count']
        user_2_name = user_2['name']
        user_2_score = user_2['follower_count']
        print('Enter who had more followers on instagram')
        print(f'A : {user_1_name}')
        print('VS')
        print(f'B : {user_2_name} ')
        ans = str(input()).lower()
        if ans == 'a' and user_1_score > user_2_score:
            user_1 = user_2
            user_2 = random.choice(data)
            count += 1
        else:
            game = False
    return  count
def game():
    user_1 = random.choice(data)
    user_2 = random.choice(data)
    print(f'You won {selecter(user_1,user_2)} times')

game()