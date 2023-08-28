import pygame


class Eventhandler:
    on_keydown_funcs: set = set()
    on_keyup_funcs: set = set()

    on_mousebutton_down_funcs: set = set()
    on_mousebutton_up_funcs: set = set()
    on_mousemotion_funcs: set = set()

    undhandled_event_funcs: set = set()

    @staticmethod
    def handleEvents(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game.running = False
                exit()

            if registerEventHandle(event, pygame.KEYDOWN, Eventhandler.on_keydown_funcs): continue
            if registerEventHandle(event, pygame.KEYUP, Eventhandler.on_keyup_funcs): continue
            if registerEventHandle(event, pygame.MOUSEBUTTONDOWN, Eventhandler.on_mousebutton_down_funcs): continue
            if registerEventHandle(event, pygame.MOUSEBUTTONUP, Eventhandler.on_mousebutton_up_funcs): continue
            if registerEventHandle(event, pygame.MOUSEMOTION, Eventhandler.on_mousemotion_funcs): continue

            # unhandled event gets passed in
            runFunctions(Eventhandler.undhandled_event_funcs, event)


def runFunctions(functions: set[callable], *args):
    set(map(lambda func: func(*args), functions))


def registerEventHandle(event, isEventType, funcs):
    if not event.type == isEventType:
        return False
    runFunctions(funcs, event)
    return True


# Decorators #-----------------------------------------------


def onKeyDown(func):
    Eventhandler.on_keydown_funcs.add(func)


def onKeyUp(func):
    Eventhandler.on_keyup_funcs.add(func)


def onMouseButtonDown(func):
    Eventhandler.on_mousebutton_down_funcs.add(func)


def onMouseButtonUp(func):
    Eventhandler.on_mousebutton_up_funcs.add(func)


def onMouseMotion(func):
    Eventhandler.on_mousemotion_funcs.add(func)


def unhandledEvent(func):
    Eventhandler.undhandled_event_funcs.add(func)
