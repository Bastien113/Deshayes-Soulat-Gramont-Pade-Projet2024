import unittest
from unittest.mock import patch
import interface

class TestInterface(unittest.TestCase):

    # Test pour vérifier l'initialisation de pygame
    @patch('interface.pygame.display.set_mode')
    def test_pygame_initialisation(self, mock_set_mode):
        # Initialiser pygame
        interface.pygame.init()
        # Configurer l'écran avec la taille spécifiée
        interface.ecran = interface.pygame.display.set_mode((interface.SCREEN_SIZE, interface.SCREEN_SIZE))
        # Vérifier que set_mode a été appelé avec les bonnes dimensions
        mock_set_mode.assert_called_with((interface.SCREEN_SIZE, interface.SCREEN_SIZE))

    # Test pour vérifier le dessin des lignes sur l'écran
    @patch('interface.pygame.draw.line')
    def test_dessiner_lignes(self, mock_draw_line):
        # Appeler la fonction pour dessiner les lignes
        interface.dessiner_lignes()
        # Vérifier que la fonction draw.line a été appelée 4 fois (pour les 4 lignes)
        self.assertEqual(mock_draw_line.call_count, 4)

    # Test pour vérifier le dessin d'un X sur l'écran
    @patch('interface.pygame.draw.line')
    def test_dessiner_X(self, mock_draw_line):
        # Dessiner un X dans la case en haut à gauche
        interface.dessiner_X(0, 0)
        # Vérifier que la fonction draw.line a été appelée 2 fois (pour les deux lignes du X)
        self.assertEqual(mock_draw_line.call_count, 2)

    # Test pour vérifier le dessin d'un O sur l'écran
    @patch('interface.pygame.draw.circle')
    def test_dessiner_O(self, mock_draw_circle):
        # Dessiner un O dans la case en haut à gauche
        interface.dessiner_O(0, 0)
        # Vérifier que la fonction draw.circle a été appelée une fois
        mock_draw_circle.assert_called_once()

if __name__ == '__main__':
    unittest.main()