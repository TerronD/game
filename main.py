import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption("Игра 2000 онлайн без регистрации")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png')

walk_left = [
    pygame.image.load('images/player/playerjpg.jpg')
]
walk_right = [
    pygame.image.load('images/player/playerjpg.jpg')
]



worm = pygame.image.load('images/worm.png')
worm_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 300
player_y = 800

is_jump = False
jump_count = 12

bg_sound = pygame.mixer.Sound('sounds/nokia-tune-original meloboom.mp3')
# bg_sound.play()

worm_timer = pygame.USEREVENT + 1
pygame.time.set_timer(worm_timer, 2500)

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1920, 0))
    screen.blit(walk_right[player_anim_count], (player_x, player_y))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    if worm_list_in_game:
        for el in worm_list_in_game:
            screen.blit(worm, el)
            el.x -= 10

            if player_rect.colliderect(el):
                print("Помер")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_a] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 1700:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -12:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 12

    bg_x -= 2
    if bg_x == -1920:
        bg_x = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == worm_timer:
            worm_list_in_game.append(worm.get_rect(topleft=(1700, 830)))

