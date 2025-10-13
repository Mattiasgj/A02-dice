from dice_game.game import Game
from dice_game.player import Player

def main():
    player_1 = Player("test 1")
    player_2 = Player("test 2")

    game = Game(player_1, player_2)
    
    hold = False

    current_player = player_1
    
    while True:
        turn = game.play_turn(current_player, hold)
        print(turn)
        if turn == False:
            current_player = game.switch_turns(current_player)
            print(f"turn over, now its {current_player.get_name()} turn")
        else:
            print(f"Your score is: {current_player.get_score()}")

        hold = input('Hold? y/n: ').lower().startswith('y')
        
        


   

if __name__ == "__main__":
    main()