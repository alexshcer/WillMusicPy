import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load('D:/MyFiles/Coding/MyProjects/Python/WillMusicPy/assets/audio/2.mp3')
pygame.mixer.music.play()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MUSIC_END:
            print('music end event')

        if event.type == pygame.MOUSEBUTTONDOWN:
            # play again
            pygame.mixer.music.play()