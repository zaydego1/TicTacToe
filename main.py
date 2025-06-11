from game import board

def main():
    game_board = board.Board(3)
    game_board.move(0, 0, 1)
    game_board.move(0, 1, 2)
    game_board.move(1, 1, 1)
    game_board.move(2, 2, 2)
    game_board.move(2, 0, 1)
    game_board.move(1, 0, 2)
    game_board.move(1, 2, 1)
    game_board.move(0, 2, 2)
    game_board.move(2, 1, 1)


    # Game 2: Player 2 wins
    game2 = board.Board(3)
    game2.move(0, 0, 1)
    game2.move(1, 0, 2)
    game2.move(0, 1, 1)
    game2.move(1, 1, 2)
    game2.move(2, 2, 1)
    game2.move(1, 2, 2)  # Player 2 wins

    # Game 3: Player 1 wins diagonally
    game3 = board.Board(3)
    game3.move(0, 0, 1)
    game3.move(0, 1, 2)
    game3.move(1, 1, 1)
    game3.move(0, 2, 2)
    game3.move(2, 2, 1)  # Player 1 wins

    # Drawn games
    # Game 4: Draw
    game4 = board.Board(3)
    game4.move(0, 0, 1)
    game4.move(0, 1, 2)
    game4.move(0, 2, 1)
    game4.move(1, 1, 2)
    game4.move(1, 0, 1)
    game4.move(1, 2, 2)
    game4.move(2, 1, 1)
    game4.move(2, 0, 2)
    game4.move(2, 2, 1)  # Draw

    # Game 5: Draw
    game5 = board.Board(3)
    game5.move(0, 0, 2)
    game5.move(0, 1, 1)
    game5.move(0, 2, 2)
    game5.move(1, 0, 1)
    game5.move(1, 1, 2)
    game5.move(1, 2, 1)
    game5.move(2, 0, 1)
    game5.move(2, 1, 2)
    game5.move(2, 2, 1)  # Draw

    # Game 6: Draw
    game6 = board.Board(3)
    game6.move(0, 0, 1)
    game6.move(0, 1, 2)
    game6.move(0, 2, 1)
    game6.move(1, 0, 2)
    game6.move(1, 1, 1)
    game6.move(1, 2, 2)
    game6.move(2, 0, 2)
    game6.move(2, 1, 1)
    game6.move(2, 2, 2)  # Draw

    # Exception games
    # Game 7: Invalid move (cell already taken)
    try:
        game7 = board.Board(3)
        game7.move(0, 0, 1)
        game7.move(0, 0, 2)  # Exception expected
    except Exception as e:
        print(f"Game 7 Exception: {e}")

    # Game 8: Invalid player number
    try:
        game8 = board.Board(3)
        game8.move(0, 0, 3)  # Exception expected
    except Exception as e:
        print(f"Game 8 Exception: {e}")

    # Game 9: Move out of bounds
    try:
        game9 = board.Board(3)
        game9.move(3, 3, 1)  # Exception expected
    except Exception as e:
        print(f"Game 9 Exception: {e}")

if __name__ == '__main__':
    main()