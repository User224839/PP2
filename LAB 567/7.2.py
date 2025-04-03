import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 50)

playlist = [
    r"C:\\Users\\Nurdaulet\\Music\\My universe - Kairat Nurtas.mp3", 
    r"C:\\Users\\Nurdaulet\\Music\\Растаман - Не Нужна Мне Корона.mp3", 
    r"C:\\Users\\Nurdaulet\\Music\\zattybek-kopbosynuly---akmarjan.mp3"
]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

play_music()

running = True
while running:
    screen.fill((0, 0, 0))

    for i in range(len(playlist)):
        color = (255, 255, 255) if i != current_track else (255, 255, 0)  # Желтый для активного трека
        text = font.render(str(i + 1), True, color)
        screen.blit(text, (WIDTH // 2 - 20, 50 + i * 50))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                play_music()

pygame.quit()