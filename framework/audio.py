import pygame

pygame.mixer.pre_init()
pygame.mixer.init()


def playSound(sound_path, volume=1, loops=0, maxtime=0, fade_ms=0):
    sound = pygame.mixer.Sound(sound_path)
    sound.set_volume(volume)
    sound.play(loops, maxtime, fade_ms)

