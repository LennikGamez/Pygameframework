import random

from framework import *
from framework.audio import playSound

class DustParticle(Particle):
    # [pos: Vector, radius, color:Color]
    def renderParticle(self, particle):
        Render.circle(particle[0], particle[1], color=particle[2])
        particle[0] += Vector(random.randint(-2, 2), random.randint(-2, 2))
        particle[1] -= 0.05+ random.random() * 0.2
        particle[2] = Color.RGB(particle[2][0], particle[2][1]-1.3, particle[2][2]-2)
        if particle[1] <= 0:
            self.deleteParticle(particle)


class Player(Object):

    def __init__(self, pos: Vector):
        super().__init__(pos)
        img = loadImg(
            r"D:\Documents\GamesAssets\Art\Packs\kenney_boardgameicons\PNG\Double (128px)\character.png").convert_alpha()

        self.sprite = Sprite(self.position, img)
        self.head = HitBox(self.position, Vector(32, 25))
        self.body = HitBox(self.position, Vector(75, 65))

        off = self.head.getCenterToPositionOffset(self.sprite.center() - Vector(0, 32))

        self.addComponent(self.sprite)
        self.addComponent(self.head, off)
        self.addComponent(self.body, self.body.getCenterToPositionOffset(self.sprite.center() + Vector(0, 15)))


class App(Game):
    def __init__(self, width=500, height=500) -> None:
        super().__init__(width, height)

        self.p = DustParticle()
        self.player = Player(Vector(10, 10))
        self.player2 = Player(Vector(500, 10))
        self.player3 = Player(Vector(500, 100))
        self.player4 = Player(Vector(500, 190))
        self.player5 = Player(Vector(500, 280))

        GroupManager.addToGroup("Players", self.player2, self.player3, self.player4, self.player5)

        self.collider1 = HitBox(Vector(250, 200), Vector(50, 50))
        self.collider1.render = lambda: Render.rect(self.collider1.position, self.collider1.size.x,
                                                    self.collider1.size.y)

        self.timer = RepeatTimer(1, lambda: print("done"))
        self.addToScene(self.collider1, self.player, self.player2, self.player3, self.player4, self.player5)

    def loop(self):
        self.p.emit()
        Render.text(Vector(250,15),"0000")
        """ Main Loop """
        for p in GroupManager.getGroup("Players"):
            p.position.x -= 100 * Game.DELTA

        speed = 300
        if Keyboard.pressed(pygame.K_LEFT):
            self.player.position.x -= speed * Game.DELTA
            g.p.addParticles([g.player.body.center(), 7, Color.WHITE])
        if Keyboard.pressed(pygame.K_RIGHT):
            self.player.position.x += speed * Game.DELTA
            g.p.addParticles([g.player.body.center(), 7, Color.WHITE])
        if Keyboard.pressed(pygame.K_UP):
            self.player.position.y -= speed * Game.DELTA
            g.p.addParticles([g.player.body.center(), 7, Color.WHITE])
        if Keyboard.pressed(pygame.K_DOWN):
            self.player.position.y += speed * Game.DELTA
            g.p.addParticles([g.player.body.center(), 7, Color.WHITE])

        collision = CollisionHandler.snapbackCollision(self.player.body, self.collider1, self.player)
        for player in GroupManager.getGroup("Players"):
            CollisionHandler.snapbackCollision(self.player.head, player.body, self.player)
            CollisionHandler.snapbackCollision(player.body, self.player.head, player)


@onMouseButtonDown
def click(e):
    if e.button == 1:
        print("stop")
    else:
        print("start")



if __name__ == "__main__":
    g = App()
    g.run(60)
