import pygame


class Eventhandler:
    on_keydown_funcs: list = []
    on_keyup_funcs: list = []

    @staticmethod
    def handleEvents(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game.running = False
                exit()

            if event.type == pygame.KEYDOWN:
                # Maybe pass in the event instead of the key
                runFunctions(Eventhandler.on_keydown_funcs, event.key)
            if event.type == pygame.KEYUP:
                runFunctions(Eventhandler.on_keyup_funcs, event.key)


def runFunctions(functions: list, *args):
    set(map(lambda func: func(*args), functions))


# Decorators #-----------------------------------------------

def onKeyDown(func):
    Eventhandler.on_keydown_funcs.append(func)
    return func


def onKeyUp(func):
    Eventhandler.on_keyup_funcs.append(func)
    return func
