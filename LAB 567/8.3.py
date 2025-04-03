import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    shape_mode = 'free'  # Modes: 'free' (freehand drawing), 'rect' (rectangle), 'circle' (circle), 'eraser'
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Check for quit event or Ctrl+W or Alt+F4 to close
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Switch colors with r, g, b keys
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # Switch drawing modes with key presses
                if event.key == pygame.K_e:  # Eraser mode
                    shape_mode = 'eraser'
                elif event.key == pygame.K_c:  # Circle mode
                    shape_mode = 'circle'
                elif event.key == pygame.K_r:  # Rectangle mode
                    shape_mode = 'rect'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # If mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
                if shape_mode == 'eraser':  # If in eraser mode, remove points (erase)
                    points = [p for p in points if pygame.Rect(position[0]-radius, position[1]-radius, radius*2, radius*2).collidepoint(p[0], p[1])]

        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Draw all points based on the current drawing mode
        i = 0
        while i < len(points) - 1:
            if shape_mode == 'free':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif shape_mode == 'rect':
                drawRectangle(screen, points[i], points[i + 1], radius, mode)
            elif shape_mode == 'circle':
                drawCircle(screen, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        clock.tick(60)

# Function to draw lines between points
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Function to draw a rectangle between two points
def drawRectangle(screen, start, end, width, color_mode):
    c1 = 0 if color_mode == 'blue' else 255
    c2 = 255 if color_mode == 'blue' else 0
    color = (c1, c2, 0)
    pygame.draw.rect(screen, color, pygame.Rect(start[0], start[1], end[0] - start[0], end[1] - start[1]))

# Function to draw a circle between two points
def drawCircle(screen, start, end, width, color_mode):
    c1 = 0 if color_mode == 'blue' else 255
    c2 = 255 if color_mode == 'blue' else 0
    color = (c1, c2, 0)
    radius = int(((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5)
    pygame.draw.circle(screen, color, start, radius)

main()
    