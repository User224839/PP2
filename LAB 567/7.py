import pygame
import time
import math

# Инициализация Pygame
pygame.init()

# Опции экрана
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображения Микки (замените на путь к вашему изображению)
mickey = pygame.image.load("mickey.png")
mickey = pygame.transform.scale(mickey, (WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Функция для рисования стрелок
def draw_hand(surface, angle, length, color, width=5):
    angle_rad = math.radians(angle)
    x = WIDTH // 2 + length * math.cos(angle_rad)
    y = HEIGHT // 2 - length * math.sin(angle_rad)
    pygame.draw.line(surface, color, (WIDTH // 2, HEIGHT // 2), (x, y), width)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    # Получаем текущее время
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Вычисляем углы поворота
    min_angle = 360 - (minutes % 60) * 6
    sec_angle = 360 - (seconds % 60) * 6

    # Рисуем стрелки
    draw_hand(screen, min_angle, 80, (0, 0, 255), 6)  # Минутная стрелка (правая рука)
    draw_hand(screen, sec_angle, 100, (255, 0, 0), 4)  # Секундная стрелка (левая рука)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
