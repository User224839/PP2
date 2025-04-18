import pygame
import random
import psycopg2

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
        self.base_speed = 100  # базовая скорость (задержка в мс)
        self.speed = self.base_speed
        self.score = 0
        self.level = 1

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.body
        ):
            return False  # Game over

        self.body.insert(0, new_head)

        if self.growing > 0:
            self.growing -= 1
        else:
            self.body.pop()

        return True

    def grow(self, size):
        self.growing += size
        self.score += size

        # Check if it's time to level up
        if self.score // 20 + 1 > self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.speed = max(10, self.speed // 2)  # Уменьшаем задержку вдвое, но не меньше 10 мс
        print(f"LEVEL UP! Now at level {self.level}, new speed: {self.speed}ms")

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
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
        self.weight = random.randint(1, 3)
        self.color = RED if self.weight == 1 else BLUE if self.weight == 2 else WHITE
        self.timer = pygame.time.get_ticks() + random.randint(3000, 7000)

    def is_expired(self):
        return pygame.time.get_ticks() > self.timer

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Database connection
def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        port=1234,
        database="postgres",  # Поменяй на свою базу если нужно
        user="postgres",
        password="simplenurik"
    )

# Check user login and retrieve score and level
def login_user():
    username = input("Enter your username: ")
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT score, level FROM user_score WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        score, level = result
        print(f"Welcome back {username}! Your score: {score}, level: {level}")
    else:
        cur.execute("INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)", (username, 0, 1))
        conn.commit()
        print(f"New user {username} created! Starting with score: 0, level: 1")
        score, level = 0, 1

    cur.close()
    conn.close()
    return username, score, level

# Update score and level in database
def update_score(username, score, level):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE username = %s", (score, level, username))
    conn.commit()
    cur.close()
    conn.close()

# Game loop
def game_loop(username):
    clock = pygame.time.Clock()
    snake = Snake()
    foods = [Food() for _ in range(3)]

    font = pygame.font.SysFont(None, 36)

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

        # Draw score and level
        score_text = font.render(f"Score: {snake.score}  Level: {snake.level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.delay(snake.speed)

    # Update user score and level after game ends
    update_score(username, snake.score, snake.level)
    pygame.quit()

# Main program
def main():
    username, score, level = login_user()  # Get username, score, and level from the login
    game_loop(username)  # Start the game loop

if __name__ == "__main__":
    main()
