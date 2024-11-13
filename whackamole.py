import pygame
import random


def main():
    try:
        pygame.init()
        GRID_WIDTH = 32
        GRID_HEIGHT = 32
        GRID_COLS = 20
        GRID_ROWS = 16
        SCREEN_WIDTH = GRID_WIDTH * GRID_COLS
        SCREEN_HEIGHT = GRID_HEIGHT * GRID_ROWS

        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_x, mole_y = 0, 0  # Start mole in top-left corner
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + GRID_WIDTH and mole_y <= mouse_y < mole_y + GRID_HEIGHT:
                        mole_x = random.randrange(GRID_COLS) * GRID_WIDTH
                        mole_y = random.randrange(GRID_ROWS) * GRID_HEIGHT

            screen.fill("light green")
            for x in range(0, SCREEN_WIDTH, GRID_WIDTH):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_HEIGHT):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
