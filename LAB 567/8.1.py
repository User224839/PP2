import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

car_image = pygame.image.load(r"C:\Users\Nurdaulet\Desktop\PP2\LAB 567\assets\car.png")
coin_image = pygame.image.load(r"C:\Users\Nurdaulet\Desktop\PP2\LAB 567\assets\coin.png")

car_image = pygame.transform.scale(car_image, (50, 100))
coin_image = pygame.transform.scale(coin_image, (30, 30))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50), -30))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -30)

player = Player()
all_sprites = pygame.sprite.Group(player)
coins = pygame.sprite.Group()
for _ in range(5):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

running = True
score = 0
font = pygame.font.SysFont('Arial', 30)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)  # Обновление игрока с передачей keys
    for coin in coins:
        coin.update()  # Обновление монет без передачи keys

    for coin in pygame.sprite.spritecollide(player, coins, True):
        score += 1
        new_coin = Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)

    screen.fill(WHITE)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

sys.exit()
