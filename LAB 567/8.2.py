import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Размеры клетки
BLOCK_SIZE = 20

# FPS
FPS = 10
clock = pygame.time.Clock()

# Класс для змейки
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = 'UP'
        self.length = 1

    def update(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            head_y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            head_y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            head_x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            head_x += BLOCK_SIZE
        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.length += 1
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    def is_collision_with_self(self):
        return self.body[0] in self.body[1:]

    def is_collision_with_border(self):
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Класс для еды
class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Главная функция игры
def game():
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    font = pygame.font.SysFont('Arial', 30)

    global FPS
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                if event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'

        snake.update()

        # Проверка на столкновение с границей или с самой собой
        if snake.is_collision_with_self() or snake.is_collision_with_border():
            running = False

        # Проверка на съедание еды
        if snake.body[0] == food.position:
            snake.grow()
            score += 1
            food = Food(snake.body)  # Генерация новой еды

            # Если змейка съела 3-4 еды, увеличиваем уровень и скорость
            if score % 4 == 0:
                level += 1
                FPS += 2  # Увеличиваем скорость

        screen.fill(BLACK)
        snake.draw()
        food.draw()

        # Отображение счета и уровня
        score_text = font.render(f"Score: {score}", True, BLUE)
        level_text = font.render(f"Level: {level}", True, BLUE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Запуск игры
game()
