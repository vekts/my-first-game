import pygame

pygame.init()

screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("My First Game!")
pygame.display.set_icon(pygame.image.load('images/icon.webp'))

square = pygame.Surface((50, 50))
square.fill((51, 49, 56))

text = pygame.font.Font(None,30)
font_text = text.render("Crazy Game!",True, (51, 49, 56))
play_img = pygame.image.load('images/img_toplay.webp')
size_img = pygame.transform.scale(play_img, (60, 60))

running = True
bc_color = (84, 77, 184)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bc_color = (119, 75, 122)

    screen.fill(bc_color)
    screen.blit(square, (290, 150))
    screen.blit(font_text, (250, 120))
    screen.blit(size_img, (285, 195))
    pygame.draw.circle(square, 'White', (40, 40), 20)
    pygame.display.update()

pygame.quit()
