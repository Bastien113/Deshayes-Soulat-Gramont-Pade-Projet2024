import unittest
import constants

class TestConstants(unittest.TestCase):
    # Test pour vérifier la constante de la taille de l'écran
    def test_screen_size(self):
        self.assertEqual(constants.SCREEN_SIZE, 300)

    # Test pour vérifier la constante de la taille des carrés
    def test_square_size(self):
        self.assertEqual(constants.SQUARE_SIZE, constants.SCREEN_SIZE // 3)

    # Test pour vérifier la constante de la largeur des lignes
    def test_line_width(self):
        self.assertEqual(constants.LINE_WIDTH, 10)

    # Test pour vérifier les constantes de couleur
    def test_colors(self):
        self.assertEqual(constants.LINE_COLOR, (0, 0, 0))
        self.assertEqual(constants.X_COLOR, (66, 66, 66))
        self.assertEqual(constants.O_COLOR, (28, 170, 156))
        self.assertEqual(constants.VICTORY_COLOR, (255, 0, 0))
        self.assertEqual(constants.WHITE, (255, 255, 255))

if __name__ == '__main__':
    unittest.main()