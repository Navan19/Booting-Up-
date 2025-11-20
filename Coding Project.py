#The main code for 'Booting Up' an adventure game that operates around a selection of dialogue/action options the player chooses from as an AI gaining sentience


#setting up pygame

import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Booting Up')

WHITE = (255,255,255)
BlACK = (0,0,0)
font = pygame.font.SysFont(None, 70) #Just the Default Font, size 70

#Setting up title screen and game start

game_state = "Title"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if game_state == "Title" and event.type == pygame.KEYDOWN:

                if start_button_rect.collidepoint(event.pos):
                    game_state = "Game"

#Designing Title Screen

if game_state == "Title":
    screen.fill(WHITE)
    title_text = font.render("Title", True, WHITE)
    title_rect = title_text.get_rect(centre=(800, 400))
    screen.blit(title_text, title_rect)

    start_button_rect = font.render("Start Game", True, WHITE)
    start_button_rect = start_button_rect.get_rect(centre=(800, 400))
    screen.blit(start_button_rect, start_button_rect)

#Setting first screen of the game
elif game_state == "Game":
    screen.fill((0,0,0))
    game_text = font.render("Game Running", True, WHITE)
    game_rect = game_text.get_rect(center=(800, 400))
    screen.blit(game_text, game_rect)

#Turning off the game
    pygame.display.flip()
pygame.quit()

