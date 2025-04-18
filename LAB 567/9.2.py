import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)
        self.growing = 0
        self.speed = 100  # Snake speed in milliseconds

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Check border collision
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.body
        ):
            return False  # Game over condition

        self.body.insert(0, new_head)

        if self.growing > 0:
            self.growing -= 1
        else:
            self.body.pop()

        return True

    def grow(self, size):
        self.growing += size

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:  # Prevent moving backward
            self.direction = new_direction

    def get_head_position(self):
        return self.body[0]

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.position = (
            random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
            random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        )
        self.weight = random.randint(1, 3)  # Food can have weight 1, 2, or 3
        self.color = RED if self.weight == 1 else BLUE if self.weight == 2 else WHITE
        self.timer = pygame.time.get_ticks() + random.randint(3000, 7000)  # 3-7 seconds

    def is_expired(self):
        return pygame.time.get_ticks() > self.timer

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Game loop
clock = pygame.time.Clock()
snake = Snake()
foods = [Food() for _ in range(3)]  # Multiple foods

running = True
while running:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -GRID_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, GRID_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-GRID_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((GRID_SIZE, 0))

    # Move snake
    if not snake.move():
        running = False  # Game over

    # Check food collision
    for food in foods:
        if snake.get_head_position() == food.position:
            snake.grow(food.weight)
            food.respawn()

    # Remove expired food and replace it
    for food in foods:
        if food.is_expired():
            food.respawn()

    # Draw everything
    snake.draw()
    for food in foods:
        food.draw()

    pygame.display.flip()
    pygame.time.delay(snake.speed)  # Adjust speed based on game mechanics

pygame.quit()
