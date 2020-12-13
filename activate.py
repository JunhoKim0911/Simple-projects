import random
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Rona vs snowballs")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\rona_gift\\background_1.jpg")
gameover = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\rona_gift\\gameover.png")

character = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\rona_gift\\rona.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10

snow = pygame.image.load("C:\\Users\\user\\Desktop\\PythonWorkspace\\rona_gift\\snow_4.png")
snow_size = snow.get_rect().size
snow_width = snow_size[0]
snow_height = snow_size[1]
snow_x_pos = random.randint(0, screen_width - snow_width)
snow_y_pos = 0
snow_speed = 5

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    snow_y_pos += snow_speed

    if snow_y_pos > screen_height:
        snow_x_pos = random.randint(0, screen_width - snow_width)
        snow_y_pos = 0
        
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    snow_rect = snow.get_rect()
    snow_rect.left = snow_x_pos
    snow_rect.top = snow_y_pos

    if character_rect.colliderect(snow_rect):
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(snow, (snow_x_pos, snow_y_pos))

    pygame.display.update()

screen.blit(gameover, (0, 0))
finish_font = pygame.font.Font(None, 40)
first = finish_font.render("Merry X-mas", True, (255, 0, 0))
second = finish_font.render("Rona :)", True, (0, 102, 51))

screen.blit(first, (160, 30))
screen.blit(second, (200, 65))
pygame.display.update()

pygame.time.delay(5000)

pygame.quit()