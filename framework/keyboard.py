import pygame


class Keyboard:

    @staticmethod
    def getKeyCode(key: str):
        """
        returns the key Code for a string. Output can be used on Keyboard.pressed() function
        """
        return pygame.key.key_code(key)


    @staticmethod
    def getKeys():
        return pygame.key.get_pressed()
    
    @staticmethod
    def pressed(key):
        if Keyboard.getKeys()[key]:
            return True
        return False