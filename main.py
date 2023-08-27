
from framework import *


class App(Game):
    def __init__(self, width=500, height=500) -> None:
        super().__init__(width, height)

        #img = loadImg(r"D:\Documents\GamesAssets\Art\Packs\kenney_boardgameicons\PNG\Double (128px)\character.png").convert_alpha()
        
        
        self.player = HitBox(Vector(0, 200),Vector(20,20))

        self.collider1 = HitBox(Vector(250,200), Vector(50,50))
        self.addToScene(self.player, self.collider1)
    def loop(self):
        """ Main Loop """
        speed = 300
        if Keyboard.pressed(pygame.K_LEFT):
            self.player.position.x -= speed * Game.DELTA
        if Keyboard.pressed(pygame.K_RIGHT):
            self.player.position.x += speed * Game.DELTA
        if Keyboard.pressed(pygame.K_UP):
            self.player.position.y -= speed * Game.DELTA
        if Keyboard.pressed(pygame.K_DOWN):
            self.player.position.y += speed * Game.DELTA

        collision = CollisionHandler.isOverlap(self.player, self.collider1)
        print(collision)

g = App()
g.run(60)