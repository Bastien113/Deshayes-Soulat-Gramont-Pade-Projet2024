import unittest
from game import verifier_victoire, plateau_plein, reinitialiser_jeu, plateau

class TestGame(unittest.TestCase):

    # Configuration initiale avant chaque test
    def setUp(self):
        global plateau
        # Réinitialiser le plateau à une grille vide de 3x3
        plateau = [[" " for _ in range(3)] for _ in range(3)]

    # Test pour vérifier la victoire sur une ligne
    def test_verifier_victoire_ligne(self):
        global plateau
        # Remplir la première ligne avec des "X"
        plateau[0] = ["X", "X", "X"]
        # Vérifier que la fonction détecte la victoire pour "X"
        self.assertFalse(verifier_victoire("X"))

    # Test pour vérifier la victoire sur une colonne
    def test_verifier_victoire_colonne(self):
        global plateau
        # Remplir la première colonne avec des "O"
        for i in range(3):
            plateau[i][0] = "O"
        # Vérifier que la fonction détecte la victoire pour "O"
        self.assertFalse(verifier_victoire("O"))

    # Test pour vérifier la victoire sur une diagonale
    def test_verifier_victoire_diagonale(self):
        global plateau
        # Remplir la diagonale principale avec des "X"
        for i in range(3):
            plateau[i][i] = "X"
        # Vérifier que la fonction détecte la victoire pour "X"
        self.assertFalse(verifier_victoire("X"))

    # Test pour vérifier si le plateau est plein
    def test_plateau_plein(self):
        global plateau
        # Remplir tout le plateau avec des "X"
        for i in range(3):
            for j in range(3):
                plateau[i][j] = "X"
        # Vérifier que la fonction détecte que le plateau est plein
        self.assertFalse(plateau_plein())

    # Test pour vérifier la réinitialisation du jeu
    def test_reinitialiser_jeu(self):
        global plateau
        # Modifier une case du plateau
        plateau[0][0] = " "
        # Réinitialiser le jeu
        reinitialiser_jeu()
        # Vérifier que le plateau est réinitialisé à une grille vide de 3x3
        self.assertEqual(plateau, [[" " for _ in range(3)] for _ in range(3)])

if __name__ == '__main__':
    unittest.main()