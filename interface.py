import pygame
from constants import *

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
ecran = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Morpion")

def dessiner_lignes():
    """Dessine les lignes de la grille de jeu."""
    for i in range(1, 3):
        pygame.draw.line(ecran, LINE_COLOR, (0, i * SQUARE_SIZE), (SCREEN_SIZE, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(ecran, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_SIZE), LINE_WIDTH)

def dessiner_X(ligne, col):
    """Dessine le symbole X sur la grille à la position spécifiée."""
    start_x = col * SQUARE_SIZE + 20
    start_y = ligne * SQUARE_SIZE + 20
    end_x = (col + 1) * SQUARE_SIZE - 20
    end_y = (ligne + 1) * SQUARE_SIZE - 20
    pygame.draw.line(ecran, X_COLOR, (start_x, start_y), (end_x, end_y), LINE_WIDTH)
    pygame.draw.line(ecran, X_COLOR, (start_x, end_y), (end_x, start_y), LINE_WIDTH)

def dessiner_O(ligne, col):
    """Dessine le symbole O sur la grille à la position spécifiée."""
    centre_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    centre_y = ligne * SQUARE_SIZE + SQUARE_SIZE // 2
    rayon = SQUARE_SIZE // 3
    pygame.draw.circle(ecran, O_COLOR, (centre_x, centre_y), rayon, LINE_WIDTH)

def dessiner_XO(plateau):
    """Dessine les symboles X et O sur la grille en fonction de l'état du plateau."""
    ecran.fill(WHITE)  # Ajoutez cette ligne pour effacer l'écran avant de redessiner
    for ligne in range(3):
        for col in range(3):
            if plateau[ligne][col] == "X":
                dessiner_X(ligne, col)
            elif plateau[ligne][col] == "O":
                dessiner_O(ligne, col)
    dessiner_lignes()  # Redessinez les lignes de la grille

def afficher_message(message):
    """Affiche un message au centre de l'écran."""
    ecran.fill(WHITE)
    font = pygame.font.Font(None, 36)
    texte = font.render(message, True, LINE_COLOR)
    texte_rect = texte.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))
    ecran.blit(texte, texte_rect)
    pygame.display.update()
    pygame.time.wait(2000)

def menu():
    """Affiche le menu de démarrage du jeu."""
    ecran.fill(WHITE)
    font = pygame.font.Font(None, 24)

    lignes_texte = [
        "Bienvenue dans le Morpion !",
        "",
        "Cliquez ou appuyez sur une touche",
        "pour commencer la partie."
    ]

    espacement = 10
    total_hauteur = len(lignes_texte) * font.get_height() + (len(lignes_texte) - 1) * espacement
    y_depart = (SCREEN_SIZE - total_hauteur) // 2

    for i, ligne in enumerate(lignes_texte):
        texte = font.render(ligne, True, LINE_COLOR)
        texte_rect = texte.get_rect(center=(SCREEN_SIZE // 2, y_depart + i * (font.get_height() + espacement)))
        ecran.blit(texte, texte_rect)

    bouton_rect = pygame.Rect(0, 0, SCREEN_SIZE, SCREEN_SIZE)
    pygame.display.update()

    attendre_menu(bouton_rect)

def attendre_menu(bouton_rect):
    """Attend une interaction utilisateur pour quitter le menu."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and bouton_rect.collidepoint(event.pos)):
                return

def reinitialiser_ecran():
    """Réinitialise l'écran pour une nouvelle partie."""
    ecran.fill(WHITE)
    dessiner_lignes()
    pygame.display.update()