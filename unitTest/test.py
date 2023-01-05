import unittest
import main

class TestGame(unittest.TestCase):
    def test_game(self):
        answer = 5
        guess = 5
        result = main.run_guess(guess, answer)
        self.assertTrue(result)

    def test_game_wrongGuess(self):
        answer = 5
        guess = 1
        result = main.run_guess(guess, answer)
        self.assertFalse(result)

    def test_game_outOfRange(self):
        answer = 5
        guess = 12
        result = main.run_guess(guess, answer)
        self.assertFalse(result)

    def test_game_typeErr(self):
        answer = '5'
        guess = 11
        result = main.run_guess(guess, answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
