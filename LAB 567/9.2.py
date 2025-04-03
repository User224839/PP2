import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Размеры клеток
BLOCK_SIZE = 20

# Часы для управления FPS
clock = pygame.time.Clock()

# Шрифт для отображения счета
font = pygame.font.SysFont("Arial", 20)

# Класс для еды
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.rect.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.weight = random.randint(1, 5)  # Случайный вес пищи
        self.creation_time = time.time()  # Время создания пищи
        self.lifetime = 10  # Пища исчезает через 10 секунд

    def update(self):
        # Проверка, прошло ли достаточно времени (пища исчезает через 10 секунд)
        if time.time() - self.creation_time > self.lifetime:
            self.kill()  # Убираем пищу с экрана, если время прошло

# Класс для змеи
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Изначально змея длиной 3
        self.direction = "RIGHT"
        self.alive = True
        self.score = 0

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            head_y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE
        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        # Добавляем новую голову и удаляем хвост
        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        # Добавляем новый сегмент к телу змеи
        tail_x, tail_y = self.body[-1]
        if self.direction == "UP":
            tail_y += BLOCK_SIZE
        elif self.direction == "DOWN":
            tail_y -= BLOCK_SIZE
        elif self.direction == "LEFT":
            tail_x += BLOCK_SIZE
        elif self.direction == "RIGHT":
            tail_x -= BLOCK_SIZE
        self.body.append((tail_x, tail_y))

    def check_collision(self):
        head_x, head_y = self.body[0]

        # Проверка столкновения с границей экрана
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.alive = False

        # Проверка столкновения с телом змеи
        if (head_x, head_y) in self.body[1:]:
            self.alive = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    def get_head_position(self):
        return self.body[0]

# Инициализация
snake = Snake()
foods = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Функция для создания новой еды
def create_food():
    food = Food()
    foods.add(food)
    all_sprites.add(food)

# Создаем начальную еду
for _ in range(3):  # Начальное количество пищи
    create_food()

# Главный игровой цикл
running = True
while running:
    clock.tick(10)  # FPS игры

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    # Двигаем змею
    snake.move()

    # Проверка столкновений змеи с едой
    head_x, head_y = snake.get_head_position()

    # Создаем временный спрайт для головы змеи
    head_sprite = pygame.sprite.Sprite()
    head_sprite.rect = pygame.Rect(head_x, head_y, BLOCK_SIZE, BLOCK_SIZE)

    # Проверка столкновения с едой
    food_hit = pygame.sprite.spritecollideany(head_sprite, foods)
    if food_hit:
        snake.grow()  # Змея растет
        snake.score += food_hit.weight  # Добавляем вес съеденной пищи к счету
        food_hit.kill()  # Убираем съеденную пищу
        create_food()  # Генерируем новую еду

    # Проверка столкновений с границей или телом змеи
    snake.check_collision()

    # Отображаем игру
    screen.fill(BLACK)

    # Отображаем змею
    snake.draw(screen)

    # Обновляем все спрайты
    all_sprites.update()

    # Выводим счет
    score_text = font.render(f"Score: {snake.score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Обновляем экран
    pygame.display.flip()

    if not snake.alive:
        running = False

pygame.quit()
