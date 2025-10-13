from dice_game.game import Game
from dice_game.player import Player
def main():
    player_1 = Player("test 1")
    player_2 = Player("test 2")

    game = Game()
    
    hold = False

    while True:
        turn = game.play_turn(player_1, hold)
        print(turn)
        if turn == False:
            print("turn over")
            break
        else:
            print(f"Your score is: {player_1.get_score()}")

        hold = input('Hold? y/n: ').lower().startswith('y')
        
        


   

if __name__ == "__main__":
    main()