import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Racer")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
car_image = pygame.image.load("C:\\Users\\Nurdaulet\\Desktop\\PP2\\LAB 567\\assets\\car.png")
coin_image = pygame.image.load("C:\\Users\\Nurdaulet\\Desktop\\PP2\\LAB 567\\assets\\coin.png")

# Масштабирование изображений
car_image = pygame.transform.scale(car_image, (50, 100))
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Класс машинки
class Car(pygame.sprite.Sprite):
    def __init__(self, x, controls):
        super().__init__()
        self.image = car_image
        self.rect = self.image.get_rect(center=(x, HEIGHT - 120))
        self.speed = 5
        self.controls = controls
        self.score = 0

    def update(self, keys):
        if keys[self.controls["left"]] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[self.controls["right"]] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        
        # Увеличение скорости каждые 100 очков
        self.speed = 5 * (2 ** (self.score // 100))

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(-200, -50)))
        self.speed = random.randint(2, 5)  

    def update(self):
        self.rect.y += self.speed  # Двигаем монеты вниз
        if self.rect.top > HEIGHT:  # Если монета вышла за экран, сбрасываем её
            self.respawn()

    def respawn(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(-200, -50)
        self.speed = random.randint(2, 5)

# Создание игроков
player1 = Car(WIDTH // 3, {"left": pygame.K_a, "right": pygame.K_d})
player2 = Car(2 * WIDTH // 3, {"left": pygame.K_LEFT, "right": pygame.K_RIGHT})

# Группы спрайтов
all_sprites = pygame.sprite.Group(player1, player2)
coins = pygame.sprite.Group()

# Создание монет
for _ in range(5):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление машин
    keys = pygame.key.get_pressed()
    player1.update(keys)
    player2.update(keys)

    # Обновление монет
    coins.update()

    # Проверка столкновений с монетами
    for player in [player1, player2]:
        collected_coin = pygame.sprite.spritecollideany(player, coins)
        if collected_coin:
            player.score += 10
            collected_coin.respawn()

    # Отрисовка спрайтов
    all_sprites.draw(screen)

    # Отображение очков
    font = pygame.font.Font(None, 36)
    score1_text = font.render(f"Player 1: {player1.score}", True, BLACK)
    score2_text = font.render(f"Player 2: {player2.score}", True, BLACK)
    screen.blit(score1_text, (20, 20))
    screen.blit(score2_text, (WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
