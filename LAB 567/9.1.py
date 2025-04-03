import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Загрузка изображений
car_image = pygame.image.load(r"C:\Users\Nurdaulet\Desktop\PP2\LAB 567\assets\car.png")
coin_image = pygame.image.load(r"C:\Users\Nurdaulet\Desktop\PP2\LAB 567\assets\coin.png")

# Масштабирование изображения монеты, чтобы оно было корректного размера
coin_image = pygame.transform.scale(coin_image, (32, 32))  # Устанавливаем размер монеты (например 32x32)

# Часы для управления FPS
clock = pygame.time.Clock()

# Переменные игры
car_speed = 5
enemy_speed = 5
coin_count_player1 = 0
coin_count_player2 = 0
font = pygame.font.SysFont('Arial', 30)

# Класс для машины
class Car(pygame.sprite.Sprite):
    def __init__(self, controls):
        super().__init__()
        self.image = car_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed = car_speed
        self.controls = controls  # Управление (стрелки или WASD)

    def update(self, keys):
        if self.controls == 'arrows':
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.speed
        elif self.controls == 'wasd':
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.right < WIDTH:
                self.rect.x += self.speed

# Класс для монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Начало за пределами экрана
        self.weight = random.randint(1, 5)  # Случайный вес монеты

    def update(self):
        self.rect.y += 5  # Монеты двигаются вниз
        if self.rect.top > HEIGHT:  # Если монета выходит за пределы экрана
            self.kill()  # Убираем монету с экрана
            new_coin = Coin()
            all_sprites.add(new_coin)
            coins.add(new_coin)

# Класс для врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-150, -50)

    def update(self):
        self.rect.y += enemy_speed  # Враг двигается вниз
        if self.rect.top > HEIGHT:  # Если враг выходит за пределы экрана, сбрасываем его
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-150, -50)

# Инициализация групп спрайтов
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Инициализация двух машин, врагов и монет
player1 = Car('arrows')
player2 = Car('wasd')
all_sprites.add(player1, player2)

# Генерация врагов и монет
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

for _ in range(3):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

# Главный игровой цикл
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем состояния клавиш и обновляем позиции машин
    keys = pygame.key.get_pressed()
    player1.update(keys)
    player2.update(keys)

    # Обновляем монеты и врагов
    for sprite in all_sprites:
        if isinstance(sprite, Car):
            sprite.update(keys)  # Обновляем с использованием клавиш
        else:
            sprite.update()  # Враг и монета не требуют клавиш для обновления

    # Проверка на столкновения машин с монетами
    coin_hits1 = pygame.sprite.spritecollide(player1, coins, True)
    coin_hits2 = pygame.sprite.spritecollide(player2, coins, True)
    
    # Обработка сбора монет первым игроком
    for coin in coin_hits1:
        coin_count_player1 += coin.weight  # Увеличиваем счет за монеты
        if coin_count_player1 >= 10:  # Увеличиваем скорость врага после 10 монет
            enemy_speed += 1
            coin_count_player1 = 0  # Сбросить счет после увеличения скорости

        # Создаем новую монету после сбора
        new_coin = Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)

    # Обработка сбора монет вторым игроком
    for coin in coin_hits2:
        coin_count_player2 += coin.weight  # Увеличиваем счет за монеты
        if coin_count_player2 >= 10:  # Увеличиваем скорость врага после 10 монет
            enemy_speed += 1
            coin_count_player2 = 0  # Сбросить счет после увеличения скорости

        # Создаем новую монету после сбора
        new_coin = Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)

    # Рисуем все спрайты
    all_sprites.draw(screen)

    # Выводим счет для первого игрока (стрелки) в правом верхнем углу
    coin_text1 = font.render(f"Player 1 Coins: {coin_count_player1}", True, WHITE)
    screen.blit(coin_text1, (WIDTH - 250, 10))

    # Выводим счет для второго игрока (WASD) в левом верхнем углу
    coin_text2 = font.render(f"Player 2 Coins: {coin_count_player2}", True, WHITE)
    screen.blit(coin_text2, (10, 10))

    # Обновляем экран
    pygame.display.flip()

# Закрыть игру
pygame.quit()
