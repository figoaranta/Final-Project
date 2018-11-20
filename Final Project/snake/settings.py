import pygame


class settings():
    def __init__(self):
        self.green = (0, 220, 0)
        self.bright_green = ( 0,225,0)
        self.red = (220,0,0)
        self.bright_red = (225,0,0)

    def music(self):
        pygame.mixer.music.load("jazz.wav")
        pygame.mixer.music.play()


    def eat_sound(self):
        self.m = pygame.mixer.Sound("bite.wav")
        self.m.play()


