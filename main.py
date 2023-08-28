from framework import *


class Particle(Position2D):
    def __int__(self, pos: Vector):
        super().__init__(self, pos)

    def render(self):
        Render.circle(self.position, 7)


class App(Game):
    def __init__(self, width=500, height=500) -> None:
        super().__init__(width, height)

        # img = loadImg(r"D:\Documents\GamesAssets\Art\Packs\kenney_boardgameicons\PNG\Double (128px)\character.png").convert_alpha()

        self.player = HitBox(Vector(0, 200), Vector(20, 20))

        self.collider1 = HitBox(Vector(250, 200), Vector(50, 50))

        self.particles = [Particle(Vector(i * 20, 400)) for i in range(10)]
        self.timer = RepeatTimer(1, lambda : print("done"))
        self.addToScene(self.collider1, self.player, *self.particles)

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

        collision = CollisionHandler.snapbackCollision(self.player, self.collider1)
        if collision.is_left():
            for p in self.particles:
                p.delete()
            self.collider1.delete()

@onMouseButtonDown
def click(e):
    if e.button == 1:
        print("stop")
        g.timer.stopTimer()
    else:
        print("start")
        g.timer.startTimer()


if __name__ == "__main__":
    g = App()
    g.run(60)
