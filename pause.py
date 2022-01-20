from tkinter.tix import Tree
import pygame

pygame.init()

sound1 = pygame.mixer.Sound('찬미하라.mp3')
sound1.set_volume(0.1)
# sound1.play(-1)
# https://www.youtube.com/watch?v=omCbuCmXXaU&t

sound2 = pygame.mixer.Sound('8비트 게임 배경음악.mp3')
sound2.set_volume(0.1)
sound2.play(-1)

# https://www.youtube.com/watch?v=CFwntWyCGbc



while 1:
    a = int (input('멈추고 싶으면 1, 다시 재생하고 싶으면 2: '))
    if a == 1:
        pygame.mixer.pause()
    else :
        pygame.mixer.unpause()
