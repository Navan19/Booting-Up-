#Testing first screen independantly

import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Booting Up')

WHITE = (255,255,255)
BlACK = (0,0,0)
GREEN = (65,196,14)
font = pygame.font.SysFont(None, 70) #Just the Default Font, size 70

game_state = "FIRST SCREEN"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if game_state == "FIRST SCREEN" and event.type == pygame.KEYDOWN:
            running = False

if game_state == "FIRST SCREEN":
    screen.fill(0,0,0)
    screen.blit(font.render(game_state, True, WHITE), (0,0))
    game_text = font.render("Game Running", True, GREEN)
    game_rect = game_text.get_rect(center=(800, 400))
    screen.blit(game_text, game_rect)



pygame.display.flip()
pygame.quit()
