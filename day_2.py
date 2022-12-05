from common_functions import load_as_string_array

def play_rpc(opponent, player):
    ord_player = ord(player) - 87
    ord_opponent = ord(opponent) - 64
    # print(ord_player, end=' - ')
    # print(ord_opponent)
    if ord_player-ord_opponent == 0:
        print('Tie: '+ str(ord_player) + " "+ str(ord_opponent), end=' ')
        return 3
    if (ord_opponent)%3 == ord_player-1:
        print('Win! '+ str(ord_player) + " "+ str(ord_opponent), end=' ')
        return 6
    else:
        print('Loss... '+ str(ord_player) + " "+ str(ord_opponent), end=' ')
        return 0

def part_1():
    my_total_score = 0
    for line in arr:
        letter_score = ord(line[2]) - 87
        game_score = play_rpc(line[0], line[2])
        line_score = game_score + letter_score
        print()
        print(letter_score)
        # print(line_score)
        my_total_score += line_score

    print("total:")
    print(my_total_score)


if __name__ == '__main__':
    arr = load_as_string_array('data/day_2_data.txt')
    # part_1()
    total_score = 0
    for line in arr:
        game_result = line[2]
        opponent = ord(line[0]) - 64
        if game_result == 'X': # loose
            player = (opponent-2) % 3
            player += 1
            print("lose " + str(player))
            total_score += player
        elif game_result == 'Y':
            total_score += opponent + 3
            print("tie " + str(opponent))
        else:
            player = (opponent) % 3
            player += 1
            total_score += player + 6
            print("win " + str(player))
    print(total_score)

