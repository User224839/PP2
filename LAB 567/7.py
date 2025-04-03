
# ===== Движущийся мяч =====
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")

ball_pos = [250, 250]
ball_radius = 25
move_step = 20
running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_pos[1] - move_step - ball_radius >= 0:
                ball_pos[1] -= move_step
            elif event.key == pygame.K_DOWN and ball_pos[1] + move_step + ball_radius <= 500:
                ball_pos[1] += move_step
            elif event.key == pygame.K_LEFT and ball_pos[0] - move_step - ball_radius >= 0:
                ball_pos[0] -= move_step
            elif event.key == pygame.K_RIGHT and ball_pos[0] + move_step + ball_radius <= 500:
                ball_pos[0] += move_step

pygame.quit()
