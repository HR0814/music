import pygame
import time

pygame.init()

sound1 = pygame.mixer.Sound("나영석_땡2.wav")
sound2 = pygame.mixer.Sound("땡.wav")
sound3 = pygame.mixer.Sound("실로폰.wav")

def effect(a):
    if a == 1:
        sound1.play()
        time.sleep(2)
        sound1.stop()
    elif a == 2:
        sound2.play()
        time.sleep(1.5)
        sound1.stop()
    else:
        sound3.play()
        time.sleep(3)
        sound1.stop()

print(effect(1))
print(effect(2))
print(effect(3))