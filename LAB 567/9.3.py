#r — рисует прямоугольник.
#t — рисует прямой треугольник.
#e — рисует равносторонний треугольник.
#h — рисует ромб.
#l — рисует линию (по умолчанию).
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the clock
clock = pygame.time.Clock()

# Shape modes (for toggling between shapes)
DRAW_RECTANGLE = 1
DRAW_TRIANGLE = 2
DRAW_EQ_TRIANGLE = 3
DRAW_RHOMBUS = 4
DRAW_LINE = 5

current_shape = DRAW_RECTANGLE  # Default to drawing a rectangle
drawing = False
start_pos = (0, 0)

# Function to draw a rectangle
def draw_rectangle(surface, start, end, color):
    pygame.draw.rect(surface, color, pygame.Rect(start, (end[0] - start[0], end[1] - start[1])))

# Function to draw a right triangle
def draw_right_triangle(surface, start, end, color):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, start, end, color):
    # Calculate the height of the equilateral triangle
    height = (end[0] - start[0]) * (3 ** 0.5) / 2
    top_point = (start[0] + (end[0] - start[0]) / 2, start[1] - height)
    points = [start, end, top_point]
    pygame.draw.polygon(surface, color, points)

# Function to draw a rhombus
def draw_rhombus(surface, start, end, color):
    # Calculate the center and create the 4 points of the rhombus
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    points = [
        (start[0], center[1]),
        (center[0], start[1]),
        (end[0], center[1]),
        (center[0], end[1])
    ]
    pygame.draw.polygon(surface, color, points)

# Main function
def main():
    global current_shape, drawing, start_pos
    screen.fill(WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click to start drawing
                    start_pos = event.pos
                    drawing = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left click to stop drawing
                    end_pos = event.pos
                    if current_shape == DRAW_RECTANGLE:
                        draw_rectangle(screen, start_pos, end_pos, BLACK)
                    elif current_shape == DRAW_TRIANGLE:
                        draw_right_triangle(screen, start_pos, end_pos, BLACK)
                    elif current_shape == DRAW_EQ_TRIANGLE:
                        draw_equilateral_triangle(screen, start_pos, end_pos, BLACK)
                    elif current_shape == DRAW_RHOMBUS:
                        draw_rhombus(screen, start_pos, end_pos, BLACK)
                    drawing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'r' to draw rectangle
                    current_shape = DRAW_RECTANGLE
                elif event.key == pygame.K_t:  # Press 't' to draw right triangle
                    current_shape = DRAW_TRIANGLE
                elif event.key == pygame.K_e:  # Press 'e' to draw equilateral triangle
                    current_shape = DRAW_EQ_TRIANGLE
                elif event.key == pygame.K_h:  # Press 'h' to draw rhombus
                    current_shape = DRAW_RHOMBUS
                elif event.key == pygame.K_l:  # Press 'l' to draw line (default mode)
                    current_shape = DRAW_LINE

        # Clear screen and redraw shapes
        if drawing:
            end_pos = pygame.mouse.get_pos()
            if current_shape == DRAW_RECTANGLE:
                draw_rectangle(screen, start_pos, end_pos, BLACK)
            elif current_shape == DRAW_TRIANGLE:
                draw_right_triangle(screen, start_pos, end_pos, BLACK)
            elif current_shape == DRAW_EQ_TRIANGLE:
                draw_equilateral_triangle(screen, start_pos, end_pos, BLACK)
            elif current_shape == DRAW_RHOMBUS:
                draw_rhombus(screen, start_pos, end_pos, BLACK)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
