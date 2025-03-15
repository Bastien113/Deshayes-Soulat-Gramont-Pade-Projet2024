import pygame
from constants import *
from interface import dessiner_XO, afficher_message, menu, reinitialiser_ecran

# Initialisation du plateau de jeu
plateau = [[" " for _ in range(3)] for _ in range(3)]
joueur_actuel = "X"

def verifier_victoire(joueur):
    """Vérifie si le joueur a gagné en alignant trois symboles."""
    for ligne in range(3):
        if plateau[ligne][0] == plateau[ligne][1] == plateau[ligne][2] == joueur:
            return True
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] == joueur:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

def plateau_plein():
    """Vérifie si toutes les cases du plateau sont remplies."""
    for ligne in plateau:
        if " " in ligne:
            return False
    return True

def reinitialiser_jeu():
    """Réinitialise le plateau de jeu et le joueur actuel, et rafraîchit l'écran."""
    global plateau, joueur_actuel
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"
    reinitialiser_ecran()

def jeu():
    """Boucle principale du jeu qui gère les interactions et la logique de jeu."""
    global joueur_actuel
    menu()
    reinitialiser_ecran()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                souris_x = event.pos[0] // SQUARE_SIZE
                souris_y = event.pos[1] // SQUARE_SIZE

                if plateau[souris_y][souris_x] == " ":
                    plateau[souris_y][souris_x] = joueur_actuel
                    if verifier_victoire(joueur_actuel):
                        afficher_message(f"Joueur {joueur_actuel} a gagné !")
                        reinitialiser_jeu()
                        menu()
                    elif plateau_plein():
                        afficher_message("Match nul !")
                        reinitialiser_jeu()
                        menu()
                    else:
                        joueur_actuel = "O" if joueur_actuel == "X" else "X"

                    dessiner_XO(plateau)
                    pygame.display.update()

        dessiner_XO(plateau)
        pygame.display.update()