import pygame
from sys import exit

# --- Init & Window -----------------------------------------------------------
pygame.init()
WIDTH, HEIGHT = 800, 400                   # Single source of truth for size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()                # Frame rate controller (60 FPS target)

# --- Assets & Resources ------------------------------------------------------
# Fonts: cache once; render returns a Surface (don't re-render every frame)
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Images: convert() for opaque, convert_alpha() for images with transparency
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My Game", False, "Black")

# Snail: keep both the Surface (image) and Rect (position/size)
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# Place the snail so its bottom sits on the ground at y=300
snail_rect = snail_surface.get_rect(bottomleft=(600, 300))

# Player
player_surf = pygame.image.load(
    "graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

# --- Main Game Loop ----------------------------------------------------------
while True:
    # 1) Handle OS/window events (close button, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 2) Update game state (movement, timers, etc.)
    # Move snail left by 2 pixels per frame
    snail_rect.x -= 2

    # If the snail leaves the screen to the left, wrap it back to the right
    if snail_rect.right <= 0:               # fully off-screen
        snail_rect.left = WIDTH            # re-enter from the right edge

    # 3) Draw everything (back-to-front)
    # Background layers first
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    # Actors (use their rects for blitting so image+position stay in sync)
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)

    # 4) Flip the back buffer to the screen and cap FPS
    pygame.display.update()
    clock.tick(60)  # Run the loop at most 60 times per second
